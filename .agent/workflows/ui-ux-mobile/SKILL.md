---
name: ui-ux-mobile
description: "Mobile UI/UX design intelligence. Material Design 3, iOS 26 Liquid Glass, KMP Compose."
---

# UI/UX Mobile - Design Intelligence for Mobile Apps

Searchable database for iOS, Android, and cross-platform mobile UI/UX.

## Search Commands

```bash
# Domain search
python3 .shared/ui-ux-mobile/scripts/search.py "<keyword>" --domain <domain>

# Stack search
python3 .shared/ui-ux-mobile/scripts/search.py "<keyword>" --stack <stack>
```

**Domains:** style, color, typography, component, navigation, gesture, accessibility, animation

**Stacks:** swiftui, jetpack-compose, flutter, react-native, kmp-compose, material3, liquid-glass

## Workflow

1. **Analyze** - Extract platform, design system, style, stack from request
2. **Search** - Query relevant domains and stacks
3. **Implement** - Apply platform-specific patterns

## Platform Rules

### iOS (Liquid Glass)
- Glass for navigation/controls only
- GlassEffectContainer for grouping
- Spring animations

### Android (Material 3)
- MaterialTheme.colorScheme roles
- Dynamic color on SDK 31+
- LazyColumn with stable keys

### Cross-Platform
- 48dp/44pt touch targets
- Test TalkBack and VoiceOver
- Reduce motion alternatives
