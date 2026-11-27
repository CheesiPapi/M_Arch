from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

# gathering the file name and the sheet name from the excel file ---------------
excelFileData = "error_function_data&graph/nearLaserCutData.xlsx"
sheet = "nearLaserCutData"

# These are the columns that the data I want are in.  --------------------------
xColumn = "Distance"
yColumn = "Light Intensity"

# we are gunna smooth those data points to get a better curve -----------------
SMOOTH = True
SMOOTH_WINDOW = 51                     # must be odd; bigger = smoother
SMOOTH_POLYORDER = 3

# Labels ----------------------------------------------------------------------
TITLE = "Intensity and its Derivative vs. Distance"
X_LABEL = "Distance"
Y_LABEL = "Intensity"
DERIV_LABEL = "Derivative"
GAUSS_LABEL = "Gaussian"

# --- Colors ------------------------------------------------------------------
INTENSITY_COLOR = "#1f77b4"            # blue
DERIV_COLOR = "#ff7f0e"                # orange
GAUSS_COLOR = "#CC0000"                # red
RAW_POINT_COLOR = "#9aa5b1"            # grey dots for the raw data
FIG_BACKGROUND = "white"

# --- Lines and markers -------------------------------------------------------
INTENSITY_LINEWIDTH = 2.5
DERIV_LINEWIDTH = 2.5
DERIV_LINESTYLE = "--"                 # "-", "--", ":", "-."
GAUSS_LINEWIDTH = 2.5
GAUSS_LINESTYLE = ":"
SHOW_RAW_POINTS = True                 # faint dots showing the unsmoothed data
RAW_POINT_SIZE = 18
RAW_POINT_ALPHA = 0.6
MARK_DERIV_PEAK = True                 # dot + label at the derivative's maximum

# Text and layout -------------------------------------------------------------
FIG_SIZE = (10, 6)
TITLE_SIZE = 15
LABEL_SIZE = 12
TICK_SIZE = 10
LEGEND_LOC = "center left"
SHOW_GRID = True
GRID_ALPHA = 0.35
STYLE = "seaborn-v0_8-whitegrid"       # any matplotlib style, or None

# Output -----------------------------------------------------------------------
SAVE_FIGURE = True
OUTPUT_FILE = "intensity_and_derivative.png"
DPI = 300
SHOW_PLOT = True

# These are the lists that will be filled with our data points for our gaussian distribution plot
x_gauss = []
y_gauss = []

# To get a proper gaussian distribution the formula below in the for loop was used 
sigma = 25
mu = 56

# The for loop that generates the points of the gaussian distribution curve
for i in range(0, 151, 3):
    x_gauss.append(i)
    yFormula = (6275/((sigma)*np.sqrt(2*np.pi))) * np.exp((-0.5)*((i-mu)/(sigma))**2)
    y_gauss.append(yFormula)

# Loading the excel data -----------------------------------------------------------------------
dataDir = Path(__file__).resolve().parent
excelPath = Path(excelFileData)
if not excelPath.is_absolute():
    excelPath = dataDir / excelPath

# Reading the data from the excel file and prepping them to be placed in their lists
df = pd.read_excel(excelPath, sheet_name=sheet)
df.columns = df.columns.astype(str).str.strip()

# The excel files are getting their data points now
for col in (xColumn, yColumn):
    if col not in df.columns:
        raise KeyError(f"Column '{col}' not found. Available columns: {list(df.columns)}")

df = df[[xColumn, yColumn]].apply(pd.to_numeric, errors="coerce").dropna()
df = df.sort_values(xColumn).drop_duplicates(subset=xColumn)

# this tells numpy about the data points from the excel file and I think converts the lists to arrays
xData = df[xColumn].to_numpy()
yData = df[yColumn].to_numpy()

# smooth, then differentiate -------------------------------------------------------------
if SMOOTH:
    window = min(SMOOTH_WINDOW, len(yData))
    if window % 2 == 0:
        window -= 1
    if window <= SMOOTH_POLYORDER:
        raise ValueError(f"Only {len(yData)} data points; not enough to smooth. Set SMOOTH = False.")
    y_plot = savgol_filter(yData, window_length=window, polyorder=SMOOTH_POLYORDER)
else:
    y_plot = yData

derivative = np.gradient(y_plot, xData) * -1

# plotting -----------------------------------------------------------------------------------

if STYLE:
    try:
        plt.style.use(STYLE)
    except OSError:
        pass  # fall back to matplotlib defaults

fig, ax1 = plt.subplots(figsize=FIG_SIZE, facecolor=FIG_BACKGROUND)

# Left axis: intensity (the Gaussian shares this axis)
ax1.set_xlabel(X_LABEL, fontsize=LABEL_SIZE, fontweight="bold")
ax1.set_ylabel(Y_LABEL, color=INTENSITY_COLOR, fontsize=LABEL_SIZE, fontweight="bold")

handles = []

if SHOW_RAW_POINTS:
    handles.append(ax1.scatter(xData, yData, s=RAW_POINT_SIZE, color=RAW_POINT_COLOR,
                               alpha=RAW_POINT_ALPHA, label="Raw data", zorder=2))

handles += ax1.plot(xData, y_plot, color=INTENSITY_COLOR, linewidth=INTENSITY_LINEWIDTH,
                    label=Y_LABEL + (" (smoothed)" if SMOOTH else ""), zorder=3)
handles += ax1.plot(x_gauss, y_gauss, color=GAUSS_COLOR, linewidth=GAUSS_LINEWIDTH,
                    linestyle=GAUSS_LINESTYLE, label=GAUSS_LABEL, zorder=3)
ax1.tick_params(axis="y", labelcolor=INTENSITY_COLOR, labelsize=TICK_SIZE)
ax1.tick_params(axis="x", labelsize=TICK_SIZE)

# Right axis: derivative
ax2 = ax1.twinx()
ax2.set_ylabel(DERIV_LABEL, color=DERIV_COLOR, fontsize=LABEL_SIZE, fontweight="bold", loc="center")
handles += ax2.plot(xData, derivative, color=DERIV_COLOR, linewidth=DERIV_LINEWIDTH,
                    linestyle=DERIV_LINESTYLE, label=DERIV_LABEL, zorder=3)
ax2.tick_params(axis="y", labelcolor=DERIV_COLOR, labelsize=TICK_SIZE)
ax2.grid(False)  # avoid a second, misaligned grid

# One legend covering all curves (both axes)
ax1.legend(handles=handles, loc="upper right")

if SHOW_PLOT:
    plt.show()

print(x_gauss, y_gauss) # gauss
print()
print(derivative) # derivative
print()
print(xData, yData) # raw
print()
print(xData, y_plot) # smoothed