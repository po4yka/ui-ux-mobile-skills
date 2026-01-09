# UI/UX Mobile - Design Intelligence for Mobile Apps

AI-powered design intelligence toolkit for mobile UI/UX development. Provides searchable databases of styles, colors, typography, components, navigation, gestures, accessibility, and animations.

## Supported Platforms

- **iOS**: SwiftUI with iOS 26 Liquid Glass
- **Android**: Jetpack Compose with Material Design 3
- **Cross-platform**: Flutter, React Native, Kotlin Multiplatform (KMP)

## Features

- **8 Search Domains**: style, color, typography, component, navigation, gesture, accessibility, animation
- **7 Stack Guides**: SwiftUI, Jetpack Compose, Flutter, React Native, KMP, Material 3, Liquid Glass
- **Zero Dependencies**: Pure Python with BM25 search algorithm
- **Multi-AI Support**: Works with Claude Code, Cursor, Windsurf, GitHub Copilot, Kiro

## Quick Start

### Search by Domain

```bash
# Search mobile styles
python3 .claude/skills/ui-ux-mobile/scripts/search.py "liquid glass" --domain style

# Search color systems
python3 .claude/skills/ui-ux-mobile/scripts/search.py "dynamic color" --domain color

# Search components
python3 .claude/skills/ui-ux-mobile/scripts/search.py "bottom sheet" --domain component

# Search accessibility
python3 .claude/skills/ui-ux-mobile/scripts/search.py "screen reader" --domain accessibility
```

### Search by Stack

```bash
# SwiftUI + Liquid Glass
python3 .claude/skills/ui-ux-mobile/scripts/search.py "glass effect" --stack swiftui

# Jetpack Compose + Material 3
python3 .claude/skills/ui-ux-mobile/scripts/search.py "state navigation" --stack jetpack-compose

# Flutter
python3 .claude/skills/ui-ux-mobile/scripts/search.py "theme provider" --stack flutter

# KMP Compose
python3 .claude/skills/ui-ux-mobile/scripts/search.py "expect actual" --stack kmp-compose
```

## Available Domains

| Domain | Description |
|--------|-------------|
| `style` | Visual styles by platform (Material You, Liquid Glass, minimal) |
| `color` | Color palettes and systems (dynamic color, tonal palette) |
| `typography` | Type scales and fonts (display, headline, body) |
| `component` | UI components cross-platform (button, card, sheet) |
| `navigation` | Navigation patterns (bottom nav, tab bar, drawer) |
| `gesture` | Touch interactions (swipe, tap, haptic) |
| `accessibility` | A11y guidelines (WCAG, VoiceOver, TalkBack) |
| `animation` | Motion design (spring, ease, reduce motion) |

## Available Stacks

| Stack | Focus |
|-------|-------|
| `swiftui` | iOS 26+, Liquid Glass, NavigationStack, @State |
| `jetpack-compose` | Material 3, NavHost, StateFlow, remember |
| `flutter` | Material/Cupertino, Navigator 2.0, Provider |
| `react-native` | React Navigation, FlatList, StyleSheet |
| `kmp-compose` | expect/actual, StateFlow, shared UI |
| `material3` | Color roles, typography, shape, elevation |
| `liquid-glass` | glassEffect, GlassEffectContainer, tinting |

## Documentation

Detailed research documentation available in `docs/`:

- **[Material Design 3](docs/MATERIAL3.md)** - Complete Material 3 guide
- **[iOS 26 Liquid Glass](docs/IOS26-LIQUID-GLASS.md)** - Liquid Glass design system
- **[KMP Unified UI](docs/KMP-UNIFIED-UI.md)** - Kotlin Multiplatform guide
- **[Modern Mobile UX](docs/MODERN-MOBILE-UIUX.md)** - Best practices guide

## Project Structure

```
ui-ux-mobile-skills/
├── .claude/skills/ui-ux-mobile/     # Claude Code skill
│   ├── SKILL.md                      # Skill definition
│   ├── scripts/                      # Search engine
│   └── data/                         # CSV databases
├── .cursor/rules/                    # Cursor rules
├── .windsurf/workflows/              # Windsurf workflow
├── .agent/workflows/                 # Generic agent workflow
├── .github/prompts/                  # GitHub Copilot prompt
├── .kiro/steering/                   # Kiro steering
├── .shared/ui-ux-mobile/             # Shared data
└── docs/                             # Research documentation
```

## Requirements

- Python 3.x (no external dependencies)

## License

MIT
