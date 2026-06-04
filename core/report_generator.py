from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime
import os


def generate_pdf_report(
    investigation
):

    os.makedirs(
        "exports",
        exist_ok=True
    )

    filename = (
        f"exports/"
        f"{investigation['name'].replace(' ', '_')}.pdf"
    )

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "MAILTRACE INVESTIGATION REPORT",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Investigation: {investigation['name']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Target: {investigation['target']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Created: {investigation['created']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Generated: {datetime.now()}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Notes",
            styles["Heading2"]
        )
    )

    for note in investigation[
        "notes"
    ]:

        content.append(
            Paragraph(
                f"• {note}",
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Evidence",
            styles["Heading2"]
        )
    )

    for evidence in investigation[
        "evidence"
    ]:

        content.append(
            Paragraph(
                str(evidence),
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

    doc.build(content)

    return filename