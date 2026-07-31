from utils.report_generator import generate_pdf
import os

if st.button("📄 Generate PDF Report"):

    os.makedirs("reports", exist_ok=True)

    pdf_path = "reports/executive_report.pdf"

    generate_pdf(df, pdf_path)

    with open(pdf_path, "rb") as pdf:

        st.download_button(
            "⬇ Download Report",
            data=pdf,
            file_name="Executive_Report.pdf",
            mime="application/pdf"
        )