"""
dash_dracula.bootstrap
~~~~~~~~~~~~~~~~~~~~~~~
Helpers to wire the Dracula theme into any Dash application:

* ``apply_theme(app, default_theme="dark")``
  Copies ``dracula.css`` into the app's ``assets/`` folder, registers the
  Plotly-graph theme-toggle ``clientside_callback`` on the app, and returns
  a ``dcc.Store`` component that must be added to the layout.

* ``theme_toggle_button()``
  Returns a pre-configured ``dbc.Button`` that drives the toggle.

Usage::

    import dash
    import dash_bootstrap_components as dbc
    import dash_dracula as dr

    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
    theme_store = dr.apply_theme(app)   # add theme_store to your layout

    # Somewhere in your layout:
    layout = dbc.Container([
        dr.theme_toggle_button(),
        theme_store,
        ...
    ])
"""
import os
import shutil

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc

# ── JS payload ───────────────────────────────────────────────────────────────
# Extracted verbatim from app.py — kept in one place so both the original app
# and any new app share exactly the same toggle logic.
_TOGGLE_JS = """
function(n_clicks, current_theme) {
    if (!n_clicks) {
        return [window.dash_clientside.no_update, window.dash_clientside.no_update];
    }
    var new_theme = (current_theme === 'dark') ? 'light' : 'dark';
    var is_light  = (new_theme === 'light');

    // Toggle CSS class on <body> — the light-theme CSS block handles the rest
    document.body.classList.toggle('light-theme', is_light);

    // Plotly graph layout overrides
    var layout_light = {
        paper_bgcolor: '#fffbeb',
        plot_bgcolor:  '#fffbeb',
        'font.color':  '#1f1f1f',
        'title.font.color': '#1f1f1f',
        'xaxis.gridcolor':    '#cfcfde',
        'xaxis.linecolor':    '#ceccc0',
        'xaxis.tickcolor':    '#ceccc0',
        'xaxis.tickfont.color': '#6c664b',
        'xaxis.title.font.color': '#1f1f1f',
        'yaxis.gridcolor':    '#cfcfde',
        'yaxis.linecolor':    '#ceccc0',
        'yaxis.tickcolor':    '#ceccc0',
        'yaxis.tickfont.color': '#6c664b',
        'yaxis.title.font.color': '#1f1f1f',
        'legend.bgcolor':     '#efeddc',
        'legend.bordercolor': '#dedccf',
        'legend.font.color':  '#1f1f1f',
        'coloraxis.colorbar.tickfont.color': '#1f1f1f',
        'coloraxis.colorbar.title.font.color': '#1f1f1f',
        'scene.bgcolor':      '#fffbeb',
        'scene.xaxis.backgroundcolor': '#efeddc',
        'scene.yaxis.backgroundcolor': '#efeddc',
        'scene.zaxis.backgroundcolor': '#efeddc',
        'scene.xaxis.gridcolor': '#cfcfde',
        'scene.yaxis.gridcolor': '#cfcfde',
        'scene.zaxis.gridcolor': '#cfcfde',
        'scene.xaxis.linecolor': '#ceccc0',
        'scene.yaxis.linecolor': '#ceccc0',
        'scene.zaxis.linecolor': '#ceccc0',
        'scene.xaxis.tickfont.color':       '#6c664b',
        'scene.yaxis.tickfont.color':       '#6c664b',
        'scene.zaxis.tickfont.color':       '#6c664b',
        'scene.xaxis.title.font.color':     '#1f1f1f',
        'scene.yaxis.title.font.color':     '#1f1f1f',
        'scene.zaxis.title.font.color':     '#1f1f1f'
    };
    var layout_dark = {
        paper_bgcolor: '#282a36',
        plot_bgcolor:  '#282a36',
        'font.color':  '#f8f8f2',
        'title.font.color': '#f8f8f2',
        'xaxis.gridcolor':    '#44475a',
        'xaxis.linecolor':    '#6272a4',
        'xaxis.tickcolor':    '#6272a4',
        'xaxis.tickfont.color': '#f8f8f2',
        'xaxis.title.font.color': '#f8f8f2',
        'yaxis.gridcolor':    '#44475a',
        'yaxis.linecolor':    '#6272a4',
        'yaxis.tickcolor':    '#6272a4',
        'yaxis.tickfont.color': '#f8f8f2',
        'yaxis.title.font.color': '#f8f8f2',
        'legend.bgcolor':     '#44475a',
        'legend.bordercolor': '#6272a4',
        'legend.font.color':  '#f8f8f2',
        'coloraxis.colorbar.tickfont.color': '#f8f8f2',
        'coloraxis.colorbar.title.font.color': '#f8f8f2',
        'scene.bgcolor':      '#282a36',
        'scene.xaxis.backgroundcolor': '#282a36',
        'scene.yaxis.backgroundcolor': '#282a36',
        'scene.zaxis.backgroundcolor': '#282a36',
        'scene.xaxis.gridcolor': '#44475a',
        'scene.yaxis.gridcolor': '#44475a',
        'scene.zaxis.gridcolor': '#44475a',
        'scene.xaxis.linecolor': '#6272a4',
        'scene.yaxis.linecolor': '#6272a4',
        'scene.zaxis.linecolor': '#6272a4',
        'scene.xaxis.tickfont.color':       '#f8f8f2',
        'scene.yaxis.tickfont.color':       '#f8f8f2',
        'scene.zaxis.tickfont.color':       '#f8f8f2',
        'scene.xaxis.title.font.color':     '#f8f8f2',
        'scene.yaxis.title.font.color':     '#f8f8f2',
        'scene.zaxis.title.font.color':     '#f8f8f2'
    };
    var patch = is_light ? layout_light : layout_dark;

    document.querySelectorAll('.js-plotly-plot').forEach(function(el) {
        try { Plotly.relayout(el, patch); } catch(e) {}
    });

    return [new_theme, is_light ? '\\u{1F319} Donker' : '\\u2600\\uFE0F Licht'];
}
"""


def _assets_src() -> str:
    """Absolute path to the ``assets/`` folder inside this package."""
    return os.path.join(os.path.dirname(__file__), "assets")


def _ensure_css_in_app(app: dash.Dash) -> None:
    """Copy ``dracula.css`` into the app's assets folder if not already there.

    Dash 4 auto-serves exactly one ``assets/`` folder per app.  The simplest
    portable approach is to copy the CSS there at startup.
    """
    src = os.path.join(_assets_src(), "dracula.css")
    # Resolve the app's assets directory
    try:
        assets_folder = os.path.abspath(app.config.assets_folder)
    except AttributeError:
        assets_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

    os.makedirs(assets_folder, exist_ok=True)
    dest = os.path.join(assets_folder, "dracula.css")
    if not os.path.exists(dest):
        shutil.copy(src, dest)


def theme_toggle_button() -> dbc.Button:
    """Return the pre-configured dark/light toggle button.

    The button's ``id`` must be ``"theme-toggle-btn"`` — the clientside
    callback registered by :func:`apply_theme` listens for clicks on that id.
    """
    return dbc.Button(
        "☀️ Licht",
        id="theme-toggle-btn",
        color="secondary",
        outline=True,
        size="sm",
    )


def apply_theme(
    app: dash.Dash,
    default_theme: str = "dark",
) -> dcc.Store:
    """Wire the Dracula theme into a Dash application.

    1. Copies ``dracula.css`` into the app's ``assets/`` folder so Dash
       serves it automatically.
    2. Registers a ``clientside_callback`` on the app that toggles
       ``body.light-theme`` and re-colours all Plotly graphs when the
       ``#theme-toggle-btn`` button is clicked.

    Parameters
    ----------
    app:
        The ``dash.Dash`` instance to configure.
    default_theme:
        Either ``"dark"`` (default) or ``"light"``.

    Returns
    -------
    dcc.Store
        A hidden store component with ``id="theme-store"`` that **must** be
        added to the app layout.  It persists the current theme value so the
        callback always has access to it.

    Example
    -------
    ::

        app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
        theme_store = apply_theme(app)

        app.layout = dbc.Container([
            theme_toggle_button(),
            theme_store,
            ...
        ])
    """
    _ensure_css_in_app(app)

    app.clientside_callback(
        _TOGGLE_JS,
        Output("theme-store", "data"),
        Output("theme-toggle-btn", "children"),
        Input("theme-toggle-btn", "n_clicks"),
        State("theme-store", "data"),
        prevent_initial_call=True,
    )

    return dcc.Store(id="theme-store", data=default_theme)
