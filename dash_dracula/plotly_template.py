"""
dash_dracula.plotly_template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Registers ``pio.templates["dracula"]`` — a Plotly layout template using the
official Dracula colour palette.

Call ``register()`` (or simply ``import dash_dracula``) before creating any
Plotly figures so that ``template="dracula"`` is available everywhere.
"""
import plotly.graph_objects as go
import plotly.io as pio

from .colors import (
    BACKGROUND, CURRENT_LINE, FOREGROUND, COMMENT, COLORWAY,
)

TEMPLATE_NAME = "dracula"

_AXIS_STYLE = dict(
    gridcolor=CURRENT_LINE,
    zerolinecolor=COMMENT,
    linecolor=COMMENT,
    tickcolor=COMMENT,
)


def register() -> None:
    """Register ``pio.templates["dracula"]``.  Safe to call multiple times."""
    if TEMPLATE_NAME in pio.templates:
        return
    pio.templates[TEMPLATE_NAME] = go.layout.Template(
        layout=go.Layout(
            paper_bgcolor=BACKGROUND,
            plot_bgcolor=BACKGROUND,
            font=dict(color=FOREGROUND),
            colorway=COLORWAY,
            xaxis=_AXIS_STYLE,
            yaxis=_AXIS_STYLE,
            legend=dict(bgcolor=CURRENT_LINE, bordercolor=COMMENT),
            title=dict(font=dict(color=FOREGROUND)),
        )
    )


def unregister() -> None:
    """Remove the template from the registry (useful for testing)."""
    pio.templates.pop(TEMPLATE_NAME, None)
