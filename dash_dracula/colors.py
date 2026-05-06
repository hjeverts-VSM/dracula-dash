"""
dash_dracula.colors
~~~~~~~~~~~~~~~~~~~
Official Dracula colour palette constants.
Source: https://draculatheme.com/contribute

All hex values are lowercase to match CSS convention.
"""

# ── Official Dracula Classic palette (dark) ──────────────────────────────────
# https://draculatheme.com/contribute  /  https://draculatheme.com/spec
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

# ── Official Alucard Classic palette (light) ─────────────────────────────────
# https://draculatheme.com/spec  — complementary light theme
AL_BACKGROUND   = "#fffbeb"   # main background (warm off-white)
AL_CURRENT_LINE = "#6c664b"   # current-line / comment (dark gold)
AL_SELECTION    = "#cfcfde"   # text selection (light lavender-grey)
AL_FOREGROUND   = "#1f1f1f"   # default text (near-black)
AL_COMMENT      = "#6c664b"   # comments / secondary UI text

# Alucard accent colours (darkened for readability on light bg)
AL_RED    = "#cb3a2a"
AL_ORANGE = "#a34d14"
AL_YELLOW = "#846e15"
AL_GREEN  = "#14710a"
AL_CYAN   = "#036a96"
AL_PURPLE = "#644ac9"
AL_PINK   = "#a3144d"

# Alucard UI surface colours (from the spec UI palette)
AL_SURFACE          = "#efeddc"   # floating interactive elements
AL_BG_LIGHTER       = "#ece9df"   # background lighter
AL_BG_LIGHT         = "#dedccf"   # background light / borders
AL_BG_DARK          = "#ceccc0"   # background dark / scrollbar thumb
AL_BG_DARKER        = "#bcbab3"   # background darker

# ── Plotly colorway (dark theme traces) ─────────────────────────────────────
# Order: most-distinct first so first few traces are always visually separated
COLORWAY = [CYAN, PURPLE, GREEN, ORANGE, PINK, RED, YELLOW]

# ── Alucard colorway (light theme traces) ────────────────────────────────────
ALUCARD_COLORWAY = [AL_CYAN, AL_PURPLE, AL_GREEN, AL_ORANGE, AL_PINK, AL_RED, AL_YELLOW]

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

# ── Light-mode UI colours — Alucard Classic palette ──────────────────────────
# CSS `body.light-theme` overrides use these values.
LIGHT_COLORS = {
    "background":   AL_BACKGROUND,    # #fffbeb
    "surface":      AL_SURFACE,       # #efeddc
    "foreground":   AL_FOREGROUND,    # #1f1f1f
    "comment":      AL_COMMENT,       # #6c664b
    "cyan":         AL_CYAN,          # #036a96
    "green":        AL_GREEN,         # #14710a
    "orange":       AL_ORANGE,        # #a34d14
    "pink":         AL_PINK,          # #a3144d
    "purple":       AL_PURPLE,        # #644ac9
    "red":          AL_RED,           # #cb3a2a
    "yellow":       AL_YELLOW,        # #846e15
    "border":       AL_BG_LIGHT,      # #dedccf
    "axis_line":    AL_BG_DARK,       # #ceccc0
    "tick_font":    AL_COMMENT,       # #6c664b
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
