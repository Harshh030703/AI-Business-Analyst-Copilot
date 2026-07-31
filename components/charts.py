import plotly.express as px
import pandas as pd


def missing_chart(df):
    """
    Creates a bar chart showing missing values for each column.
    """

    missing = df.isna().sum()
    missing = missing[missing > 0]

    # If there are no missing values
    if missing.empty:
        fig = px.bar(
            x=["No Missing Values"],
            y=[0],
            title="Missing Values by Column"
        )
        fig.update_layout(
            template="plotly_white",
            height=400
        )
        return fig

    chart_df = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    fig = px.bar(
        chart_df,
        x="Column",
        y="Missing Values",
        color="Missing Values",
        color_continuous_scale="Blues",
        title="Missing Values by Column"
    )

    fig.update_layout(
        template="plotly_white",
        height=400,
        xaxis_title="Columns",
        yaxis_title="Missing Values"
    )

    return fig