# Dracula for [Dash](https://dash.plotly.com/)

> A dark theme for [Plotly Dash](https://dash.plotly.com/) — pip-installable Python package
> that gives any Dash application the full Dracula colour experience, including a light-mode
> toggle and always-light PDF export.

| Dark mode | Light mode |
|---|---|
| ![Dark mode](https://raw.githubusercontent.com/hjeverts-VSM/dracula-dash/master/screenshot_dark.png) | ![Light mode](https://raw.githubusercontent.com/hjeverts-VSM/dracula-dash/master/screenshot_light.png) |

## Install

All instructions can be found at [INSTALL.md](INSTALL.md).

## Features

- **Dark mode** — full Dracula palette applied via CSS variables and a custom Plotly template
- **Light mode toggle** — single button switches the entire dashboard; all Plotly graphs
  re-colour automatically via a clientside callback
- **PDF export** — `fig_to_print_image()` always produces print-ready figures on a white
  background, regardless of the current dashboard theme
- **Official palette** — all 11 Dracula colours exposed as named Python constants
  (`BACKGROUND`, `CYAN`, `PURPLE`, …)

## Quick start

```python
import dash
import dash_bootstrap_components as dbc
import dash_dracula as dr

# 1. Create the app with Bootstrap DARKLY as base
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# 2. Wire the Dracula theme (copies CSS, registers clientside toggle)
theme_store = dr.apply_theme(app)          # returns dcc.Store for the layout

# 3. Use Dracula colours and template in your figures
fig = go.Figure(layout=dict(template="dracula"))
fig.add_scatter(y=[1, 2, 3], line_color=dr.CYAN)

# 4. Export a figure to a print-ready ReportLab Image (always light)
from dash_dracula.pdf import fig_to_print_image
img = fig_to_print_image(fig, w_mm=170, h_mm=100)
```

See [sample/app.py](sample/app.py) for a complete minimal example.

## Team

This theme is maintained by the following person(s) and a bunch of
[awesome contributors](https://github.com/dracula/dash/graphs/contributors).

| [hjeverts](https://github.com/hjeverts) |
|---|

## Community

- [GitHub](https://github.com/dracula/dracula-theme/discussions) — Best for asking questions and discussing issues.
- [Discord](https://draculatheme.com/discord-invite) — Best for hanging out with the community.

## License

[MIT License](LICENSE)
