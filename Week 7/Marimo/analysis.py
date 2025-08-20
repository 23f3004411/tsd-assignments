# Copyright 2024 Marimo. All rights reserved.

import marimo

__generated_with = "0.14.17"
app = marimo.App()


@app.cell
def _():
    # 23f3004411@ds.study.iitm.ac.in
    import marimo as mo
    import pandas as pd
    import numpy as np
    import altair as alt
    return alt, mo, np, pd


@app.cell
def _(mo):
    num_points_slider = mo.ui.slider(
        start=10, stop=200, step=10, value=50, label="Number of Data Points:"
    )
    return (num_points_slider,)


@app.cell
def _(np, num_points_slider, pd):
    def create_data():
        n = num_points_slider.value
        rng = np.random.default_rng(42)
        data = {
            "x": rng.uniform(0, 10, n),
            "y": rng.uniform(0, 10, n),
            "size": rng.integers(50, 500, n),
        }
        df = pd.DataFrame(data)
        return df, n
    return (create_data,)


@app.cell
def _(alt, create_data, mo):
    def create_outputs():
        df, n = create_data() # Call the function from the cell above
    
        # Dynamic markdown that updates based on the slider's state.
        markdown_output = mo.md(f"""
            ## 📊 Scatter Plot Analysis
        
            The scatter plot below visualizes the relationship between the 'x' and 'y' variables
            for **{n}** randomly generated data points.
        
            Use the slider at the top to change the number of points displayed.
        """)
    
        # An Altair scatter plot that visualizes the data from the DataFrame.
        scatter_plot = (
            alt.Chart(df)
            .mark_circle()
            .encode(
                x="x",
                y="y",
                size="size",
                tooltip=["x", "y", "size"],
            )
            .properties(
                title="Relationship between X and Y"
            )
        )
        return markdown_output, scatter_plot
    return (create_outputs,)


@app.cell
def _(create_outputs, mo, num_points_slider):
    markdown, plot = create_outputs()
    mo.vstack(
        [
            num_points_slider,
            markdown,
            plot,
        ]
    )
    return


if __name__ == "__main__":
    app.run()
