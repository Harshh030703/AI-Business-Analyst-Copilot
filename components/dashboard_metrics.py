import streamlit as st


def dataset_health(df):
    """
    Display dataset health metrics.
    """

    total_cells = df.shape[0] * df.shape[1]

    missing = int(df.isna().sum().sum())

    quality = round((1 - missing / total_cells) * 100, 2)

    memory = round(
        df.memory_usage(deep=True).sum() / (1024 ** 2),
        2
    )

    numeric_columns = len(
        df.select_dtypes(include="number").columns
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Dataset Health",
            f"{quality}%"
        )

    with c2:
        st.metric(
            "Memory Usage",
            f"{memory} MB"
        )

    with c3:
        st.metric(
            "Numeric Columns",
            numeric_columns
        )