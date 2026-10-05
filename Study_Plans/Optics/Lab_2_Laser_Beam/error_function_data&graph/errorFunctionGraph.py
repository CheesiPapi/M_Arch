"""
Plot light intensity data from an Excel file together with its derivative.

Put this script in the same folder as the Excel file (or set EXCEL_FILE to a
full path). Everything you would want to tweak lives in the CONFIG section.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

# =============================================================================
# CONFIG - edit these to change the data source and the look of the graph
# =============================================================================

# --- Data --------------------------------------------------------------------
EXCEL_FILE = "lightMeasurementRazorCloseToSensor.xlsx"  # relative to this script, or a full path
SHEET = 0                              # sheet index or name
X_COLUMN = "Distance"                  # exact header text in your Excel file
Y_COLUMN = "Light Intensity Close"     # exact header text in your Excel file

# --- Smoothing (applied before taking the derivative) ------------------------
SMOOTH = True
SMOOTH_WINDOW = 21                     # must be odd; bigger = smoother
SMOOTH_POLYORDER = 3

# --- Labels ------------------------------------------------------------------
TITLE = "Intensity and its Derivative vs. Distance"
X_LABEL = "Distance"
Y_LABEL = "Intensity"
DERIV_LABEL = "Derivative"

# --- Colors ------------------------------------------------------------------
INTENSITY_COLOR = "#1f77b4"            # blue
DERIV_COLOR = "#ff7f0e"                # orange
RAW_POINT_COLOR = "#9aa5b1"            # grey dots for the raw data
FIG_BACKGROUND = "white"

# --- Lines and markers -------------------------------------------------------
INTENSITY_LINEWIDTH = 2.5
DERIV_LINEWIDTH = 2.5
DERIV_LINESTYLE = "--"                 # "-", "--", ":", "-."
SHOW_RAW_POINTS = True                 # faint dots showing the unsmoothed data
RAW_POINT_SIZE = 18
RAW_POINT_ALPHA = 0.6
MARK_DERIV_PEAK = True                 # dot + label at the derivative's maximum

# --- Text and layout ---------------------------------------------------------
FIG_SIZE = (10, 6)
TITLE_SIZE = 15
LABEL_SIZE = 12
TICK_SIZE = 10
LEGEND_LOC = "upper left"
SHOW_GRID = True
GRID_ALPHA = 0.35
STYLE = "seaborn-v0_8-whitegrid"       # any matplotlib style, or None

# --- Output ------------------------------------------------------------------
SAVE_FIGURE = True
OUTPUT_FILE = "intensity_and_derivative.png"
DPI = 300
SHOW_PLOT = True

# =============================================================================
# Load and clean the data
# =============================================================================
script_dir = Path(__file__).resolve().parent
excel_path = Path(EXCEL_FILE)
if not excel_path.is_absolute():
    excel_path = script_dir / excel_path

df = pd.read_excel(excel_path, sheet_name=SHEET)
df.columns = df.columns.astype(str).str.strip()

for col in (X_COLUMN, Y_COLUMN):
    if col not in df.columns:
        raise KeyError(f"Column '{col}' not found. Available columns: {list(df.columns)}")

df = df[[X_COLUMN, Y_COLUMN]].apply(pd.to_numeric, errors="coerce").dropna()
df = df.sort_values(X_COLUMN).drop_duplicates(subset=X_COLUMN)

x = df[X_COLUMN].to_numpy()
y = df[Y_COLUMN].to_numpy()

# =============================================================================
# Smooth, then differentiate
# =============================================================================
if SMOOTH:
    window = min(SMOOTH_WINDOW, len(y))
    if window % 2 == 0:
        window -= 1
    if window <= SMOOTH_POLYORDER:
        raise ValueError(f"Only {len(y)} data points; not enough to smooth. Set SMOOTH = False.")
    y_plot = savgol_filter(y, window_length=window, polyorder=SMOOTH_POLYORDER)
else:
    y_plot = y

derivative = np.gradient(y_plot, x)

# =============================================================================
# Plot
# =============================================================================
if STYLE:
    try:
        plt.style.use(STYLE)
    except OSError:
        pass  # fall back to matplotlib defaults

fig, ax1 = plt.subplots(figsize=FIG_SIZE, facecolor=FIG_BACKGROUND)

# Left axis: intensity
ax1.set_xlabel(X_LABEL, fontsize=LABEL_SIZE, fontweight="bold")
ax1.set_ylabel(Y_LABEL, color=INTENSITY_COLOR, fontsize=LABEL_SIZE, fontweight="bold")
handles = []

if SHOW_RAW_POINTS:
    handles.append(ax1.scatter(x, y, s=RAW_POINT_SIZE, color=RAW_POINT_COLOR,
                               alpha=RAW_POINT_ALPHA, label="Raw data", zorder=2))

handles += ax1.plot(x, y_plot, color=INTENSITY_COLOR, linewidth=INTENSITY_LINEWIDTH,
                    label=Y_LABEL + (" (smoothed)" if SMOOTH else ""), zorder=3)
ax1.tick_params(axis="y", labelcolor=INTENSITY_COLOR, labelsize=TICK_SIZE)
ax1.tick_params(axis="x", labelsize=TICK_SIZE)

# Right axis: derivative
ax2 = ax1.twinx()
ax2.set_ylabel(DERIV_LABEL, color=DERIV_COLOR, fontsize=LABEL_SIZE, fontweight="bold")
handles += ax2.plot(x, derivative, color=DERIV_COLOR, linewidth=DERIV_LINEWIDTH,
                    linestyle=DERIV_LINESTYLE, label=DERIV_LABEL, zorder=3)
ax2.tick_params(axis="y", labelcolor=DERIV_COLOR, labelsize=TICK_SIZE)
ax2.grid(False)  # avoid a second, misaligned grid

if MARK_DERIV_PEAK:
    i = int(np.argmax(np.abs(derivative)))
    ax2.plot(x[i], derivative[i], "o", color=DERIV_COLOR, markersize=8,
             markeredgecolor="white", markeredgewidth=1.5, zorder=4)
    ax2.annotate(f"peak at {x[i]:.3g}", xy=(x[i], derivative[i]),
                 xytext=(12, 10), textcoords="offset points",
                 color=DERIV_COLOR, fontsize=TICK_SIZE, fontweight="bold")

ax1.grid(SHOW_GRID, alpha=GRID_ALPHA)

ax1.legend(handles, [h.get_label() for h in handles], loc=LEGEND_LOC,
           frameon=True, shadow=True)
ax1.set_title(TITLE, fontsize=TITLE_SIZE, fontweight="bold", pad=15)

fig.tight_layout()

if SAVE_FIGURE:
    out_path = script_dir / OUTPUT_FILE
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"Saved figure to {out_path}")

if SHOW_PLOT:
    plt.show()