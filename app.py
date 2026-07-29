import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from utils.data_processor import load_data, dataset_summary
from utils.charts import create_chart

st.set_page_config(
    page_title="AI Business Analyst Copilot",
    page_icon="📊",
    layout="wide",
)

# ---------------- Sidebar ---------------- #

with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Dashboard",
            "Upload Data",
            "Visualization",
            "AI Insights",
            "Chat with Data"
        ],
        icons=[
            "house",
            "cloud-upload",
            "bar-chart",
            "robot",
            "chat-dots"
        ],
        menu_icon="cast",
        default_index=0,
    )

st.title("📊 AI Business Analyst Copilot")

# ==========================================================
# Dashboard
# ==========================================================

if selected == "Dashboard":

    if "df" in st.session_state:

        df = st.session_state["df"]

        c1, c2, c3 = st.columns(3)

        c1.metric("Rows", df.shape[0])
        c2.metric("Columns", df.shape[1])
        c3.metric("Missing", int(df.isnull().sum().sum()))

        st.success("Dataset Loaded Successfully ✅")

    else:

        st.info("Upload a CSV or Excel file to begin analysis.")

# ==========================================================
# Upload
# ==========================================================

elif selected == "Upload Data":

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        df = load_data(uploaded_file)

        # Save DataFrame globally
        st.session_state["df"] = df

        st.success("Dataset Loaded Successfully!")

        summary = dataset_summary(df)

        # ---------- Metrics ----------

        r1 = st.columns(4)

        r1[0].metric("Rows", summary["Rows"])
        r1[1].metric("Columns", summary["Columns"])
        r1[2].metric("Missing", summary["Missing Values"])
        r1[3].metric("Duplicates", summary["Duplicate Rows"])

        r2 = st.columns(4)

        r2[0].metric("Numeric", summary["Numeric Columns"])
        r2[1].metric("Categorical", summary["Categorical Columns"])
        r2[2].metric("Date", summary["Date Columns"])
        r2[3].metric("Memory (MB)", summary["Memory Usage (MB)"])

        st.divider()

        st.subheader("📋 Dataset Preview")

        st.dataframe(df.head(10), use_container_width=True)

        st.divider()

        st.subheader("📌 Data Types")

        datatype_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

        st.dataframe(datatype_df, use_container_width=True)

        st.divider()

        st.subheader("⚠ Missing Values")

        missing = df.isnull().sum()

        missing = missing[missing > 0]

        if len(missing) == 0:
            st.success("No Missing Values Found")

        else:

            missing_df = pd.DataFrame({
                "Column": missing.index,
                "Missing Values": missing.values
            })

            st.dataframe(missing_df, use_container_width=True)

        st.divider()

        st.subheader("🔢 Unique Values")

        unique = pd.DataFrame({
            "Column": df.columns,
            "Unique Values": df.nunique()
        })

        st.dataframe(unique, use_container_width=True)

# ==========================================================
# Visualization
# ==========================================================

elif selected == "Visualization":

    st.header("📈 Interactive Visualization")

    if "df" not in st.session_state:

        st.warning("Please upload a dataset first.")

    else:

        df = st.session_state["df"]

        chart_type = st.selectbox(
            "Select Chart",
            [
                "Bar Chart",
                "Line Chart",
                "Scatter Plot",
                "Histogram",
                "Box Plot",
                "Pie Chart"
            ]
        )

        columns = df.columns.tolist()

        x_col = st.selectbox(
            "Select X-axis",
            columns
        )

        y_col = None

        if chart_type not in ["Histogram", "Pie Chart", "Box Plot"]:

            numeric_cols = df.select_dtypes(include="number").columns.tolist()

            y_col = st.selectbox(
                "Select Y-axis",
                numeric_cols
            )

        fig = create_chart(
            df,
            chart_type,
            x_col,
            y_col
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ==========================================================
# AI Insights
# ==========================================================

elif selected == "AI Insights":

    from utils.ai_helper import ask_ai

    st.header("🤖 AI Business Insights")

    if "df" not in st.session_state:

        st.warning("Please upload a dataset first.")

    else:

        df = st.session_state["df"]

        st.success("Dataset Ready ✅")

        if st.button("Generate AI Insights"):

            with st.spinner("Analyzing dataset..."):

                sample_data = df.head(50).to_string(index=False)

                prompt = f"""
You are a Senior Business Analyst.

Analyze the following dataset.

Provide:

1. Executive Summary

2. Key KPIs

3. Data Quality Issues

4. Interesting Trends

5. Business Risks

6. Business Opportunities

7. Recommendations

Dataset:

{sample_data}
"""

                response = ask_ai(prompt)

            st.markdown(response)


# ==========================================================
# Chat
# ==========================================================

elif selected == "Chat with Data":

    from utils.ai_helper import ask_ai

    st.header("💬 Chat with your Dataset")

    if "df" not in st.session_state:

        st.warning("Please upload a dataset first.")

    else:

        df = st.session_state["df"]

        question = st.text_area(
            "Ask a question about your dataset"
        )

        if st.button("Ask AI"):

            with st.spinner("Analyzing your data..."):

                dataset_info = f"""
Dataset Shape:
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Columns:
{', '.join(df.columns)}

Sample Data:

{df.head(30).to_string(index=False)}
"""

                prompt = f"""
You are an expert Business Analyst.

Answer ONLY using the dataset below.

If the answer cannot be determined from the available data,
say that clearly.

Dataset:

{dataset_info}

Question:

{question}
"""

                answer = ask_ai(prompt)

            st.success("Answer Generated")

            st.markdown(answer)
            