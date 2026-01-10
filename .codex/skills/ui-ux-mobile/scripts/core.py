#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI/UX Mobile Core - BM25 search engine for mobile UI/UX design guides
Supports Material Design 3, iOS 26 Liquid Glass, KMP, and cross-platform patterns
"""

import csv
import re
from pathlib import Path
from math import log
from collections import defaultdict

# ============ CONFIGURATION ============
DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3

CSV_CONFIG = {
    "style": {
        "file": "styles.csv",
        "search_cols": ["Style", "Platform", "Keywords", "Use Cases"],
        "output_cols": ["Style", "Platform", "Keywords", "Use Cases", "Colors", "Typography", "Components", "Animation", "Example Apps"]
    },
    "color": {
        "file": "colors.csv",
        "search_cols": ["Palette Name", "Platform", "Dynamic Color Support"],
        "output_cols": ["Palette Name", "Platform", "Primary", "Secondary", "Tertiary", "Surface", "On-Surface", "Error", "Dynamic Color Support"]
    },
    "typography": {
        "file": "typography.csv",
        "search_cols": ["Style Name", "Platform", "Use Case"],
        "output_cols": ["Style Name", "Platform", "Font Family", "Size", "Weight", "Line Height", "Letter Spacing", "Use Case"]
    },
    "component": {
        "file": "components.csv",
        "search_cols": ["Component", "Platform", "Accessibility", "Best Practices"],
        "output_cols": ["Component", "Platform", "SwiftUI API", "Compose API", "Flutter API", "RN Component", "Accessibility", "Best Practices"]
    },
    "navigation": {
        "file": "navigation.csv",
        "search_cols": ["Pattern", "Platform", "Best For", "Thumb Zone"],
        "output_cols": ["Pattern", "Platform", "Implementation", "Thumb Zone", "Gesture Support", "Deep Linking", "Best For"]
    },
    "gesture": {
        "file": "gestures.csv",
        "search_cols": ["Gesture", "Platform", "Haptic Feedback", "Accessibility Alternative"],
        "output_cols": ["Gesture", "Platform", "SwiftUI", "Compose", "Flutter", "Haptic Feedback", "Accessibility Alternative"]
    },
    "accessibility": {
        "file": "accessibility.csv",
        "search_cols": ["Guideline", "WCAG Level", "Testing Method", "Priority"],
        "output_cols": ["Guideline", "WCAG Level", "iOS Implementation", "Android Implementation", "Testing Method", "Priority"]
    },
    "animation": {
        "file": "animations.csv",
        "search_cols": ["Animation Type", "Platform", "Use Case", "Reduce Motion Alternative"],
        "output_cols": ["Animation Type", "Platform", "Duration", "Easing", "SwiftUI API", "Compose API", "Use Case", "Reduce Motion Alternative"]
    },
    # New domains
    "onboarding": {
        "file": "onboarding.csv",
        "search_cols": ["Pattern", "Type", "Platform", "Best For"],
        "output_cols": ["Pattern", "Type", "Platform", "SwiftUI Implementation", "Compose Implementation", "Best For", "User Friction", "Conversion Impact", "Accessibility"]
    },
    "forms": {
        "file": "forms.csv",
        "search_cols": ["Pattern", "Category", "Platform", "Validation Timing"],
        "output_cols": ["Pattern", "Category", "Platform", "SwiftUI Implementation", "Compose Implementation", "Validation Timing", "Error Display", "Accessibility Notes"]
    },
    "responsive": {
        "file": "responsive.csv",
        "search_cols": ["Pattern", "Category", "Platform", "Width Range"],
        "output_cols": ["Pattern", "Category", "Platform", "Width Range", "SwiftUI Implementation", "Compose Implementation", "Navigation Change", "Grid Columns", "Use Case"]
    },
    "errors": {
        "file": "errors.csv",
        "search_cols": ["Pattern", "Category", "Platform", "User Message Style"],
        "output_cols": ["Pattern", "Category", "Platform", "SwiftUI Implementation", "Compose Implementation", "User Message Style", "Recovery Action", "Accessibility"]
    },
    "tokens": {
        "file": "tokens.csv",
        "search_cols": ["Token Name", "Level", "Category", "Platform"],
        "output_cols": ["Token Name", "Level", "Category", "Platform", "SwiftUI Usage", "Compose Usage", "Example Value", "Theme Support", "Description"]
    },
    "spacing": {
        "file": "spacing.csv",
        "search_cols": ["Pattern", "Category", "Platform", "Use Case"],
        "output_cols": ["Pattern", "Category", "Platform", "Value iOS", "Value Android", "SwiftUI Usage", "Compose Usage", "Use Case", "Density Mode"]
    },
    "loading": {
        "file": "loading.csv",
        "search_cols": ["Pattern", "Category", "Platform", "Use Case"],
        "output_cols": ["Pattern", "Category", "Platform", "SwiftUI Implementation", "Compose Implementation", "Duration", "Use Case", "Accessibility Alternative"]
    },
    "performance": {
        "file": "performance.csv",
        "search_cols": ["Pattern", "Category", "Platform", "Impact"],
        "output_cols": ["Pattern", "Category", "Platform", "SwiftUI Implementation", "Compose Implementation", "Impact", "Measurement", "Best Practice"]
    }
}

STACK_CONFIG = {
    "swiftui": {"file": "stacks/swiftui.csv"},
    "jetpack-compose": {"file": "stacks/jetpack-compose.csv"},
    "flutter": {"file": "stacks/flutter.csv"},
    "react-native": {"file": "stacks/react-native.csv"},
    "kmp-compose": {"file": "stacks/kmp-compose.csv"},
    "material3": {"file": "stacks/material3.csv"},
    "liquid-glass": {"file": "stacks/liquid-glass.csv"}
}

# Common columns for all stacks
_STACK_COLS = {
    "search_cols": ["Category", "Guideline", "Description", "Do", "Don't"],
    "output_cols": ["Category", "Guideline", "Description", "Do", "Don't", "Code Good", "Code Bad", "Severity", "Docs URL"]
}

AVAILABLE_STACKS = list(STACK_CONFIG.keys())


# ============ BM25 IMPLEMENTATION ============
class BM25:
    """BM25 ranking algorithm for text search"""

    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus = []
        self.doc_lengths = []
        self.avgdl = 0
        self.idf = {}
        self.doc_freqs = defaultdict(int)
        self.N = 0

    def tokenize(self, text):
        """Lowercase, split, remove punctuation, filter short words"""
        text = re.sub(r'[^\w\s]', ' ', str(text).lower())
        return [w for w in text.split() if len(w) > 2]

    def fit(self, documents):
        """Build BM25 index from documents"""
        self.corpus = [self.tokenize(doc) for doc in documents]
        self.N = len(self.corpus)
        if self.N == 0:
            return
        self.doc_lengths = [len(doc) for doc in self.corpus]
        self.avgdl = sum(self.doc_lengths) / self.N

        for doc in self.corpus:
            seen = set()
            for word in doc:
                if word not in seen:
                    self.doc_freqs[word] += 1
                    seen.add(word)

        for word, freq in self.doc_freqs.items():
            self.idf[word] = log((self.N - freq + 0.5) / (freq + 0.5) + 1)

    def score(self, query):
        """Score all documents against query"""
        query_tokens = self.tokenize(query)
        scores = []

        for idx, doc in enumerate(self.corpus):
            score = 0
            doc_len = self.doc_lengths[idx]
            term_freqs = defaultdict(int)
            for word in doc:
                term_freqs[word] += 1

            for token in query_tokens:
                if token in self.idf:
                    tf = term_freqs[token]
                    idf = self.idf[token]
                    numerator = tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                    score += idf * numerator / denominator

            scores.append((idx, score))

        return sorted(scores, key=lambda x: x[1], reverse=True)


# ============ SEARCH FUNCTIONS ============
def _load_csv(filepath):
    """Load CSV and return list of dicts"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    """Core search function using BM25"""
    if not filepath.exists():
        return []

    data = _load_csv(filepath)

    # Build documents from search columns
    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

    # BM25 search
    bm25 = BM25()
    bm25.fit(documents)
    ranked = bm25.score(query)

    # Get top results with score > 0
    results = []
    for idx, score in ranked[:max_results]:
        if score > 0:
            row = data[idx]
            results.append({col: row.get(col, "") for col in output_cols if col in row})

    return results


def detect_domain(query):
    """Auto-detect the most relevant domain from query"""
    query_lower = query.lower()

    domain_keywords = {
        "style": ["style", "design", "material", "liquid", "glass", "minimal", "dark", "theme", "visual"],
        "color": ["color", "palette", "hex", "rgb", "primary", "secondary", "tonal", "dynamic"],
        "typography": ["font", "typography", "text", "display", "headline", "body", "label", "size"],
        "component": ["button", "card", "list", "dialog", "sheet", "fab", "chip", "toggle", "slider", "textfield", "input"],
        "navigation": ["navigation", "tab", "drawer", "stack", "bottom", "rail", "deep link", "routing"],
        "gesture": ["gesture", "tap", "swipe", "drag", "pinch", "long press", "haptic", "touch"],
        "accessibility": ["accessibility", "a11y", "wcag", "screen reader", "voiceover", "talkback", "contrast", "focus"],
        "animation": ["animation", "motion", "spring", "transition", "ease", "duration", "reduce motion"],
        # New domains
        "onboarding": ["onboarding", "walkthrough", "coach", "tutorial", "empty state", "first launch", "welcome"],
        "forms": ["form", "validation", "input", "field", "submit", "error", "required", "email", "password"],
        "responsive": ["responsive", "tablet", "foldable", "breakpoint", "adaptive", "grid", "columns", "layout"],
        "errors": ["error", "retry", "failure", "crash", "recover", "offline", "timeout", "validation"],
        "tokens": ["token", "design token", "semantic", "primitive", "theme", "color role"],
        "spacing": ["spacing", "padding", "margin", "gap", "grid", "baseline", "density"],
        "loading": ["loading", "skeleton", "shimmer", "progress", "spinner", "refresh", "fetch"],
        "performance": ["performance", "memory", "battery", "optimize", "cache", "lazy", "virtualization"]
    }

    scores = {domain: sum(1 for kw in keywords if kw in query_lower) for domain, keywords in domain_keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "component"


def filter_by_platform(results, platform):
    """Filter results by platform (ios, android, cross-platform)"""
    if not platform:
        return results

    platform_lower = platform.lower()
    platform_map = {
        "ios": ["ios", "swiftui", "uikit", "apple", "iphone", "ipad"],
        "android": ["android", "compose", "material", "kotlin", "google"],
        "cross-platform": ["cross-platform", "flutter", "react native", "kmp", "multiplatform"]
    }

    keywords = platform_map.get(platform_lower, [platform_lower])

    filtered = []
    for row in results:
        platform_value = str(row.get("Platform", "")).lower()
        if any(kw in platform_value for kw in keywords) or "cross" in platform_value:
            filtered.append(row)

    return filtered if filtered else results  # Return original if no matches


def search_multi_domain(query, domains, max_results=MAX_RESULTS, platform=None):
    """Search across multiple domains"""
    all_results = []

    for domain in domains:
        if domain not in CSV_CONFIG:
            continue

        config = CSV_CONFIG[domain]
        filepath = DATA_DIR / config["file"]

        if not filepath.exists():
            continue

        results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)

        # Add domain tag to results
        for r in results:
            r["_domain"] = domain

        all_results.extend(results)

    # Filter by platform if specified
    if platform:
        all_results = filter_by_platform(all_results, platform)

    # Sort by BM25 score would require re-scoring, so just interleave for now
    # Return top max_results
    return all_results[:max_results]


def search(query, domain=None, max_results=MAX_RESULTS):
    """Main search function with auto-domain detection"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["component"])
    filepath = DATA_DIR / config["file"]

    if not filepath.exists():
        return {"error": f"File not found: {filepath}", "domain": domain}

    results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)

    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results
    }


def search_stack(query, stack, max_results=MAX_RESULTS):
    """Search stack-specific guidelines"""
    if stack not in STACK_CONFIG:
        return {"error": f"Unknown stack: {stack}. Available: {', '.join(AVAILABLE_STACKS)}"}

    filepath = DATA_DIR / STACK_CONFIG[stack]["file"]

    if not filepath.exists():
        return {"error": f"Stack file not found: {filepath}", "stack": stack}

    results = _search_csv(filepath, _STACK_COLS["search_cols"], _STACK_COLS["output_cols"], query, max_results)

    return {
        "domain": "stack",
        "stack": stack,
        "query": query,
        "file": STACK_CONFIG[stack]["file"],
        "count": len(results),
        "results": results
    }
