# TOKEN_TAXONOMY

This outlines the token hierarchy and naming scheme used to align iOS, Android, and cross‑platform UI while preserving native feel.

---

## Levels

1) **Primitive tokens**  
Raw values with no semantic meaning. These are the building blocks.
- Examples: `color.blue.500`, `space.8`, `radius.12`, `opacity.80`, `duration.200`

2) **Semantic tokens**  
Contextual roles mapped to platform systems (Material 3 roles, iOS system colors).
- Examples: `color.primary`, `color.onPrimary`, `surface.default`, `text.primary`

3) **Component tokens**  
Component‑specific values and state variants.
- Examples: `button.primary.bg`, `button.primary.bgPressed`, `textfield.borderFocus`

---

## Categories

- **Color**: brand, surface, outline, error, success, warning
- **Typography**: size, weight, lineHeight, letterSpacing
- **Spacing**: padding, margin, gap
- **Radius**: corner radii
- **Elevation/Shadow**: depth and overlays
- **Motion**: duration, easing, spring
- **Opacity**: disabled states, scrims

---

## Naming Guidelines

- Use dot notation: `category.subcategory.role`
- Prefer semantic roles for UI usage
- Keep primitive tokens unbranded
- Define component tokens only when needed for consistency

**Examples**
- Primitive: `color.neutral.100`, `space.16`, `radius.8`
- Semantic: `color.primary`, `text.secondary`, `surface.elevated`
- Component: `button.primary.bg`, `button.primary.text`, `chip.selected.bg`

---

## Platform Mapping (Examples)

| Semantic Token | iOS (SwiftUI) | Android (Compose) |
|---------------|--------------|------------------|
| `color.primary` | `Color.accentColor` or custom | `MaterialTheme.colorScheme.primary` |
| `color.onPrimary` | custom `Color` | `MaterialTheme.colorScheme.onPrimary` |
| `surface.default` | `Color(.systemBackground)` | `MaterialTheme.colorScheme.surface` |
| `text.primary` | `Color.primary` | `MaterialTheme.colorScheme.onSurface` |

---

## Current State vs Target

- **Current**: Tokens are mostly **semantic** (see `tokens.csv`).
- **Target**: Add **primitive** and **component** layers to support scalable theming and per‑component consistency.

---

## Recommended Next Additions

- Primitive tokens for color scale, spacing scale, radius scale.
- Component tokens for primary buttons, text fields, sheets, and cards.
- Motion tokens for default durations and easing.
