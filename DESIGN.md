# Design System: Risale AI Studio

## 🎨 Visual Identity
**Risale AI Studio** is a premium, academic-grade digital library designed for deep study of the Risale-i Nur collection. The design prioritizes legibility, historical reverence, and modern AI integration.

### Core Principles
- **Academic Precision:** Clean layouts, focused on long-form reading.
- **Anti-Slop Aesthetic:** High-end design that avoids generic "AI-generated" looks.
- **Bilingual Harmony:** Balanced presentation of Turkish/Russian/Arabic texts.
- **Reverence:** Neutral tones with gold/brand accents to respect the theological nature of the content.

---

## 🖋️ Typography
The typography system uses specialized fonts for different scripts to ensure maximum readability and cultural correctness.

- **Primary Serif (Body):** `Minion Pro` (Premium academic serif)
- **Primary Sans (UI):** `Inter` (Variable font for clarity)
- **Arabic/Ottoman:** `Nassim Arabic Pro` (Modern, readable Naskh style)
- **Cyrillic (Russian):** `Kazimir Text` (Distinctive, literary serif)
- **Fallback:** `ITC Souvenir` (Warm, approachable serif)

### Type Scale
- **Display:** 32px / 1.2 line-height (Titles)
- **H1:** 24px / 1.3 line-height
- **Body:** 18.4px / 1.6 line-height (Default reading size)
- **Caption:** 14px / 1.4 line-height

---

## 🌈 Color Palette
Based on custom DaisyUI themes with Light and Dark variants.

### Base Colors
- **Primary:** Gold/Brass accents (`#C5A059`) for highlights and active states.
- **Background:** 
  - Light: Soft cream (`#F8F5F0`) or Paper-like textures.
  - Dark: Deep Charcoal (`#1A1A1A`) or Midnight Blue.
- **Surface:** Slight variations of the background (`base-200`, `base-300`) for cards and menus.

---

## 🏗️ Components & Patterns

### 1. Window System (Tauri)
- **Rounded Corners:** 10px radius on all windows.
- **Window Border:** Subtle 1px border (`base-300`) to define the app boundary.
- **Shadows:** Soft, deep shadows for modals and dropdowns.

### 2. Reading Experience
- **Hasiye (Footnotes):** Golden dotted underline (`border-dotted border-b-2 border-primary/50`).
- **Meaning Mode:** Green dashed underline for terms with instant dictionary lookups.
- **Atmosphere Overlay:** Subtle grain/texture overlay to simulate high-quality paper.

### 3. Navigation
- **Bookshelf:** Grid or List view with premium book spine 3D effects.
- **Reader Menu:** Floating "Hover Bars" that appear on interaction to minimize distraction.

---

## 🛠️ Technical Stack
- **Framework:** Next.js 16 (Turbopack)
- **Styling:** TailwindCSS + DaisyUI
- **Icons:** Lucide React
- **Animations:** View Transitions API (Forward/Back navigation)
