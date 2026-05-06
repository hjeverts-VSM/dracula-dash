"""
dash_dracula.colors
~~~~~~~~~~~~~~~~~~~
Official Dracula colour palette constants.
Source: https://draculatheme.com/contribute

All hex values are lowercase to match CSS convention.
"""

# ── Official Dracula palette ─────────────────────────────────────────────────
# https://draculatheme.com/contribute
BACKGROUND   = "#282a36"   # main background
CURRENT_LINE = "#44475a"   # current-line / selection highlight
SELECTION    = "#44475a"   # alias for CURRENT_LINE
FOREGROUND   = "#f8f8f2"   # default text
COMMENT      = "#6272a4"   # comments / secondary UI text

# Accent colours
RED    = "#ff5555"
ORANGE = "#ffb86c"
YELLOW = "#f1fa8c"
GREEN  = "#50fa7b"
CYAN   = "#8be9fd"
PURPLE = "#bd93f9"
PINK   = "#ff79c6"

# ── Plotly colorway (dark theme traces) ─────────────────────────────────────
# Order: most-distinct first so first few traces are always visually separated
COLORWAY = [CYAN, PURPLE, GREEN, ORANGE, PINK, RED, YELLOW]

# ── Neutral colorway (readable on both dark AND light backgrounds) ───────────
# Use these for data traces when your app supports a light-mode toggle.
NEUTRAL_COLORWAY = [
    "#1f77b4",   # Plotly default blue    — readable on both backgrounds
    "#7b2fbe",   # mid-purple             — readable on both backgrounds
    "#2ca02c",   # medium green           — readable on both backgrounds
    "#e09b00",   # amber                  — readable on both backgrounds
    "#c0357a",   # dark pink              — readable on both backgrounds
    "#dc3545",   # Bootstrap danger red
    "#17becf",   # teal
]

# ── Print / PDF colours ──────────────────────────────────────────────────────
# Darkened Dracula variants — Dracula neon is unreadable on white paper.
PRINT_COLORS = {
    "background": "#ffffff",
    "surface":    "#e8e8e8",
    "foreground": "#000000",
    "cyan":       "#0055aa",
    "purple":     "#5533aa",
    "green":      "#006622",
    "orange":     "#cc5500",
    "grid":       "#999999",
    "alt_row":    "#f2f2f2",
    # figure internals
    "fig_dark":   "#111111",
    "fig_mid":    "#444444",
    "fig_grid":   "#dddddd",
    "fig_line":   "#999999",
}

# ── Light-mode UI colours (CSS `body.light-theme` overrides) ─────────────────
LIGHT_COLORS = {
    "background": "#f5f5f5",
    "surface":    "#ffffff",
    "foreground": "#212529",
    "comment":    "#6c757d",
    "cyan":       "#0066cc",
    "green":      "#198754",
    "orange":     "#e06c00",
    "pink":       "#c0357a",
    "purple":     "#6610f2",
    "red":        "#dc3545",
    "yellow":     "#b58900",
    "border":     "#dee2e6",
    "axis_line":  "#adb5bd",
    "tick_font":  "#495057",
}

# ── Convenience dict of all official palette colours ────────────────────────
AS_DICT = {
    "background":   BACKGROUND,
    "current_line": CURRENT_LINE,
    "selection":    SELECTION,
    "foreground":   FOREGROUND,
    "comment":      COMMENT,
    "red":          RED,
    "orange":       ORANGE,
    "yellow":       YELLOW,
    "green":        GREEN,
    "cyan":         CYAN,
    "purple":       PURPLE,
    "pink":         PINK,
}
