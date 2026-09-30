import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# 1. Load your data from the Excel file 
# make sure to put the r in front of the path name
# Replace 'your_data.xlsx' with your actual file name
df = pd.read_excel(r'M_Arch\Study_Plans\Optics\Lab_2_Laser_Beam\error_function_data&graph\lightMeasurementRazorCloseToSensor.xlsx')

# Replace 'Distance' and 'Intensity' with the exact column headers from your Excel file
distance = df['Distance'].values
intensity = df['Light Intensity Close'].values

# 1. Smooth the raw intensity data first
# window_length determines how aggressive the smoothing is (MUST be an odd number)
# polyorder is the polynomial curve fit (usually 2 or 3)
smoothed_intensity = savgol_filter(intensity, window_length=21, polyorder=3)

# 2. Take the derivative of the SMOOTHED data, not the raw data
derivative = np.gradient(smoothed_intensity, distance)

# 3. Set up the plot
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax1 = plt.subplots(figsize=(10, 6))

# 4. Plot Intensity (S-Curve) on the left Y-axis
color1 = '#1f77b4' # Blue
ax1.set_xlabel('Distance', fontsize=12, fontweight='bold')
ax1.set_ylabel('Intensity', color=color1, fontsize=12, fontweight='bold')
line1 = ax1.plot(distance, smoothed_intensity, color=color1, linewidth=2.5, label='Intensity')
ax1.tick_params(axis='y', labelcolor=color1)

# 5. Create a second Y-axis for the Derivative (Gaussian Peak)
ax2 = ax1.twinx()  
color2 = '#ff7f0e' # Orange
ax2.set_ylabel('Derivative', color=color2, fontsize=12, fontweight='bold')
line2 = ax2.plot(distance, derivative, color=color2, linewidth=2.5, linestyle='--', label='Derivative')
ax2.tick_params(axis='y', labelcolor=color2)

# 6. Combine legends and add a title
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=True, shadow=True)

plt.title('Intensity and its Derivative vs. Distance', fontsize=14, fontweight='bold', pad=15)
fig.tight_layout()

plt.show()

