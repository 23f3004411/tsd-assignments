import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- 1. Define Image Dimensions ---
pixels_x = 512
pixels_y = 512
dpi = 100 # Dots Per Inch

# Calculate the figure size in inches
figsize_x = pixels_x / dpi
figsize_y = pixels_y / dpi

# --- 2. Generate Sample Data ---
# Create a sample DataFrame for plotting
np.random.seed(42) # For reproducible results
data = {
    'temperature': np.random.normal(25, 5, 100),
    'humidity': np.random.normal(60, 10, 100),
    'season': np.random.choice(['Spring', 'Summer', 'Autumn', 'Winter'], 100)
}
df = pd.DataFrame(data)

# --- 3. Create and Configure the Plot ---
# Create a figure with the specified size and DPI
fig, ax = plt.subplots(figsize=(figsize_x, figsize_y), dpi=dpi)

# Generate the Seaborn plot on the created axes
sns.scatterplot(
    data=df,
    x='temperature',
    y='humidity',
    hue='season',
    ax=ax # IMPORTANT: Specify the axes to draw on
)

# Add titles and labels for context
ax.set_title(f'Seaborn Chart ({pixels_x}x{pixels_y}px)')
ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Humidity (%)')

# Ensure all elements fit within the figure cleanly
plt.tight_layout()

# --- 4. Save the Chart to a File ---
output_filename = 'seaborn_chart_512x512.png'
plt.savefig(output_filename)

print(f"✅ Successfully generated and saved chart as '{output_filename}'")

# To display the plot in a window (optional), uncomment the line below
# plt.show()