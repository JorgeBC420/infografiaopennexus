#!/usr/bin/env python3
"""
Script para generar PDFs protegidos con contraseña para OpenNexus
Requiere: pip install markdown pdfkit pymupdf
"""

import os
import markdown
import pdfkit
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

def markdown_to_html(md_file, title):
    """Convierte Markdown a HTML con estilos"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content)
    
    # Agregar estilos CSS
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            body {{
                font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f8f9fa;
            }}
            h1, h2, h3 {{
                color: #00A6FB;
                border-bottom: 2px solid #00F5D4;
                padding-bottom: 5px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #00A6FB;
                color: white;
            }}
            .highlight {{
                background-color: #e3f2fd;
                padding: 15px;
                border-left: 4px solid #00A6FB;
                margin: 20px 0;
            }}
            .footer {{
                text-align: center;
                margin-top: 40px;
                padding: 20px;
                background-color: #003554;
                color: white;
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="highlight">
            <strong>🔒 Documento Confidencial - OpenNexus 2025</strong><br>
            Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
            Contraseña del archivo: {generate_dynamic_password()}
        </div>
        {html_content}
        <div class="footer">
            <h3>OpenNexus - Transformando una Amenaza Nacional en una Oportunidad Global</h3>
            <p>Jorge Eduardo Bravo Chaves | Fundador<br>
            SINPE Móvil: +506 71880297<br>
            GitHub: github.com/JorgeBC420</p>
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
    print("🚀 Generando documentos PDF de OpenNexus...")
    
    # Configuración de wkhtmltopdf (ajustar path según instalación)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    
    # Opciones para PDF
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None
    }
    
    # Generar Pitch Deck
    if os.path.exists('OpenNexus_PitchDeck_2025.md'):
        print("📊 Generando Pitch Deck...")
        html_content = markdown_to_html('OpenNexus_PitchDeck_2025.md', 'OpenNexus Pitch Deck 2025')
        
        with open('temp_pitchdeck.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        pdfkit.from_file('temp_pitchdeck.html', 'OpenNexus_PitchDeck_2025.pdf', 
                        options=options, configuration=config)
        
        create_protected_zip('OpenNexus_PitchDeck_2025.pdf', 'OpenNexus_PitchDeck_2025')
        
        os.remove('temp_pitchdeck.html')
        print("✅ Pitch Deck generado exitosamente")
    
    # Generar Business Plan
    if os.path.exists('OpenNexus_BusinessPlan_2025.md'):
        print("📈 Generando Business Plan...")
        html_content = markdown_to_html('OpenNexus_BusinessPlan_2025.md', 'OpenNexus Business Plan 2025')
        
        with open('temp_businessplan.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        pdfkit.from_file('temp_businessplan.html', 'OpenNexus_BusinessPlan_2025.pdf', 
                        options=options, configuration=config)
        
        create_protected_zip('OpenNexus_BusinessPlan_2025.pdf', 'OpenNexus_BusinessPlan_2025')
        
        os.remove('temp_businessplan.html')
        print("✅ Business Plan generado exitosamente")
    
    print(f"\n🔑 Contraseña dinámica actual: {generate_dynamic_password()}")
    print("📁 Archivos ZIP creados con contraseña de protección")
    print("🌐 Listos para subir al servidor o distribuir")

if __name__ == "__main__":
    main()
