import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            # 📊 AI Business Analyst

            Enterprise Analytics Platform
            """
        )

        st.divider()

        selected = st.radio(
            "Navigation",
            [
                "Dashboard",
                "Upload Data",
                "Visualization",
                "AI Insights",
                "Chat with Data",
                "Export Report",
            ],
            label_visibility="collapsed",
        )

    return selected