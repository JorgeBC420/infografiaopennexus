#!/usr/bin/env python3
"""
Script para generar documentos HTML y ZIP protegidos para OpenNexus
Requiere: pip install markdown
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

def markdown_to_html(md_file, title):
    """Convierte Markdown a HTML con estilos optimizados para impresión"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content)
    
    # Agregar estilos CSS optimizados para impresión
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
            
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 900px;
                margin: 0 auto;
                padding: 30px;
                background-color: #ffffff;
            }}
            
            @media print {{
                body {{
                    background-color: white;
                    padding: 20px;
                    max-width: none;
                }}
                .no-print {{
                    display: none !important;
                }}
            }}
            
            h1 {{
                color: #00A6FB;
                border-bottom: 3px solid #00F5D4;
                padding-bottom: 10px;
                margin-bottom: 20px;
                font-size: 2.5em;
                font-weight: 700;
            }}
            
            h2 {{
                color: #003554;
                border-bottom: 2px solid #00A6FB;
                padding-bottom: 8px;
                margin-top: 30px;
                margin-bottom: 15px;
                font-size: 1.8em;
                font-weight: 600;
            }}
            
            h3 {{
                color: #006494;
                margin-top: 25px;
                margin-bottom: 12px;
                font-size: 1.3em;
                font-weight: 600;
            }}
            
            p {{
                margin-bottom: 15px;
                text-align: justify;
            }}
            
            ul, ol {{
                margin-bottom: 15px;
                padding-left: 25px;
            }}
            
            li {{
                margin-bottom: 5px;
            }}
            
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 25px 0;
                background-color: white;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            
            th {{
                background-color: #00A6FB;
                color: white;
                font-weight: 600;
            }}
            
            tr:nth-child(even) {{
                background-color: #f8f9fa;
            }}
            
            .highlight {{
                background: linear-gradient(135deg, #e3f2fd 0%, #f0f8ff 100%);
                padding: 20px;
                border-left: 5px solid #00A6FB;
                margin: 25px 0;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,166,251,0.1);
            }}
            
            .footer {{
                text-align: center;
                margin-top: 50px;
                padding: 25px;
                background: linear-gradient(135deg, #003554 0%, #006494 100%);
                color: white;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,53,84,0.3);
            }}
            
            .footer h3 {{
                color: #00F5D4;
                border-bottom: 2px solid #00F5D4;
                display: inline-block;
                padding-bottom: 8px;
                margin-bottom: 15px;
            }}
            
            .password-info {{
                background: linear-gradient(135deg, #051923 0%, #003554 100%);
                color: #00F5D4;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                font-weight: 600;
                text-align: center;
                border: 2px solid #00A6FB;
            }}
            
            .print-instruction {{
                background-color: #fff3cd;
                border: 1px solid #ffeaa7;
                color: #856404;
                padding: 15px;
                border-radius: 8px;
                margin: 20px 0;
                text-align: center;
                font-weight: 500;
            }}
        </style>
    </head>
    <body>
        <div class="password-info">
            <strong>🔒 Documento Confidencial - OpenNexus 2025</strong><br>
            Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
            Contraseña del archivo: <strong>{generate_dynamic_password()}</strong>
        </div>
        
        <div class="print-instruction no-print">
            💡 <strong>Para convertir a PDF:</strong> Usa Ctrl+P → Guardar como PDF en tu navegador
        </div>
        
        {html_content}
        
        <div class="footer">
            <h3>OpenNexus - Transformando una Amenaza Nacional en una Oportunidad Global</h3>
            <p><strong>Jorge Eduardo Bravo Chaves | Fundador</strong><br>
            SINPE Móvil: +506 71880297<br>
            GitHub: github.com/JorgeBC420<br>
            Email: contacto bajo solicitud</p>
            <p style="margin-top: 15px; font-size: 0.9em; opacity: 0.8;">
                Documento generado automáticamente • {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            </p>
        </div>
    </body>
    </html>
    """
    return styled_html

def create_protected_zip(html_file, output_name):
    """Crea un ZIP protegido con contraseña"""
    password = generate_dynamic_password()
    
    with zipfile.ZipFile(f"{output_name}.zip", 'w') as zipf:
        zipf.write(html_file, os.path.basename(html_file))
        zipf.setpassword(password.encode())
    
    print(f"✅ Archivo creado: {output_name}.zip")
    print(f"🔑 Contraseña: {password}")
    return f"{output_name}.zip"

def main():
    print("🚀 Generando documentos HTML de OpenNexus...")
    
    # Generar Pitch Deck
    if os.path.exists('OpenNexus_PitchDeck_2025.md'):
        print("📊 Generando Pitch Deck...")
        html_content = markdown_to_html('OpenNexus_PitchDeck_2025.md', 'OpenNexus Pitch Deck 2025')
        
        html_filename = 'OpenNexus_PitchDeck_2025.html'
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        create_protected_zip(html_filename, 'OpenNexus_PitchDeck_2025')
        print("✅ Pitch Deck HTML generado exitosamente")
    
    # Generar Business Plan
    if os.path.exists('OpenNexus_BusinessPlan_2025.md'):
        print("📈 Generando Business Plan...")
        html_content = markdown_to_html('OpenNexus_BusinessPlan_2025.md', 'OpenNexus Business Plan 2025')
        
        html_filename = 'OpenNexus_BusinessPlan_2025.html'
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        create_protected_zip(html_filename, 'OpenNexus_BusinessPlan_2025')
        print("✅ Business Plan HTML generado exitosamente")
    
    # Generar Propuesta Schneider Electric
    if os.path.exists('OpenNexus_SchneiderPartnership_2025.md'):
        print("🏢 Generando Propuesta Schneider Electric...")
        html_content = markdown_to_html('OpenNexus_SchneiderPartnership_2025.md', 'NexusOptim IA - Schneider Electric Partnership')
        
        html_filename = 'OpenNexus_SchneiderPartnership_2025.html'
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        create_protected_zip(html_filename, 'OpenNexus_SchneiderPartnership_2025')
        print("✅ Propuesta Schneider Electric HTML generada exitosamente")
    
    # Generar Documentación Games Lab
    if os.path.exists('OpenNexus_GamesLab_CaminosFe.md'):
        print("🎮 Generando Documentación Games Lab - Caminos de la Fe...")
        html_content = markdown_to_html('OpenNexus_GamesLab_CaminosFe.md', 'OpenNexus Games Lab - Caminos de la Fe RPG')
        
        html_filename = 'OpenNexus_GamesLab_CaminosFe.html'
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        create_protected_zip(html_filename, 'OpenNexus_GamesLab_CaminosFe')
        print("✅ Documentación Games Lab HTML generada exitosamente")
    
    print(f"\n🔑 Contraseña dinámica actual: {generate_dynamic_password()}")
    print("📁 Archivos ZIP con HTML creados con contraseña de protección")
    print("🌐 Los archivos HTML se pueden abrir en cualquier navegador")
    print("💡 Para convertir a PDF: Abrir HTML en navegador → Imprimir → Guardar como PDF")

if __name__ == "__main__":
    main()
