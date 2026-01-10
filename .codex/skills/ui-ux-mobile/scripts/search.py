#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI/UX Mobile Search - BM25 search engine for mobile UI/UX design guides
Usage: python search.py "<query>" [--domain <domain>] [--stack <stack>] [--platform <platform>] [--format <format>] [-n <max>]

Domains: style, color, typography, component, navigation, gesture, accessibility, animation,
         onboarding, forms, responsive, errors, tokens, spacing, loading, performance

Stacks: swiftui, jetpack-compose, flutter, react-native, kmp-compose, material3, liquid-glass

Platforms: ios, android, cross-platform

Formats: markdown (default), json, code-only, summary
"""

import argparse
from core import CSV_CONFIG, AVAILABLE_STACKS, MAX_RESULTS, search, search_stack, search_multi_domain, filter_by_platform


def format_output(result, output_format="markdown"):
    """Format results based on output format"""
    if "error" in result:
        return f"Error: {result['error']}"

    if output_format == "summary":
        return format_summary(result)
    elif output_format == "code-only":
        return format_code_only(result)
    else:
        return format_markdown(result)


def format_markdown(result):
    """Format results as markdown (default)"""
    output = []
    if result.get("stack"):
        output.append(f"## UI/UX Mobile Stack Guidelines")
        output.append(f"**Stack:** {result['stack']} | **Query:** {result['query']}")
    elif result.get("domains"):
        output.append(f"## UI/UX Mobile Multi-Domain Search")
        output.append(f"**Domains:** {', '.join(result['domains'])} | **Query:** {result['query']}")
    else:
        output.append(f"## UI/UX Mobile Search Results")
        output.append(f"**Domain:** {result['domain']} | **Query:** {result['query']}")

    if result.get("platform"):
        output.append(f"**Platform Filter:** {result['platform']}")

    output.append(f"**Source:** {result.get('file', 'multiple')} | **Found:** {result['count']} results\n")

    for i, row in enumerate(result['results'], 1):
        domain_tag = f" [{row.get('_domain', '')}]" if '_domain' in row else ""
        output.append(f"### Result {i}{domain_tag}")
        for key, value in row.items():
            if key.startswith('_'):
                continue
            value_str = str(value)
            if len(value_str) > 300:
                value_str = value_str[:300] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")

    return "\n".join(output)


def format_summary(result):
    """Format results as brief summary"""
    output = []
    output.append(f"## Search: {result['query']}")
    output.append(f"Found {result['count']} results\n")

    for i, row in enumerate(result['results'], 1):
        # Get first meaningful column
        name = row.get("Pattern") or row.get("Component") or row.get("Style") or row.get("Guideline") or row.get("Animation Type") or "Result"
        platform = row.get("Platform", "")
        output.append(f"{i}. **{name}** ({platform})")

    return "\n".join(output)


def format_code_only(result):
    """Extract only code examples from results"""
    output = []
    output.append(f"## Code Examples: {result['query']}\n")

    for row in result['results']:
        # Look for code columns
        code_good = row.get("Code Good") or row.get("SwiftUI API") or row.get("SwiftUI Implementation")
        code_bad = row.get("Code Bad") or row.get("Compose API") or row.get("Compose Implementation")
        name = row.get("Pattern") or row.get("Guideline") or row.get("Component") or "Example"

        if code_good:
            output.append(f"### {name}")
            output.append(f"**Good:** `{code_good}`")
            if code_bad:
                output.append(f"**Bad:** `{code_bad}`")
            output.append("")

    return "\n".join(output) if len(output) > 1 else "No code examples found"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UI/UX Mobile Search")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", help="Search domain(s), comma-separated for multiple")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help="Stack-specific search")
    parser.add_argument("--platform", "-p", choices=["ios", "android", "cross-platform"], help="Filter by platform")
    parser.add_argument("--format", "-f", choices=["markdown", "json", "code-only", "summary"], default="markdown", help="Output format")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="Max results (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output as JSON (shortcut for --format json)")

    args = parser.parse_args()

    # Handle format argument
    output_format = "json" if args.json else args.format

    # Stack search takes priority
    if args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
    elif args.domain and "," in args.domain:
        # Multi-domain search
        domains = [d.strip() for d in args.domain.split(",")]
        valid_domains = [d for d in domains if d in CSV_CONFIG]
        results = search_multi_domain(args.query, valid_domains, args.max_results, args.platform)
        result = {
            "domains": valid_domains,
            "query": args.query,
            "platform": args.platform,
            "count": len(results),
            "results": results
        }
    else:
        result = search(args.query, args.domain, args.max_results)
        # Apply platform filter for single domain search
        if args.platform and result.get("results"):
            result["results"] = filter_by_platform(result["results"], args.platform)
            result["count"] = len(result["results"])
            result["platform"] = args.platform

    if output_format == "json":
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_output(result, output_format))
