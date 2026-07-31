import streamlit as st


def metric_card(title, value, help_text="", color="#2563EB", icon="📊"):

    st.markdown(
        f"""
        <div class="kpi-card" style="
            background:rgba(255,255,255,0.72);
            backdrop-filter:blur(14px);
            -webkit-backdrop-filter:blur(14px);

            border:1px solid rgba(255,255,255,.35);
            border-left:8px solid {color};

            border-radius:22px;

            padding:22px;

            box-shadow:
                0 8px 30px rgba(0,0,0,.08);

            margin-bottom:10px;
        ">

            <div style="
                font-size:18px;
                color:#6B7280;
                font-weight:600;
            ">

                {icon} {title}

            </div>

            <div style="
                font-size:42px;
                font-weight:700;
                color:#111827;
                margin-top:8px;
            ">

                {value}

            </div>

            <div style="
                color:#6B7280;
                font-size:14px;
                margin-top:8px;
            ">

                {help_text}

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )