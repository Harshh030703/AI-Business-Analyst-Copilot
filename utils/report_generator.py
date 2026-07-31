from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf(df, output_path):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "AI Business Analyst Copilot",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            "Executive Analytics Report",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            datetime.now().strftime("%d %B %Y"),
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"<b>Rows:</b> {len(df)}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Columns:</b> {len(df.columns)}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Missing Values:</b> {df.isna().sum().sum()}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Duplicate Rows:</b> {df.duplicated().sum()}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "Generated using AI Business Analyst Copilot",
            styles["Italic"]
        )
    )

    doc.build(story)