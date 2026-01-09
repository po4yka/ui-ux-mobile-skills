---
name: ui-ux-mobile
description: 'Mobile UI/UX design intelligence with Material 3, Liquid Glass, and cross-platform patterns'
agent: 'agent'
---

# ui-ux-mobile

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

Extract key information:
- **Platform**: iOS, Android, cross-platform, KMP
- **Design system**: Material 3, Liquid Glass, custom
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

| Domain | Use For |
|--------|---------|
| `style` | Visual styles by platform |
| `color` | Color palettes and systems |
| `typography` | Type scales and fonts |
| `component` | UI components cross-platform |
| `navigation` | Navigation patterns |
| `gesture` | Touch interactions |
| `accessibility` | A11y guidelines |
| `animation` | Motion design |

### Available Stacks

| Stack | Focus |
|-------|-------|
| `swiftui` | iOS 26+, Liquid Glass |
| `jetpack-compose` | Material 3, NavHost |
| `flutter` | Material/Cupertino |
| `react-native` | React Navigation |
| `kmp-compose` | expect/actual, shared UI |
| `material3` | Color roles, typography |
| `liquid-glass` | glassEffect, tinting |

---

## Example Workflow

**User request:** "Build an Android app with Material 3"

```bash
# 1. Search style
python3 .shared/ui-ux-mobile/scripts/search.py "material you dynamic" --domain style

# 2. Search color
python3 .shared/ui-ux-mobile/scripts/search.py "dynamic color android" --domain color

# 3. Search Material 3 stack
python3 .shared/ui-ux-mobile/scripts/search.py "color button" --stack material3

# 4. Search Jetpack Compose
python3 .shared/ui-ux-mobile/scripts/search.py "state navigation" --stack jetpack-compose
```

---

## Pre-Delivery Checklist

- [ ] Platform design language used correctly
- [ ] Accessibility labels on interactive elements
- [ ] 4.5:1 minimum color contrast
- [ ] 48dp/44pt minimum touch targets
- [ ] Reduce motion preference respected
- [ ] Lazy loading for long lists
