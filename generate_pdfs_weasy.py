#!/usr/bin/env python3
"""
Script alternativo para generar PDFs usando WeasyPrint (más liviano que pdfkit)
Requiere: pip install markdown weasyprint
"""

import os
import markdown
import zipfile
from datetime import datetime
import hashlib

def generate_dynamic_password():
    """Genera la contraseña dinámica basada en la fecha actual"""
    today = datetime.now()
    date_string = today.strftime('%Y-%m-%d')
    seed = f"OpenNexus{date_string}2025"
    
    # Crear hash simple basado en la fecha
    hash_obj = hashlib.md5(seed.encode())
    hash_hex = hash_obj.hexdigest()
    
    # Convertir a contraseña legible (mismo algoritmo que JavaScript)
    hash_int = int(hash_hex[:6], 16)
    password = f"ONX{str(hash_int)[:6]}Tech"
    return password

def markdown_to_html_pdf(md_file, title):
    """Convierte Markdown a HTML optimizado para PDF con WeasyPrint"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content)
    
    # HTML optimizado para WeasyPrint
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            @page {{
                size: A4;
                margin: 2cm;
            }}
            
            body {{
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
                font-size: 12pt;
            }}
            
            h1 {{
                color: #00A6FB;
                border-bottom: 3px solid #00F5D4;
                padding-bottom: 10px;
                margin-bottom: 20px;
                font-size: 24pt;
                font-weight: bold;
                page-break-before: avoid;
            }}
            
            h2 {{
                color: #003554;
                border-bottom: 2px solid #00A6FB;
                padding-bottom: 8px;
                margin-top: 30px;
                margin-bottom: 15px;
                font-size: 18pt;
                font-weight: bold;
                page-break-after: avoid;
            }}
            
            h3 {{
                color: #006494;
                margin-top: 25px;
                margin-bottom: 12px;
                font-size: 14pt;
                font-weight: bold;
                page-break-after: avoid;
            }}
            
            p {{
                margin-bottom: 12pt;
                text-align: justify;
                orphans: 2;
                widows: 2;
            }}
            
            ul, ol {{
                margin-bottom: 12pt;
                padding-left: 20pt;
            }}
            
            li {{
                margin-bottom: 4pt;
            }}
            
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20pt 0;
                page-break-inside: avoid;
            }}
            
            th, td {{
                border: 1pt solid #333;
                padding: 8pt;
                text-align: left;
                font-size: 10pt;
            }}
            
            th {{
                background-color: #00A6FB;
                color: white;
                font-weight: bold;
            }}
            
            .header-info {{
                background-color: #e3f2fd;
                padding: 15pt;
                border-left: 5pt solid #00A6FB;
                margin-bottom: 20pt;
                border-radius: 5pt;
                page-break-inside: avoid;
            }}
            
            .footer {{
                text-align: center;
                margin-top: 40pt;
                padding: 20pt;
                background-color: #003554;
                color: white;
                border-radius: 8pt;
                page-break-inside: avoid;
            }}
            
            .footer h3 {{
                color: #00F5D4;
                margin-bottom: 10pt;
            }}
        </style>
    </head>
    <body>
        <div class="header-info">
            <strong>🔒 Documento Confidencial - OpenNexus 2025</strong><br>
            Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
            Contraseña del archivo: <strong>{generate_dynamic_password()}</strong>
        </div>
        
        {html_content}
        
        <div class="footer">
            <h3>OpenNexus - Transformando una Amenaza Nacional en una Oportunidad Global</h3>
            <p><strong>Jorge Eduardo Bravo Chaves | Fundador</strong><br>
            SINPE Móvil: +506 71880297<br>
            GitHub: github.com/JorgeBC420<br>
            Email: contacto bajo solicitud</p>
            <p style="margin-top: 10pt; font-size: 9pt;">
                Documento generado automáticamente • {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            </p>
        </div>
    </body>
    </html>
    """
    return styled_html

def create_protected_zip(pdf_file, output_name):
    """Crea un ZIP protegido con contraseña"""
    password = generate_dynamic_password()
    
    with zipfile.ZipFile(f"{output_name}.zip", 'w') as zipf:
        zipf.write(pdf_file, os.path.basename(pdf_file))
        zipf.setpassword(password.encode())
    
    print(f"✅ Archivo creado: {output_name}.zip")
    print(f"🔑 Contraseña: {password}")
    return f"{output_name}.zip"

def main():
    try:
        from weasyprint import HTML, CSS
        print("🚀 Generando documentos PDF con WeasyPrint...")
    except ImportError:
        print("❌ WeasyPrint no está instalado.")
        print("💡 Instala con: pip install weasyprint")
        print("📝 Alternativamente, usa generate_pdfs.py para generar HTML")
        return
    
    # Generar Pitch Deck
    if os.path.exists('OpenNexus_PitchDeck_2025.md'):
        print("📊 Generando Pitch Deck PDF...")
        html_content = markdown_to_html_pdf('OpenNexus_PitchDeck_2025.md', 'OpenNexus Pitch Deck 2025')
        
        # Crear PDF con WeasyPrint
        HTML(string=html_content).write_pdf('OpenNexus_PitchDeck_2025.pdf')
        create_protected_zip('OpenNexus_PitchDeck_2025.pdf', 'OpenNexus_PitchDeck_2025_PDF')
        print("✅ Pitch Deck PDF generado exitosamente")
    
    # Generar Business Plan
    if os.path.exists('OpenNexus_BusinessPlan_2025.md'):
        print("📈 Generando Business Plan PDF...")
        html_content = markdown_to_html_pdf('OpenNexus_BusinessPlan_2025.md', 'OpenNexus Business Plan 2025')
        
        # Crear PDF con WeasyPrint
        HTML(string=html_content).write_pdf('OpenNexus_BusinessPlan_2025.pdf')
        create_protected_zip('OpenNexus_BusinessPlan_2025.pdf', 'OpenNexus_BusinessPlan_2025_PDF')
        print("✅ Business Plan PDF generado exitosamente")
    
    print(f"\n🔑 Contraseña dinámica actual: {generate_dynamic_password()}")
    print("📁 Archivos ZIP con PDF creados con contraseña de protección")
    print("🌐 PDFs listos para distribución profesional")

if __name__ == "__main__":
    main()
