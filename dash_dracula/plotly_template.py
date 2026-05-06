"""
dash_dracula.plotly_template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Registers Plotly layout templates:

* ``pio.templates["dracula"]``  — dark theme (Dracula Classic)
* ``pio.templates["alucard"]``  — light theme (Alucard Classic)

Call ``register()`` (or simply ``import dash_dracula``) before creating any
Plotly figures so that ``template="dracula"`` / ``template="alucard"`` are
available everywhere.
"""
import plotly.graph_objects as go
import plotly.io as pio

from .colors import (
    BACKGROUND, CURRENT_LINE, FOREGROUND, COMMENT, COLORWAY,
    AL_BACKGROUND, AL_CURRENT_LINE, AL_SELECTION, AL_FOREGROUND,
    AL_COMMENT, AL_BG_LIGHT, AL_BG_DARK, ALUCARD_COLORWAY,
)

TEMPLATE_NAME         = "dracula"
TEMPLATE_NAME_ALUCARD = "alucard"

_AXIS_STYLE = dict(
    gridcolor=CURRENT_LINE,
    zerolinecolor=COMMENT,
    linecolor=COMMENT,
    tickcolor=COMMENT,
)

_AXIS_STYLE_ALUCARD = dict(
    gridcolor=AL_SELECTION,   # #cfcfde — light lavender-grey grid
    zerolinecolor=AL_BG_DARK, # #ceccc0
    linecolor=AL_BG_DARK,
    tickcolor=AL_BG_DARK,
    tickfont=dict(color=AL_COMMENT),
    title=dict(font=dict(color=AL_FOREGROUND)),
)


def register() -> None:
    """Register ``pio.templates["dracula"]`` and ``pio.templates["alucard"]``.
    Safe to call multiple times."""
    if TEMPLATE_NAME not in pio.templates:
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
    if TEMPLATE_NAME_ALUCARD not in pio.templates:
        pio.templates[TEMPLATE_NAME_ALUCARD] = go.layout.Template(
            layout=go.Layout(
                paper_bgcolor=AL_BACKGROUND,
                plot_bgcolor=AL_BACKGROUND,
                font=dict(color=AL_FOREGROUND),
                colorway=ALUCARD_COLORWAY,
                xaxis=_AXIS_STYLE_ALUCARD,
                yaxis=_AXIS_STYLE_ALUCARD,
                legend=dict(
                    bgcolor=AL_BG_LIGHT,
                    bordercolor=AL_BG_DARK,
                    font=dict(color=AL_FOREGROUND),
                ),
                title=dict(font=dict(color=AL_FOREGROUND)),
            )
        )


def unregister() -> None:
    """Remove both templates from the registry (useful for testing)."""
    pio.templates.pop(TEMPLATE_NAME, None)
    pio.templates.pop(TEMPLATE_NAME_ALUCARD, None)
