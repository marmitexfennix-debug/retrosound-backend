from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_certificate(user, music_id):
    path = f"{music_id}.pdf"

    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()

    content = [
        Paragraph("CERTIFICADO DE ORIGINALIDADE", styles["Title"]),
        Paragraph(f"Usuário: {user}", styles["Normal"]),
        Paragraph(f"ID: {music_id}", styles["Normal"]),
        Paragraph("Obra original gerada por IA.", styles["Normal"])
    ]

    doc.build(content)

    return path
