# Install

## pip (recommended)

```bash
pip install dash-dracula-theme
```

Or, for local / editable install (e.g. during development alongside your Dash app):

```bash
pip install -e /path/to/dracula-dash
```

Or relative to a sibling project:

```bash
pip install -e ../dracula-dash
```

## Requirements

| Package | Minimum version |
|---|---|
| Python | 3.9+ |
| dash | 4.0+ |
| plotly | 5.0+ |
| dash-bootstrap-components | 2.0+ |

> **Note:** Your Dash app must include `dbc.themes.DARKLY` in `external_stylesheets`.
> The Dracula CSS variables build on top of Bootstrap DARKLY's CSS variable layer.

### Optional — PDF export

To use `fig_to_print_image()` you also need:

| Package | Minimum version |
|---|---|
| reportlab | 4.0+ |
| kaleido | 0.2+ |

Install with the `pdf` extra:

```bash
pip install "dash-dracula-theme[pdf]"
```

## Usage

See [README.md](README.md) for a quick-start example and [sample/app.py](sample/app.py)
for a complete minimal Dash application.
