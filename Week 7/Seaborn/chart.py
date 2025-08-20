# chart.py
# Description: Generates a professional Seaborn lineplot of seasonal revenue patterns.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_revenue_data():
    """
    Generates a DataFrame with synthetic revenue data for two product lines.
    The data includes a base growth trend, a seasonal component, and random noise.
    """
    # Create a date range for three years (36 months)
    dates = pd.date_range(start='2022-01-01', end='2024-12-31', freq='M')
    n_points = len(dates)

    # 1. Base trend for overall growth
    base_growth_electronics = np.linspace(120, 200, n_points)
    base_growth_apparel = np.linspace(90, 160, n_points)

    # 2. Seasonal component (sine wave to simulate Q4 peaks)
    seasonal_component = 40 * np.sin(np.linspace(0, 3 * 2 * np.pi, n_points) - np.pi/2) + 45

    # 3. Random noise for realism
    noise_electronics = np.random.normal(0, 12, n_points)
    noise_apparel = np.random.normal(0, 10, n_points)

    # Combine components to create final revenue data
    revenue_electronics = base_growth_electronics + seasonal_component + noise_electronics
    revenue_apparel = base_growth_apparel + (seasonal_component * 0.8) + noise_apparel

    # Create the final pandas DataFrame
    df_electronics = pd.DataFrame({'Date': dates, 'Product Line': 'Electronics', 'Revenue': revenue_electronics})
    df_apparel = pd.DataFrame({'Date': dates, 'Product Line': 'Apparel', 'Revenue': revenue_apparel})
    
    return pd.concat([df_electronics, df_apparel], ignore_index=True)

def create_and_save_chart(df, filename='chart.png'):
    """
    Creates, styles, and saves the Seaborn lineplot.
    """
    # Set professional styling for the chart
    sns.set_style("whitegrid")
    sns.set_context("talk", font_scale=0.8)

    # Set figure size for 512x512 output (8 inches * 64 dpi = 512 pixels)
    plt.figure(figsize=(8, 8))

    # Create the lineplot with enhanced aesthetics
    sns.lineplot(
        data=df,
        x='Date',
        y='Revenue',
        hue='Product Line',
        palette='viridis',  # A professional and colorblind-friendly palette
        linewidth=2.5,
        marker='o',         # Add markers to highlight data points
        markersize=6,
        markeredgecolor='black'
    )

    # Add meaningful titles and labels
    plt.title('Monthly Revenue Growth by Product Line (2022-2024)', fontsize=16, weight='bold', pad=20)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Monthly Revenue (in thousands USD)', fontsize=12)

    # Improve legibility of the plot
    plt.xticks(rotation=45, ha='right') # Rotate x-axis labels to prevent overlap
    plt.legend(title='Product Line', title_fontsize='13', fontsize='11', frameon=True)
    sns.despine() # Remove the top and right spines for a cleaner look

    # Adjust layout to prevent labels from being cut off
    plt.tight_layout()

    # Save the chart as a PNG with 512x512 dimensions
    plt.savefig(filename, dpi=64)
    print(f"Chart saved successfully as '{filename}'.")

if __name__ == '__main__':
    # Generate the data
    revenue_df = generate_revenue_data()
    
    # Create and save the chart
    create_and_save_chart(revenue_df)