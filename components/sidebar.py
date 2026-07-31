import streamlit as st
from streamlit_option_menu import option_menu


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            # 📊 AI Business Analyst

            Enterprise Analytics Platform
            """
        )

        st.divider()

        selected = option_menu(
            menu_title=None,

            options=[
                "Dashboard",
                "Upload Data",
                "Visualization",
                "AI Insights",
                "Chat with Data",
            ],

            icons=[
                "house",
                "cloud-upload",
                "bar-chart",
                "robot",
                "chat-dots",
            ],

            default_index=0,

            styles={
                "container": {
                    "padding": "5px",
                    "background-color": "#ffffff",
                    "border-radius": "10px",
                },

                "icon": {
                    "color": "#2563EB",
                    "font-size": "18px",
                },

                "nav-link": {
                    "font-size": "17px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#EEF4FF",
                },

                "nav-link-selected": {
                    "background-color": "#2563EB",
                    "color": "white",
                },
            },
        )

    return selected