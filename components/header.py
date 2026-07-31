import streamlit as st

def hero():

    st.markdown("""

<div style="
background:linear-gradient(135deg,#2563EB,#1E40AF);
padding:35px;
border-radius:20px;
color:white;
box-shadow:0 10px 30px rgba(37,99,235,.30);
">

<h1 style="color:white;margin-bottom:5px;">
📊 AI Business Analyst Copilot
</h1>

<h4 style="color:#E0E7FF;">
Enterprise Business Intelligence Platform
</h4>

<p style="font-size:18px;">

Analyze business datasets, generate KPIs,
visualize trends,
and receive AI-powered business insights.

</p>

</div>

""", unsafe_allow_html=True)

    st.write("")