"""
sample/app.py — Minimal Dash app demonstrating dash_dracula.

Run:
    pip install "dash-dracula-theme[pdf]" dash-bootstrap-components
    python sample/app.py

Then open http://127.0.0.1:8050
"""
import dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dcc, html

import dash_dracula as dr

# 1. Create the app with Bootstrap DARKLY as the base stylesheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], title="Dracula Dash Demo")

# 2. Wire the Dracula theme
#    apply_theme() copies dracula.css into assets/, registers the toggle
#    clientside_callback, and returns a dcc.Store for the layout.
theme_store = dr.apply_theme(app)

# 3. Build a simple figure using the Dracula Plotly template
fig = go.Figure(
    data=[
        go.Scatter(y=[4, 1, 3, 5, 2], name="Cyan trace",   line_color=dr.CYAN),
        go.Scatter(y=[2, 4, 1, 4, 3], name="Purple trace", line_color=dr.PURPLE),
        go.Scatter(y=[1, 3, 4, 2, 5], name="Green trace",  line_color=dr.GREEN),
    ],
    layout=dict(
        template="dracula",
        title="Dracula Theme Demo",
    ),
)

# 4. Layout — include the theme_store and the toggle button
app.layout = dbc.Container(
    [
        theme_store,
        dbc.Row(
            dbc.Col(
                [
                    html.H1("Dracula Dash", className="text-primary mt-4"),
                    dr.theme_toggle_button(),
                ],
                width=12,
            )
        ),
        dbc.Row(
            dbc.Col(dcc.Graph(figure=fig, id="demo-graph"), width=12)
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Colour palette", className="card-title"),
                            html.P(
                                f"BACKGROUND={dr.BACKGROUND}  CYAN={dr.CYAN}  "
                                f"PURPLE={dr.PURPLE}  GREEN={dr.GREEN}",
                                className="font-monospace",
                            ),
                        ]
                    )
                ),
                width=12,
                className="mt-3",
            )
        ),
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run(debug=True, port=8051)
