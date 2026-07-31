import streamlit as st


def load_theme():

    st.markdown("""
    <style>

    /* Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"]{
        font-family:'Poppins',sans-serif;
    }

    /* Background */
    .stApp{
        background:linear-gradient(
            135deg,
            #F8FAFC 0%,
            #EEF4FF 100%
        );
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background:#FFFFFF;
        border-right:1px solid #E5E7EB;
    }

    /* Main container */
    .block-container{
        padding-top:2rem;
        padding-left:2rem;
        padding-right:2rem;
        padding-bottom:2rem;
    }

    /* Headings */
    h1{
        color:#1E3A8A;
        font-weight:700;
    }

    h2,h3{
        color:#1F2937;
    }

    /* Streamlit metric */
    div[data-testid="stMetric"]{
        background:white;
        border-radius:16px;
        padding:20px;
        border:1px solid #E5E7EB;
        box-shadow:0 10px 25px rgba(0,0,0,.05);
    }

    /* Dataframe */
    div[data-testid="stDataFrame"]{
        border-radius:16px;
        overflow:hidden;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"]{
        font-size:16px;
        font-weight:600;
    }

    /* Buttons */
    button[kind="primary"]{
        border-radius:12px;
    }

    /* ---------- Glass KPI Card ---------- */

    .kpi-card{

        transition:all .25s ease;

        border-radius:22px;

    }

    .kpi-card:hover{

        transform:translateY(-6px);

        box-shadow:0 18px 40px rgba(37,99,235,.18);

    }

    </style>
    """, unsafe_allow_html=True)