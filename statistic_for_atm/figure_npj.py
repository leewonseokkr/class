"""Shared Matplotlib settings for q1q2.ipynb and q3.ipynb."""

import matplotlib as mpl


HAD_BLUE = "#2166AC"
OISST_RED = "#B2182B"
TREND_GRAY = "#666666"
OBSERVED_BLACK = "#222222"
PAPER_WIDTH_MM = 180
PNG_DPI = 300


def apply_npj():
    """Apply the figure settings that were previously written as rc file entries."""
    mpl.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.labelsize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "axes.linewidth": 0.65,
        "xtick.major.width": 0.65,
        "ytick.major.width": 0.65,
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "savefig.dpi": PNG_DPI,
        "axes.unicode_minus": True,
    })


def closed_frame(ax):
    """Draw a thin frame around all four sides of an axes."""
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(mpl.rcParams["axes.linewidth"])
    return ax
