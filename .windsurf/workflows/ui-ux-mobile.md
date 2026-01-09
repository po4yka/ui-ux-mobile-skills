---
description: Plan and implement mobile UI
auto_execution_mode: 3
---

# UI/UX Mobile - Design Intelligence for Mobile Apps

Searchable database of mobile UI styles, color systems, typography scales, components, navigation patterns, gestures, accessibility guidelines, and animations for iOS (SwiftUI, Liquid Glass), Android (Jetpack Compose, Material 3), and cross-platform (Flutter, React Native, KMP).

## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

---

## How to Use This Workflow

When user requests mobile UI/UX work (design, build, create, implement, review, fix, improve), follow this workflow:

### Step 1: Analyze User Requirements

Extract key information from user request:
- **Platform**: iOS, Android, cross-platform, KMP
- **Design system**: Material 3, Liquid Glass, custom
- **Style keywords**: minimal, dark mode, glassmorphism, adaptive
- **Stack**: SwiftUI, Jetpack Compose, Flutter, React Native, KMP

### Step 2: Search Relevant Domains

```bash
python3 .shared/ui-ux-mobile/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**Domains:** style, color, typography, component, navigation, gesture, accessibility, animation

### Step 3: Stack Guidelines

```bash
python3 .shared/ui-ux-mobile/scripts/search.py "<keyword>" --stack <stack>
```

**Stacks:** swiftui, jetpack-compose, flutter, react-native, kmp-compose, material3, liquid-glass

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

### Available Stacks

| Stack | Focus |
|-------|-------|
| `swiftui` | iOS 26+, Liquid Glass, NavigationStack |
| `jetpack-compose` | Material 3, NavHost, StateFlow |
| `flutter` | Material/Cupertino, Navigator 2.0 |
| `react-native` | React Navigation, FlatList |
| `kmp-compose` | expect/actual, StateFlow, shared UI |
| `material3` | Color roles, typography, shape |
| `liquid-glass` | glassEffect, GlassEffectContainer |

---

## Example Workflow

**User request:** "Build an iOS app with Liquid Glass design"

```bash
# 1. Search style
python3 .shared/ui-ux-mobile/scripts/search.py "liquid glass iOS" --domain style

# 2. Search navigation
python3 .shared/ui-ux-mobile/scripts/search.py "bottom navigation iOS" --domain navigation

# 3. Search Liquid Glass stack
python3 .shared/ui-ux-mobile/scripts/search.py "glass effect grouping" --stack liquid-glass

# 4. Search SwiftUI implementation
python3 .shared/ui-ux-mobile/scripts/search.py "state navigation" --stack swiftui

# 5. Search accessibility
python3 .shared/ui-ux-mobile/scripts/search.py "reduce transparency" --domain accessibility
```

---

## Platform-Specific Rules

### iOS (SwiftUI + Liquid Glass)

| Rule | Do | Don't |
|------|----|----- |
| **Glass usage** | Use glass for navigation and controls | Apply glass to content layers |
| **State** | Use @State, @StateObject correctly | Use @ObservedObject to create objects |
| **Animation** | Use spring animations | Ignore prefers-reduced-motion |

### Android (Jetpack Compose + Material 3)

| Rule | Do | Don't |
|------|----|----- |
| **Color** | Use MaterialTheme.colorScheme roles | Hardcode hex colors |
| **Typography** | Use MaterialTheme.typography tokens | Define custom text sizes |
| **Lists** | Use LazyColumn with stable keys | Use Column for long lists |

---

## Pre-Delivery Checklist

### Platform Consistency
- [ ] Uses platform design language (Material 3 / Liquid Glass)
- [ ] Typography follows platform type scale
- [ ] Navigation follows platform patterns

### Accessibility
- [ ] Accessibility labels on interactive elements
- [ ] 4.5:1 minimum color contrast
- [ ] 48dp/44pt minimum touch targets
- [ ] Reduce motion preference respected

### Performance
- [ ] Lazy loading for long lists
- [ ] Memoization for expensive computations
- [ ] Stable keys for list items
