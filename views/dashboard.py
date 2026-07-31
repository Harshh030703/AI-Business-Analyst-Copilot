import streamlit as st
import pandas as pd

from components.cards import metric_card
from components.header import hero
from components.charts import missing_chart
from components.dashboard_metrics import dataset_health


def show_dashboard(df):

    # ==========================================
    # Header
    # ==========================================

    hero()

    # ==========================================
    # KPI Cards
    # ==========================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            title="Records",
            value=f"{len(df):,}",
            help_text="Total rows in dataset",
            color="#2563EB",
            icon="📄"
        )

    with c2:
        metric_card(
            title="Columns",
            value=len(df.columns),
            help_text="Total features",
            color="#16A34A",
            icon="🧩"
        )

    with c3:

        missing = int(df.isna().sum().sum())

        metric_card(
            title="Missing Values",
            value=missing,
            help_text="Null values detected",
            color="#F59E0B" if missing > 0 else "#16A34A",
            icon="⚠️"
        )

    with c4:

        duplicate = int(df.duplicated().sum())

        metric_card(
            title="Duplicate Rows",
            value=duplicate,
            help_text="Duplicate records",
            color="#DC2626" if duplicate > 0 else "#16A34A",
            icon="📋"
        )

    st.divider()

    # ==========================================
    # Executive Dashboard
    # ==========================================

    st.subheader("📈 Executive Dashboard")

    dataset_health(df)

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("📉 Missing Value Analysis")

        st.plotly_chart(
            missing_chart(df),
            use_container_width=True
        )

    with right:

        st.subheader("📊 Column Distribution")

        dtype = df.dtypes.astype(str).value_counts()

        st.bar_chart(dtype)

    st.divider()

    # ==========================================
    # Tabs
    # ==========================================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📋 Preview",
            "📊 Statistics",
            "📈 Data Types",
            "⚠️ Quality Report"
        ]
    )

    # ==========================================
    # Preview
    # ==========================================

    with tab1:

        st.dataframe(
            df,
            use_container_width=True,
            height=450
        )

    # ==========================================
    # Statistics
    # ==========================================

    with tab2:

        stats = df.describe(include="all").transpose()

        st.dataframe(
            stats,
            use_container_width=True
        )

    # ==========================================
    # Data Types
    # ==========================================

    with tab3:

        datatype_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

        st.dataframe(
            datatype_df,
            use_container_width=True
        )

    # ==========================================
    # Quality Report
    # ==========================================

    with tab4:

        quality = pd.DataFrame({

            "Metric": [
                "Rows",
                "Columns",
                "Missing Values",
                "Duplicate Rows",
                "Memory Usage (MB)"
            ],

            "Value": [
                len(df),
                len(df.columns),
                int(df.isna().sum().sum()),
                int(df.duplicated().sum()),
                round(df.memory_usage(deep=True).sum() / 1024**2, 2)
            ]

        })

        st.dataframe(
            quality,
            use_container_width=True
        )