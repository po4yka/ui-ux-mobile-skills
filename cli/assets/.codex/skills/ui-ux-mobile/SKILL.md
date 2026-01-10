---
name: ui-ux-mobile
description: "Mobile UI/UX design intelligence. Material Design 3, iOS 26 Liquid Glass, KMP Compose. 7 stacks (SwiftUI, Jetpack Compose, Flutter, React Native, KMP, Material 3, Liquid Glass). Actions: plan, build, create, design, implement, review, fix, improve, optimize, prototype, refactor, migrate, compare, audit mobile UI/UX code. Platforms: iOS, Android, cross-platform, KMP. Elements: button, navigation, tab bar, bottom sheet, card, list, form, dialog. Styles: Material You, Liquid Glass, minimal, dark mode, glassmorphism, adaptive. Topics: color palette, accessibility, animation, gesture, typography, spacing, haptic feedback, dynamic color, onboarding, forms, responsive, errors, tokens, loading, performance."
---

# UI/UX Mobile - Design Intelligence for Mobile Apps

Searchable database of mobile UI styles, color systems, typography scales, components, navigation patterns, gestures, accessibility guidelines, animations, onboarding patterns, forms, responsive layouts, error handling, design tokens, spacing systems, loading states, and performance patterns for iOS (SwiftUI, Liquid Glass), Android (Jetpack Compose, Material 3), and cross-platform (Flutter, React Native, KMP).

## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

If Python is not installed, install it based on user's OS:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## How to Use This Skill

When user requests mobile UI/UX work (design, build, create, implement, review, fix, improve), follow this workflow:

### Step 1: Analyze User Requirements

Extract key information from user request:
- **Platform**: iOS, Android, cross-platform, KMP
- **Design system**: Material 3, Liquid Glass, custom
- **Style keywords**: minimal, dark mode, glassmorphism, adaptive
- **Stack**: SwiftUI, Jetpack Compose, Flutter, React Native, KMP

### Step 2: Search Relevant Domains

Use `search.py` multiple times to gather comprehensive information. Search until you have enough context.

```bash
python3 .codex/skills/ui-ux-mobile/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>] [--platform <platform>] [--format <format>]
```

**Search Options:**
- `--domain, -d` - Search domain(s), comma-separated for multi-domain search
- `--platform, -p` - Filter by platform: `ios`, `android`, `cross-platform`
- `--format, -f` - Output format: `markdown` (default), `json`, `code-only`, `summary`
- `--max-results, -n` - Maximum results (default: 3)

**Examples:**
```bash
# Single domain search
python3 .codex/skills/ui-ux-mobile/scripts/search.py "button" --domain component

# Multi-domain search
python3 .codex/skills/ui-ux-mobile/scripts/search.py "button animation" --domain component,animation

# Platform-filtered search
python3 .codex/skills/ui-ux-mobile/scripts/search.py "navigation" --domain navigation --platform ios

# Code-only output
python3 .codex/skills/ui-ux-mobile/scripts/search.py "glass" --stack swiftui --format code-only
```

**Recommended search order:**

1. **Style** - Get visual style recommendations for the platform
2. **Component** - Get cross-platform component implementations
3. **Typography** - Get platform-specific type scales
4. **Color** - Get color palette (with dynamic color support info)
5. **Navigation** - Get navigation pattern recommendations
6. **Gesture** - Get touch interaction guidelines
7. **Animation** - Get motion design patterns
8. **Accessibility** - Get a11y requirements and implementations
9. **Onboarding** - Get user onboarding patterns
10. **Forms** - Get form validation and input patterns
11. **Responsive** - Get tablet/foldable layout patterns
12. **Errors** - Get error handling and recovery patterns
13. **Tokens** - Get design token architecture
14. **Spacing** - Get spacing and sizing systems
15. **Loading** - Get loading state patterns
16. **Performance** - Get UI performance optimization patterns
17. **Stack** - Get stack-specific guidelines

### Step 3: Stack Guidelines

Search stack-specific best practices and implementation patterns.

```bash
python3 .codex/skills/ui-ux-mobile/scripts/search.py "<keyword>" --stack <stack>
```

Available stacks:
- `swiftui` - iOS 26+ with Liquid Glass
- `jetpack-compose` - Android with Material 3
- `flutter` - Cross-platform Flutter
- `react-native` - React Native patterns
- `kmp-compose` - Kotlin Multiplatform Compose
- `material3` - Material Design 3 reference
- `liquid-glass` - iOS 26 Liquid Glass reference

---

## Search Reference

### Available Domains

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `style` | Visual styles by platform | Material You, Liquid Glass, minimal, dark mode |
| `color` | Color palettes and systems | dynamic color, tonal palette, iOS system colors |
| `typography` | Type scales and fonts | display, headline, body, SF Pro, Roboto |
| `component` | UI components cross-platform | button, card, navigation bar, bottom sheet |
| `navigation` | Navigation patterns | bottom navigation, tab bar, drawer, stack |
| `gesture` | Touch interactions | swipe, tap, long press, pinch, haptic |
| `accessibility` | A11y guidelines | WCAG, VoiceOver, TalkBack, contrast, focus |
| `animation` | Motion design | spring, ease, transition, reduce motion |
| `onboarding` | User onboarding patterns | walkthrough, coach marks, progressive, empty state |
| `forms` | Form validation and inputs | validation, error state, multi-step, submit |
| `responsive` | Tablet/foldable layouts | breakpoint, adaptive, grid, window size class |
| `errors` | Error handling patterns | retry, recovery, graceful degradation, offline |
| `tokens` | Design token architecture | primitive, semantic, component, alias, theme |
| `spacing` | Spacing and sizing systems | padding, margin, baseline grid, density |
| `loading` | Loading state patterns | skeleton, shimmer, progress, streaming |
| `performance` | UI performance optimization | lazy loading, virtualization, caching, memory |

### Available Stacks

| Stack | Focus |
|-------|-------|
| `swiftui` | iOS 26+, Liquid Glass, NavigationStack, @State |
| `jetpack-compose` | Material 3, NavHost, StateFlow, remember |
| `flutter` | Material/Cupertino, Navigator 2.0, Provider |
| `react-native` | React Navigation, FlatList, StyleSheet |
| `kmp-compose` | expect/actual, StateFlow, shared UI |
| `material3` | Color roles, typography, shape, elevation |
| `liquid-glass` | glassEffect, GlassEffectContainer, tinting |

---

## Example Workflows

### iOS App with Liquid Glass

```bash
# 1. Search style for iOS 26
python3 .codex/skills/ui-ux-mobile/scripts/search.py "liquid glass iOS" --domain style

# 2. Search navigation patterns
python3 .codex/skills/ui-ux-mobile/scripts/search.py "bottom navigation iOS" --domain navigation

# 3. Search components
python3 .codex/skills/ui-ux-mobile/scripts/search.py "button sheet dialog" --domain component

# 4. Search Liquid Glass stack guidelines
python3 .codex/skills/ui-ux-mobile/scripts/search.py "glass effect grouping" --stack liquid-glass

# 5. Search SwiftUI implementation
python3 .codex/skills/ui-ux-mobile/scripts/search.py "state navigation" --stack swiftui
```

### Android App with Material 3

```bash
# 1. Search Material 3 style
python3 .codex/skills/ui-ux-mobile/scripts/search.py "material you dynamic" --domain style

# 2. Search color system
python3 .codex/skills/ui-ux-mobile/scripts/search.py "dynamic color android" --domain color

# 3. Search typography
python3 .codex/skills/ui-ux-mobile/scripts/search.py "headline body" --domain typography

# 4. Search Material 3 stack guidelines
python3 .codex/skills/ui-ux-mobile/scripts/search.py "color button" --stack material3

# 5. Search Jetpack Compose implementation
python3 .codex/skills/ui-ux-mobile/scripts/search.py "state navigation" --stack jetpack-compose
```

### Cross-Platform KMP App

```bash
# 1. Search adaptive style
python3 .codex/skills/ui-ux-mobile/scripts/search.py "adaptive cross-platform" --domain style

# 2. Search components
python3 .codex/skills/ui-ux-mobile/scripts/search.py "button navigation" --domain component

# 3. Search KMP implementation
python3 .codex/skills/ui-ux-mobile/scripts/search.py "expect actual" --stack kmp-compose

# 4. Search accessibility
python3 .codex/skills/ui-ux-mobile/scripts/search.py "screen reader" --domain accessibility
```

### Tablet/Foldable Responsive App

```bash
# 1. Search responsive patterns for tablets
python3 .codex/skills/ui-ux-mobile/scripts/search.py "tablet layout" --domain responsive

# 2. Search navigation changes for larger screens
python3 .codex/skills/ui-ux-mobile/scripts/search.py "rail drawer" --domain navigation

# 3. Search adaptive components
python3 .codex/skills/ui-ux-mobile/scripts/search.py "list detail" --domain responsive

# 4. Search spacing for density
python3 .codex/skills/ui-ux-mobile/scripts/search.py "density" --domain spacing
```

### User Onboarding Flow

```bash
# 1. Search onboarding patterns
python3 .codex/skills/ui-ux-mobile/scripts/search.py "progressive walkthrough" --domain onboarding

# 2. Search form validation for signup
python3 .codex/skills/ui-ux-mobile/scripts/search.py "email validation" --domain forms

# 3. Search loading states
python3 .codex/skills/ui-ux-mobile/scripts/search.py "skeleton progress" --domain loading

# 4. Search error handling
python3 .codex/skills/ui-ux-mobile/scripts/search.py "network error" --domain errors
```

### Design System Setup

```bash
# 1. Search design tokens architecture
python3 .codex/skills/ui-ux-mobile/scripts/search.py "semantic primitive" --domain tokens

# 2. Search spacing system
python3 .codex/skills/ui-ux-mobile/scripts/search.py "baseline grid" --domain spacing

# 3. Search color tokens
python3 .codex/skills/ui-ux-mobile/scripts/search.py "color role" --domain tokens

# 4. Search typography tokens
python3 .codex/skills/ui-ux-mobile/scripts/search.py "typography scale" --domain tokens
```

---

## Platform-Specific Rules

### iOS (SwiftUI + Liquid Glass)

| Rule | Do | Don't |
|------|----|----- |
| **Glass usage** | Use glass for navigation and controls | Apply glass to content layers |
| **Glass grouping** | Use GlassEffectContainer for related elements | Let glass sample other glass |
| **Tab bar** | Use system TabView (floating in iOS 26) | Force custom bottom navigation |
| **State** | Use @State, @StateObject, @ObservedObject correctly | Use @ObservedObject to create objects |
| **Animation** | Use spring animations with reduce motion check | Ignore prefers-reduced-motion |
| **Charts & stats** | Use Swift Charts with clear axes, summary KPIs, and tap-to-reveal values | Draw custom charts that ignore Dynamic Type or hide values |
| **Camera screens** | Use Camera Control overlays, SF Symbols, and short labels; keep viewfinder clear | Block viewfinder with controls or use custom symbols/long labels |

### Android (Jetpack Compose + Material 3)

| Rule | Do | Don't |
|------|----|----- |
| **Color** | Use MaterialTheme.colorScheme roles | Hardcode hex colors |
| **Dynamic color** | Check SDK >= 31 for dynamic color | Force dynamic color on older devices |
| **Typography** | Use MaterialTheme.typography tokens | Define custom text sizes |
| **State** | Use remember, rememberSaveable, StateFlow | Use remember for data that must survive rotation |
| **Lists** | Use LazyColumn with stable keys | Use Column with items for long lists |
| **Charts & stats** | Use Material 3 color roles, labeled legends, and tap/long-press value callouts | Encode meaning by color only or omit labels |
| **Camera screens** | Use CameraX PreviewView/CameraViewfinder with aspect-safe scaling and foldable support | Stretch previews or lock orientation and ignore window changes |

### Cross-Platform

| Rule | Do | Don't |
|------|----|----- |
| **Touch targets** | 48dp minimum on Android, 44pt on iOS | Smaller touch targets |
| **Accessibility** | Test with TalkBack AND VoiceOver | Test on one platform only |
| **Navigation** | Use platform navigation patterns | Force same navigation on all platforms |
| **Gestures** | Provide button alternatives for gestures | Require gestures without alternatives |
| **Charts & stats** | Share tokens and data model, but use native chart patterns and a text summary | Force identical interactions or skip summaries |
| **Camera screens** | Prime permissions and provide tap-to-focus, pinch-to-zoom, and capture feedback | Ask for permission cold or rely on gesture-only interactions |

---

## Pre-Delivery Checklist

### Platform Consistency
- [ ] Uses platform design language (Material 3 / Liquid Glass)
- [ ] Typography follows platform type scale
- [ ] Color system uses platform color roles
- [ ] Navigation follows platform patterns

### Accessibility
- [ ] All interactive elements have accessibility labels
- [ ] Minimum 4.5:1 color contrast for text
- [ ] Touch targets are 48dp (Android) / 44pt (iOS) minimum
- [ ] Reduce motion preference respected
- [ ] Tested with VoiceOver (iOS) / TalkBack (Android)

### Animation
- [ ] Spring animations for natural feel
- [ ] Reduce motion alternative provided
- [ ] Durations: 150-200ms for small, 300-400ms for large
- [ ] No flashing content (seizure risk)

### Performance
- [ ] Lazy loading for long lists
- [ ] Memoization for expensive computations
- [ ] Stable keys for list items
- [ ] Minimal state scope

### Responsive Design
- [ ] Tablet layouts use NavigationRail or Drawer
- [ ] Foldable devices handled with WindowSizeClass
- [ ] Grid columns adapt to screen width
- [ ] Content density appropriate for device

### Error Handling
- [ ] Network errors show retry option
- [ ] Form validation shows inline errors
- [ ] Empty states provide clear next action
- [ ] Offline mode gracefully degrades

### Loading States
- [ ] Skeleton screens for content loading
- [ ] Progress indicators for user actions
- [ ] Streaming states for real-time updates
- [ ] Pull-to-refresh where appropriate

---

## Tips for Better Results

1. **Specify platform** - "iOS button" > "button" for platform-specific results
2. **Search multiple domains** - Use comma-separated domains: `--domain component,animation`
3. **Filter by platform** - Use `--platform ios` to get platform-specific results
4. **Check accessibility** - Always search accessibility for any interactive element
5. **Use stack search** - Get implementation-specific code patterns
6. **Code-only output** - Use `--format code-only` for quick code snippets
7. **Design tokens first** - Search tokens and spacing before implementing new components
8. **Error handling** - Search errors domain for graceful degradation patterns
9. **Combine results** - Synthesize multiple searches for complete guidance
