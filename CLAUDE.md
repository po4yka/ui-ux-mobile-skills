# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

UI/UX Mobile is an AI-powered design intelligence toolkit providing searchable databases of mobile UI styles, color systems, typography scales, components, navigation patterns, gestures, accessibility guidelines, and animations. It works as a skill/workflow for AI coding assistants (Claude Code, Windsurf, Cursor, etc.).

Supports:
- **iOS**: SwiftUI with iOS 26 Liquid Glass
- **Android**: Jetpack Compose with Material Design 3
- **Cross-platform**: Flutter, React Native, Kotlin Multiplatform (KMP)

## Search Command

```bash
python3 .claude/skills/ui-ux-mobile/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
```

**Domain search:**
- `style` - Visual styles by platform (Material You, Liquid Glass, minimal)
- `color` - Color palettes and systems (dynamic color, tonal palette)
- `typography` - Type scales and fonts (display, headline, body)
- `component` - UI components cross-platform (button, card, sheet)
- `navigation` - Navigation patterns (bottom nav, tab bar, drawer)
- `gesture` - Touch interactions (swipe, tap, haptic)
- `accessibility` - A11y guidelines (WCAG, VoiceOver, TalkBack)
- `animation` - Motion design (spring, ease, reduce motion)

**Stack search:**
```bash
python3 .claude/skills/ui-ux-mobile/scripts/search.py "<query>" --stack <stack>
```
Available stacks: `swiftui`, `jetpack-compose`, `flutter`, `react-native`, `kmp-compose`, `material3`, `liquid-glass`

## Architecture

```
.claude/skills/ui-ux-mobile/    # Claude Code skill
├── SKILL.md                      # Skill definition with workflow instructions
├── scripts/
│   ├── search.py                 # CLI entry point
│   └── core.py                   # BM25 search engine
└── data/                         # CSV databases
    ├── styles.csv                # Mobile visual styles
    ├── colors.csv                # Color systems
    ├── typography.csv            # Type scales
    ├── components.csv            # UI components
    ├── navigation.csv            # Navigation patterns
    ├── gestures.csv              # Touch interactions
    ├── accessibility.csv         # A11y guidelines
    ├── animations.csv            # Motion design
    └── stacks/                   # Stack-specific guidelines (7 CSV files)

.windsurf/workflows/              # Windsurf workflow
.cursor/rules/                    # Cursor rules
.agent/workflows/ui-ux-mobile/    # Generic agent workflow
.github/prompts/                  # GitHub Copilot prompt
.kiro/steering/                   # Kiro steering file
.shared/ui-ux-mobile/             # Shared data copy

docs/                             # Research documentation
├── MATERIAL3.md                  # Material Design 3 guide
├── IOS26-LIQUID-GLASS.md         # iOS 26 Liquid Glass guide
├── KMP-UNIFIED-UI.md             # KMP unified interface guide
└── MODERN-MOBILE-UIUX.md         # Modern mobile UX practices
```

The search engine uses BM25 ranking. Domain auto-detection is available when `--domain` is omitted.

## Sync Rules

When modifying files, keep all agent workflows in sync:

- **Data & Scripts** (`data/`, `scripts/`): Copy changes to `.shared/ui-ux-mobile/`
- **SKILL.md**: Update corresponding files in `.agent/`, `.cursor/`, `.windsurf/`, `.github/prompts/`, `.kiro/steering/`

## Prerequisites

Python 3.x (no external dependencies required)

## Git Workflow

Never push directly to `main`. Always:

1. Create a new branch: `git checkout -b feat/...` or `fix/...`
2. Commit changes
3. Push branch: `git push -u origin <branch>`
4. Create PR: `gh pr create`
