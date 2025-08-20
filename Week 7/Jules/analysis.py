import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Data Setup ---
# Quarterly equipment efficiency data for 2024
data = {
    'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
    'Efficiency_Rate': [74.53, 74.55, 78.25, 79.80]
}
df = pd.DataFrame(data)

# --- Constants ---
INDUSTRY_TARGET = 90
company_average = df['Efficiency_Rate'].mean()

# Verify the average for the report
print(f"Calculated Company Average Efficiency: {company_average:.2f}%") # Should be 76.78%

# --- Visualization 1: Quarterly Trend Analysis ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the quarterly efficiency trend line
sns.lineplot(
    x='Quarter',
    y='Efficiency_Rate',
    data=df,
    marker='o',
    markersize=8,
    color='royalblue',
    label='Quarterly Efficiency',
    ax=ax
)

# Add a horizontal line for the company's 2024 average
ax.axhline(
    y=company_average,
    color='darkorange',
    linestyle='--',
    label=f'2024 Average: {company_average:.2f}%'
)

# Formatting the plot
ax.set_title('Quarterly Equipment Efficiency Rate (2024)', fontsize=16, fontweight='bold')
ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Efficiency Rate (%)', fontsize=12)
ax.set_ylim(70, 95) # Set y-axis limits to better frame the data
ax.legend(fontsize=11)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('quarterly_trend.png')
print("Generated and saved 'quarterly_trend.png'")


# --- Visualization 2: Benchmark Comparison ---
fig, ax = plt.subplots(figsize=(8, 6))

# Data for the comparison bar chart
comparison_data = {
    'Metric': ['Company Average', 'Industry Target'],
    'Value': [company_average, INDUSTRY_TARGET]
}
comp_df = pd.DataFrame(comparison_data)

# Create the bar plot
bars = sns.barplot(
    x='Metric',
    y='Value',
    data=comp_df,
    palette=['firebrick', 'forestgreen'],
    ax=ax
)

# Add data labels on top of the bars for clarity
for bar in bars.patches:
    ax.annotate(f'{bar.get_height():.2f}%',
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha='center', va='center',
                size=12, xytext=(0, -15),
                textcoords='offset points', color='white', fontweight='bold')

# Formatting the plot
ax.set_title('Average Efficiency vs. Industry Target', fontsize=16, fontweight='bold')
ax.set_ylabel('Efficiency Rate (%)', fontsize=12)
ax.set_xlabel('')
ax.set_ylim(0, 100) # Set y-axis from 0 to 100 for proper context
plt.tight_layout()

# Save the plot as an image file
plt.savefig('benchmark_comparison.png')
print("Generated and saved 'benchmark_comparison.png'")