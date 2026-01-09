# Apple iOS 26 Liquid Glass Design System

> Last updated: January 2026
> iOS version: 26.x
> Announced: WWDC 2025 (June 9, 2025)
> Released: September 15, 2025

## Table of Contents

1. [Overview](#overview)
2. [Core Design Principles](#core-design-principles)
3. [Visual Characteristics](#visual-characteristics)
4. [Glass Materials](#glass-materials)
5. [Component Adoption](#component-adoption)
6. [SwiftUI Implementation](#swiftui-implementation)
7. [UIKit Implementation](#uikit-implementation)
8. [Color and Materials](#color-and-materials)
9. [Motion and Animation](#motion-and-animation)
10. [Accessibility](#accessibility)
11. [Icon Design Guidelines](#icon-design-guidelines)
12. [Official Documentation](#official-documentation)

---

## Overview

Liquid Glass is Apple's most significant design evolution since iOS 7 (2013). It represents a unified design language spanning iOS 26, iPadOS 26, macOS Tahoe 26, watchOS 26, tvOS 26, and visionOS 26.

### What is Liquid Glass?

A dynamic "meta-material" that:
- Reflects and refracts its surroundings
- Responds fluidly to user interaction
- Creates depth through translucency and layering
- Adapts intelligently to underlying content

### Design Inspirations

Liquid Glass synthesizes elements from:
- **macOS Aqua**: Translucency and depth concepts
- **iOS 7**: Real-time Gaussian blurring
- **iPhone X**: Motion and dynamic interactions
- **Dynamic Island**: Fluid, morphing UI paradigms
- **visionOS**: Glass-like transparent interfaces

---

## Core Design Principles

Apple defines three fundamental principles for Liquid Glass:

### 1. Hierarchy

> "Establish a clear visual hierarchy where controls and interface elements elevate and distinguish the content beneath them."

**Implementation:**
- Foreground elements: Crisp edges, soft highlights
- Mid-layers: Translucent with adaptive tint
- Backgrounds: Intelligent blur based on brightness/contrast

### 2. Harmony

> "Align with the concentric design of the hardware and software to create harmony between interface elements, system experiences, and devices."

**Implementation:**
- Interface elements match device curves
- Consistent behavior across Apple platforms
- Visual continuity between app and system UI

### 3. Consistency

> "Adopt platform conventions to maintain a consistent design that continuously adapts across window sizes and displays."

**Implementation:**
- Follow platform-specific behaviors
- Adapt to different screen sizes
- Maintain recognizable patterns

---

## Visual Characteristics

### Translucency and Depth

Liquid Glass treats UI as overlapping sheets of glass:

| Layer | Characteristics |
|-------|-----------------|
| **Foreground** | Crisp edges, bright highlights, full opacity |
| **Midground** | Translucent, adaptive tint for readability |
| **Background** | Intelligent blur, content-aware adaptation |

### Light Interactions

- **Specular Highlights**: Dynamic reflections responding to device orientation
- **Lensing Effect**: Real-time light bending along edges and surfaces
- **Parallax Depth**: Subtle 3D effects when tilting device
- **Illumination Spread**: Material glows on interaction

### Blur Effects

- **Gaussian Blur**: Real-time with content-aware adjustments
- **Adaptive Blur**: System adjusts intensity based on background
- **Scroll Edge Effects**: Gradual blur fading at edges
- **Metal Compositing**: Hardware-accelerated performance

---

## Glass Materials

### Two Primary Variants

| Property | Regular | Clear |
|----------|---------|-------|
| **Adaptivity** | Full adaptive behaviors | No adaptation |
| **Transparency** | Dynamic opacity | Permanently transparent |
| **Use Case** | Most versatile, works anywhere | Media-rich content backgrounds |
| **Legibility** | Built-in through adaptation | Requires dimming layer beneath |
| **Color Shift** | Tone range from underlying content | Static appearance |

### Choosing the Right Variant

**Use Regular Glass when:**
- Building navigation controls
- Creating floating buttons
- Designing toolbars and tab bars
- Content beneath varies

**Use Clear Glass when:**
- Displaying over consistent backgrounds
- Media playback controls
- Photo/video viewing interfaces
- Maximum content visibility needed

---

## Component Adoption

### Navigation Elements

#### Navigation Bars / Toolbars
- Enhanced with floating glass effect
- Top bar buttons on separate glass layer
- Most labeled actions now icon-only
- Buttons have defined space for recognition

#### Tab Bars
- Now floating and dynamic
- Shrink when scrolling (focus on content)
- Expand fluidly when scrolling back
- Separate functional layer above content

#### Sidebars
- Larger elements with deeper shadows
- Pronounced lensing effects
- Contextual adaptation based on content

### Sheets and Modals

#### Action Sheets / Alerts
- Transform from rigid boxes to floating glass
- Lighter, more consistent appearance
- Use Liquid Glass material

#### Full-Screen Modals
- Cover screen without visual stack (iOS 26)
- Visual stack only for additional modals
- System-enforced corner radii
- Concentric corners for consistency

#### Partial Height Sheets
- Inset by default with glass background
- Bottom edges nest in display curves
- Transition to opaque at full height

### System Controls

#### Buttons
- `.buttonStyle(.glass)` - Translucent secondary actions
- `.buttonStyle(.glassProminent)` - Opaque primary actions
- Interactive scaling, bouncing, shimmering on touch

#### Updated Controls
- Text fields, sliders, toggles
- Alerts and panels
- Popovers and menus
- Context-sensitive controls
- System notifications

---

## SwiftUI Implementation

### Core Modifier: glassEffect()

```swift
func glassEffect<S: Shape>(
    _ glass: Glass = .regular,
    in shape: S = DefaultGlassEffectShape,
    isEnabled: Bool = true
) -> some View
```

### Basic Usage

```swift
// Standard glass effect
RoundedRectangle(cornerRadius: 16)
    .glassEffect(.regular)
    .frame(height: 100)

// Clear glass variant
Circle()
    .glassEffect(.clear)

// Custom shape
Capsule()
    .glassEffect(.regular, in: .capsule)

// Concentric corners (match container)
Rectangle()
    .glassEffect(.regular, in: .rect(cornerRadius: .containerConcentric))
```

### Tinting Glass

```swift
// Color-tinted glass
Rectangle()
    .glassEffect(.regular.tint(.blue))

// Custom tint with opacity
Circle()
    .glassEffect(.regular.tint(.yellow.opacity(0.3)))
```

### Interactive Effects

```swift
// Make glass respond to touch
Button("Action") { }
    .glassEffect(.regular)
    .interactive()

// Combined interactive glass
Circle()
    .glassEffect(.regular.tint(.blue).interactive())
```

### Glass Effect ID (Morphing)

```swift
@Namespace var namespace

// Associate related glass elements
Circle()
    .glassEffect(.regular)
    .glassEffectID("circle1", in: namespace)

RoundedRectangle(cornerRadius: 8)
    .glassEffect(.regular)
    .glassEffectID("rect1", in: namespace)
```

### GlassEffectContainer (Grouping)

Glass cannot sample other glass. Use `GlassEffectContainer` to group related elements:

```swift
@Namespace var namespace

GlassEffectContainer {
    Circle()
        .glassEffect(.regular)
        .glassEffectID("item1", in: namespace)

    RoundedRectangle(cornerRadius: 8)
        .glassEffect(.regular)
        .glassEffectID("item2", in: namespace)
}
```

**Benefits:**
- Combines shapes into single morphable shape
- Blends overlapping shapes
- Consistent blur and lighting
- Enables smooth morphing transitions
- Improves rendering performance

### Button Styles

```swift
// Secondary action (translucent)
Button("Secondary") { }
    .buttonStyle(.glass)

// Primary action (opaque prominent)
Button("Primary") { }
    .buttonStyle(.glassProminent)
```

### Glass Effect Transitions

```swift
enum GlassEffectTransition {
    case identity          // No transition
    case matchedGeometry   // Morphing between shapes
    case materialize       // Appear/disappear animation
}
```

---

## UIKit Implementation

### UIGlassEffect

```swift
// Create glass effect view
let glassView = UIVisualEffectView(effect: UIGlassEffect())
glassView.frame = CGRect(x: 0, y: 0, width: 200, height: 100)
view.addSubview(glassView)
```

### UIGlassContainerEffect

```swift
// Group glass elements for uniform adaptation
let containerEffect = UIGlassContainerEffect()
// Configure container...
```

### Interactive Features

- Interactive scaling and bouncing capabilities
- Materialization and dematerialization animations
- Custom gesture handling for glass views

---

## Color and Materials

### System Materials

Liquid Glass builds on Apple's system materials:
- Composited through Metal for performance
- Clear variant uses live scene sampling
- Automatic light/dark mode adaptation

### Vibrancy Effects

Apply vibrancy to elements on top of glass:

```swift
// Use fills, transparency, and vibrancy
// instead of glass on glass
Text("Label")
    .foregroundStyle(.secondary)  // Uses vibrancy automatically
```

**Best Practice:** Never stack glass on glass. Use vibrancy effects instead.

### Color Adaptation

| Behavior | Description |
|----------|-------------|
| **Neutral Base** | Grays, white, beige foundation |
| **Content-Informed** | Color influenced by surroundings |
| **Automatic Switching** | Light/dark variants as needed |
| **Tone Generation** | Range based on underlying brightness |

### Contextual Tinting

```swift
// Selective tinting for primary elements
.glassEffect(.regular.tint(.accentColor))
```

**Guidelines:**
- Use selectively for primary elements only
- Avoid tinting all elements (creates confusion)
- Mimics physical colored glass behavior

---

## Motion and Animation

### Fluid Animation Principles

- **Instant Response**: Reacts immediately to interaction
- **Temporary Lift**: Elements lift during interaction
- **Dynamic Morphing**: Controls morph between states
- **Velocity Continuity**: Maintains gesture momentum

### Spring Animations

Apple's recommended approach for natural motion:

```swift
withAnimation(.spring(duration: 0.4, bounce: 0.2)) {
    // State change
}
```

**Characteristics:**
- Automatically tracks gesture velocities
- Maintains continuity for static and velocity cases
- New spring presets available
- Duration and bounce customizable

### Gesture-Driven Interactions

```swift
// Fluid gesture modifiers
.gesture(
    DragGesture()
        .onChanged { value in
            // Haptic feedback linked to ripple animations
        }
)
```

### Material Transitions

**Materialization/Dematerialization:**
- Elements appear by modulating light bending
- Graceful transitions as glass appears/disappears
- Smooth merging like water droplets when overlapping

### Performance Optimization

| Device | Behavior |
|--------|----------|
| **Newer Chips** | Full detail reflections and depth |
| **Older Devices** | Reduced highlights and parallax |
| **Low Power Mode** | Minimal animation flourishes |
| **Reduced Motion** | Disabled elastic properties |

---

## Accessibility

### Supported System Settings

#### Reduce Transparency (Primary)
- Adds darker backgrounds to translucent areas
- Frosted appearance obscures more background
- Most effective single setting for minimizing effects

```swift
// System automatically respects this setting
// No additional code required
```

#### Increase Contrast
- Produces predominantly black/white display
- Enhanced contrasting borders
- Combined with Reduce Transparency for maximum effect

#### Reduce Motion
- Eliminates lensing light bending effects
- Preserves depth and hierarchy
- Trims parallax and long transitions
- Keeps core visual structure

### iOS 26.1+ Enhancement

**Settings > Display & Brightness > Liquid Glass**
- Choose between appearance options
- "Tinted" option for more opaque look
- Only available when Reduce Transparency is OFF

### Legibility Guidelines

| Element Type | Behavior |
|--------------|----------|
| Small (navbars, tabbars) | Flip between light/dark based on background |
| Large (menus, sidebars) | Adapt contextually without flipping |
| Symbols/Glyphs | Mirror glass behavior for maximum contrast |

**Minimum Contrast:** 4.5:1 (WCAG AA standard)

---

## Icon Design Guidelines

### Layered System Requirements

Icons must work across four appearance modes:
1. **Default** - Standard with Liquid Glass effects
2. **Clear Light** - Transparent, showing wallpaper
3. **Clear Dark** - Original colors with glass effect
4. **Tinted** - User-selected color overlay

### Design Rules

- Keep silhouette identical across all modes
- Recognition must never drop across modes
- Keep elements centered to avoid clipping
- System applies masking for final shape

### Icon Asset Requirements

Provide assets for each appearance mode:
- Same silhouette across all variants
- Appropriate contrast for each mode
- Centered design within safe area

---

## Official Documentation

### Primary Apple Resources

| Resource | URL |
|----------|-----|
| Meet Liquid Glass (WWDC25 Video) | https://developer.apple.com/videos/play/wwdc2025/219/ |
| Build a SwiftUI app with the new design | https://developer.apple.com/videos/play/wwdc2025/323/ |
| Build a UIKit app with the new design | https://developer.apple.com/videos/play/wwdc2025/284/ |
| Liquid Glass Documentation | https://developer.apple.com/documentation/TechnologyOverviews/liquid-glass |
| Adopting Liquid Glass Guide | https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass |
| Applying Liquid Glass to custom views | https://developer.apple.com/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views |

### Human Interface Guidelines

| Topic | URL |
|-------|-----|
| Materials | https://developer.apple.com/design/human-interface-guidelines/materials |
| Design Gallery | https://developer.apple.com/design/new-design-gallery/ |
| What's New in iOS | https://developer.apple.com/ios/whats-new/ |

### Apple Newsroom

| Announcement | URL |
|--------------|-----|
| New Software Design | https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/ |
| iOS 26 Announcement | https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/ |
| Developer Tools | https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/ |

### Community Resources

| Resource | URL |
|----------|-----|
| Liquid Glass Reference (GitHub) | https://github.com/conorluddy/LiquidGlassReference |
| LiquidGlassSwiftUI Sample | https://github.com/mertozseven/LiquidGlassSwiftUI |
| LiquidGlassCheatsheet | https://github.com/GonzaloFuentes28/LiquidGlassCheatsheet |

---

## Quick Reference

### Where to Use Liquid Glass

| DO Use | DON'T Use |
|--------|-----------|
| Navigation bars and toolbars | Content layer (lists, tables) |
| Tab bars and bottom accessories | Full-screen backgrounds |
| Floating action buttons | Scrollable content |
| Sheets, popovers, menus | Stacked glass on glass |
| Context-sensitive controls | Every UI element |
| System-level alerts | |
| Dock and home screen elements | |

### Common SwiftUI Patterns

```swift
// Basic glass button
Button("Action") { }
    .buttonStyle(.glass)

// Custom glass view
RoundedRectangle(cornerRadius: 16)
    .glassEffect(.regular)
    .frame(height: 100)

// Interactive tinted glass
Circle()
    .glassEffect(.regular.tint(.blue).interactive())

// Grouped glass elements
GlassEffectContainer {
    // Multiple glass views
}
```

### Automatic Adoption

- System components automatically adopt Liquid Glass when recompiled with iOS 26 SDK
- No redesign required for basic adoption
- iOS 27 will remove option to retain current designs

---

## Design Philosophy Summary

Liquid Glass is designed for **navigation and control layers** that float above content:

1. **Content remains primary** - Glass elevates controls, not content
2. **Controls provide functional overlay** - Clear hierarchy between content and UI
3. **Depth creates context** - Visual weight indicates importance
4. **Adaptivity ensures legibility** - System handles contrast automatically
5. **Motion conveys physicality** - Animations feel natural and responsive
