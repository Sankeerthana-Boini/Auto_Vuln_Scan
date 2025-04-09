from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(data, output_path="reports\\report.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setFont("Helvetica", 12)
    y = 800
    c.drawString(100, y, "Vulnerability Scan Report")
    y -= 40

    for item in data:
        c.drawString(100, y, f"Name: {item['name']}")
        y -= 20
        c.drawString(100, y, f"Risk: {item['risk']}")
        y -= 20
        c.drawString(100, y, f"Description: {item['desc'][:100]}")
        y -= 20
        c.drawString(100, y, f"Solution: {item['solution'][:100]}")
        y -= 40
        if y < 100:
            c.showPage()
            y = 800

    c.save()
