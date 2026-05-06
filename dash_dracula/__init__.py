"""
dash_dracula
~~~~~~~~~~~~
Dracula dark/light theme for Plotly Dash applications.

Quick start::

    import dash
    import dash_bootstrap_components as dbc
    import dash_dracula as dr

    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
    theme_store = dr.apply_theme(app)   # wire CSS + toggle callback

    # In your layout:
    #   dr.theme_toggle_button()  — the ☀️/🌙 button component
    #   theme_store               — dcc.Store that must be in the layout

    # In your figures:
    #   template="dracula"        — auto-registered on import
    #   line_color=dr.CYAN        — use palette constants directly

    # For PDF export (always light):
    #   from dash_dracula.pdf import fig_to_print_image
    #   img = fig_to_print_image(fig, w_mm=170, h_mm=100)
"""

# ── Auto-register the Plotly template on import ──────────────────────────────
from .plotly_template import register as _register, TEMPLATE_NAME

_register()

# ── Colour palette ───────────────────────────────────────────────────────────
from .colors import (
    BACKGROUND,
    CURRENT_LINE,
    SELECTION,
    FOREGROUND,
    COMMENT,
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    CYAN,
    PURPLE,
    PINK,
    COLORWAY,
    NEUTRAL_COLORWAY,
    PRINT_COLORS,
    LIGHT_COLORS,
    AS_DICT as PALETTE,
)

# ── Bootstrap / theme wiring ─────────────────────────────────────────────────
from .bootstrap import apply_theme, theme_toggle_button

# ── PDF utility (lazy — reportlab not required for basic theme usage) ─────────
from .pdf import fig_to_print_image

__all__ = [
    # Template
    "TEMPLATE_NAME",
    # Official palette
    "BACKGROUND", "CURRENT_LINE", "SELECTION", "FOREGROUND", "COMMENT",
    "RED", "ORANGE", "YELLOW", "GREEN", "CYAN", "PURPLE", "PINK",
    # Convenience collections
    "COLORWAY", "NEUTRAL_COLORWAY", "PRINT_COLORS", "LIGHT_COLORS", "PALETTE",
    # Bootstrap helpers
    "apply_theme", "theme_toggle_button",
    # PDF
    "fig_to_print_image",
]
