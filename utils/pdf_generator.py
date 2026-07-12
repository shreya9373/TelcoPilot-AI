from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report_text, filename="incident_report.pdf"):
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    for line in report_text.split("\n"):
        story.append(Paragraph(line.replace(" ", "&nbsp;"), styles["BodyText"]))

    doc.build(story)

    return filename