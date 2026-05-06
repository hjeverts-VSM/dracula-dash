"""
dash_dracula.pdf
~~~~~~~~~~~~~~~~~
Utility for rendering Plotly figures to print-ready ReportLab ``Image``
objects.  The output is **always light** (white background, dark text)
regardless of the current dashboard theme.

Requires the ``pdf`` extra::

    pip install "dash-dracula-theme[pdf]"
    # or: pip install reportlab kaleido

Usage::

    from dash_dracula.pdf import fig_to_print_image

    img = fig_to_print_image(my_figure, w_mm=170, h_mm=100)
    # img is a reportlab.platypus.Image ready to include in a PDF
"""


def fig_to_print_image(fig_dict_or_fig, w_mm: float = 170, h_mm: float = 100):
    """Render a Plotly figure to a ReportLab ``Image``, fully overridden for print.

    All Dracula dark-theme colours are stripped and replaced with a
    ``simple_white`` template on a white background with dark fonts.
    3-D figures receive additional ``scene.bgcolor`` and axis-backgroundcolor
    fixes that beat any baked-in template values.

    Parameters
    ----------
    fig_dict_or_fig:
        Either a Plotly ``go.Figure`` instance or a dict (e.g. from
        ``dcc.Graph.figure``).
    w_mm:
        Output width in millimetres.
    h_mm:
        Output height in millimetres.

    Returns
    -------
    reportlab.platypus.Image or None
        ``None`` if rendering fails or the input is ``None``.
    """
    if fig_dict_or_fig is None:
        return None
    try:
        import io

        import plotly.graph_objects as go
        import plotly.io as pio
        from reportlab.lib.units import mm
        from reportlab.platypus import Image

        fig_obj = (
            go.Figure(fig_dict_or_fig)
            if isinstance(fig_dict_or_fig, dict)
            else fig_dict_or_fig
        )

        DARK  = "#111111"
        MID   = "#444444"
        GRID  = "#dddddd"
        LINE  = "#999999"
        WHITE = "white"

        axis_style_2d = dict(
            title_font=dict(color=DARK, size=11),
            tickfont=dict(color=MID, size=9),
            linecolor=LINE,
            gridcolor=GRID,
            zerolinecolor=LINE,
        )
        axis_style_3d = dict(
            title_font=dict(color=DARK, size=10),
            tickfont=dict(color=MID, size=8),
            linecolor=LINE,
            gridcolor=GRID,
            backgroundcolor=WHITE,
        )

        is_3d = bool(
            fig_obj.data
            and any(
                (hasattr(t, "z") and hasattr(t, "surfacecolor"))
                or t.type in ("surface", "scatter3d", "mesh3d")
                for t in fig_obj.data
            )
        )

        common = dict(
            template="simple_white",
            paper_bgcolor=WHITE,
            font=dict(color=DARK, size=10),
            title_font=dict(color=DARK, size=13),
            legend=dict(
                font=dict(color=DARK),
                bgcolor=WHITE,
                bordercolor=LINE,
                borderwidth=1,
            ),
        )

        if is_3d:
            fig_obj.update_layout(
                **common,
                scene=dict(
                    bgcolor=WHITE,
                    xaxis=dict(**axis_style_3d),
                    yaxis=dict(**axis_style_3d),
                    zaxis=dict(**axis_style_3d),
                ),
                margin=dict(l=10, r=10, t=70, b=10),
            )
            # Direct attribute assignment beats any baked-in template values
            try:
                fig_obj.layout.template = None
                fig_obj.layout.scene.bgcolor = WHITE
                for _ax in (
                    fig_obj.layout.scene.xaxis,
                    fig_obj.layout.scene.yaxis,
                    fig_obj.layout.scene.zaxis,
                ):
                    _ax.backgroundcolor = WHITE
                    _ax.gridcolor = GRID
                    _ax.linecolor = LINE
            except Exception:
                pass
        else:
            fig_obj.update_layout(
                **common,
                plot_bgcolor=WHITE,
                xaxis=dict(**axis_style_2d),
                yaxis=dict(**axis_style_2d),
                margin=dict(l=75, r=20, t=60, b=70),
            )
            for ax in ["xaxis2", "xaxis3", "yaxis2", "yaxis3"]:
                if getattr(fig_obj.layout, ax, None):
                    fig_obj.update_layout(**{ax: axis_style_2d})

        # Fix colorbar and parcoords fonts
        for trace in fig_obj.data:
            if hasattr(trace, "colorbar") and trace.colorbar:
                trace.colorbar.tickfont = dict(color=DARK)
                if trace.colorbar.title:
                    trace.colorbar.title.font = dict(color=DARK)
            if hasattr(trace, "labelfont"):
                trace.labelfont = dict(color=DARK, size=10)
            if hasattr(trace, "tickfont") and trace.type == "parcoords":
                trace.tickfont = dict(color=MID, size=8)

        png = pio.to_image(
            fig_obj,
            format="png",
            width=int(w_mm * 3.78),
            height=int(h_mm * 3.78),
            scale=2,
        )
        return Image(io.BytesIO(png), width=w_mm * mm, height=h_mm * mm)
    except Exception:
        return None
