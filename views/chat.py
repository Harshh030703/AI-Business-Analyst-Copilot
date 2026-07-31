import plotly.express as px


def missing_chart(df):

    missing = df.isna().sum()

    missing = missing[missing > 0]

    fig = px.bar(
        missing,
        x=missing.index,
        y=missing.values,
        color=missing.values,
        title="Missing Values by Column"
    )

    fig.update_layout(
        template="plotly_white",
        height=400
    )

    return fig