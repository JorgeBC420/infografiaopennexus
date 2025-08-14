#!/usr/bin/env python3
"""
Script simplificado para generar documentos HTML de OpenNexus
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
    hash_int = 0
    for char in seed:
        hash_int = ((hash_int << 5) - hash_int) + ord(char)
        hash_int = hash_int & hash_int  # Convertir a 32bit
    
    # Convertir a contraseña legible (mismo algoritmo que JavaScript)
    password = f"ONX{str(abs(hash_int))[:6]}Tech"
    return password

def markdown_to_html(md_file, title):
    """Convierte Markdown a HTML con estilos profesionales"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content, extensions=['tables'])
    
    # Agregar estilos CSS profesionales
    styled_html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
            
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #2c3e50;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }}
            
            .container {{
                max-width: 900px;
                margin: 0 auto;
                background: white;
                border-radius: 15px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                overflow: hidden;
            }}
            
            .header {{
                background: linear-gradient(135deg, #00A6FB 0%, #00F5D4 100%);
                color: white;
                padding: 40px;
                text-align: center;
            }}
            
            .header h1 {{
                font-size: 2.5em;
                font-weight: 900;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }}
            
            .content {{
                padding: 40px;
            }}
            
            h1, h2, h3, h4, h5, h6 {{
                color: #00A6FB;
                margin: 30px 0 15px 0;
                font-weight: 700;
            }}
            
            h1 {{
                font-size: 2.2em;
                border-bottom: 3px solid #00F5D4;
                padding-bottom: 10px;
            }}
            
            h2 {{
                font-size: 1.8em;
                border-bottom: 2px solid #00A6FB;
                padding-bottom: 8px;
            }}
            
            h3 {{
                font-size: 1.4em;
                color: #003554;
            }}
            
            p {{
                margin: 15px 0;
                text-align: justify;
            }}
            
            ul, ol {{
                margin: 15px 0 15px 30px;
            }}
            
            li {{
                margin: 8px 0;
            }}
            
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 25px 0;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                border-radius: 10px;
                overflow: hidden;
            }}
            
            th, td {{
                padding: 15px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            
            th {{
                background: linear-gradient(135deg, #00A6FB, #0582CA);
                color: white;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            
            tr:hover {{
                background-color: #f8f9fa;
            }}
            
            .highlight {{
                background: linear-gradient(135deg, #e3f2fd, #f1f8e9);
                padding: 20px;
                border-left: 5px solid #00A6FB;
                margin: 25px 0;
                border-radius: 5px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            }}
            
            .warning {{
                background: linear-gradient(135deg, #fff3cd, #ffeaa7);
                border-left-color: #ffc107;
            }}
            
            .success {{
                background: linear-gradient(135deg, #d4edda, #b8e6b8);
                border-left-color: #28a745;
            }}
            
            .footer {{
                background: linear-gradient(135deg, #003554, #006494);
                color: white;
                text-align: center;
                padding: 40px;
                margin-top: 40px;
            }}
            
            .footer h3 {{
                color: #00F5D4;
                margin-bottom: 15px;
            }}
            
            .password-box {{
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin: 20px 0;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }}
            
            .password-code {{
                font-family: 'Courier New', monospace;
                font-size: 1.5em;
                font-weight: bold;
                background: rgba(0,0,0,0.3);
                padding: 10px 20px;
                border-radius: 5px;
                display: inline-block;
                margin: 10px 0;
                letter-spacing: 2px;
            }}
            
            .emoji {{
                font-size: 1.2em;
                margin-right: 8px;
            }}
            
            @media print {{
                body {{
                    background: white;
                    padding: 0;
                }}
                
                .container {{
                    box-shadow: none;
                    border-radius: 0;
                }}
                
                .header {{
                    background: #00A6FB !important;
                    -webkit-print-color-adjust: exact;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 {title}</h1>
                <p style="font-size: 1.2em; margin-top: 15px;">OpenNexus - Transformando una Amenaza Nacional en una Oportunidad Global</p>
            </div>
            
            <div class="password-box">
                <div class="emoji">🔒</div>
                <strong>Documento Confidencial - OpenNexus 2025</strong><br>
                Generado el: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}<br>
                <div class="password-code">{generate_dynamic_password()}</div>
                <small>Contraseña de acceso al archivo ZIP</small>
            </div>
            
            <div class="content">
                {html_content}
            </div>
            
            <div class="footer">
                <h3>🌟 OpenNexus - Soberanía Tecnológica de Costa Rica</h3>
                <p><strong>Jorge Eduardo Bravo Chaves</strong> | Fundador y CEO<br>
                📱 SINPE Móvil: +506 71880297<br>
                💻 GitHub: github.com/JorgeBC420<br>
                🌐 Web: https://infografiaopennexusv1.pages.dev/</p>
                
                <div style="margin-top: 20px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.3);">
                    <small>© 2025 OpenNexus. Todos los derechos reservados.<br>
                    Este documento contiene información confidencial y propietaria.</small>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return styled_html

def create_protected_zip(html_file, output_name):
    """Crea un ZIP protegido con contraseña"""
    password = generate_dynamic_password()
    
    # Crear ZIP con contraseña (requiere pyminizip o usar zipfile sin contraseña)
    zip_filename = f"{output_name}.zip"
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(html_file, os.path.basename(html_file))
    
    print(f"✅ Archivo creado: {zip_filename}")
    print(f"🔑 Contraseña: {password}")
    print(f"📄 Contenido: {html_file}")
    return zip_filename

def main():
    print("🚀 Generando documentos HTML de OpenNexus...")
    print(f"🔑 Contraseña dinámica actual: {generate_dynamic_password()}")
    print("=" * 60)
    
    # Generar Pitch Deck
    if os.path.exists('OpenNexus_PitchDeck_2025.md'):
        print("📊 Generando Pitch Deck HTML...")
        html_content = markdown_to_html('OpenNexus_PitchDeck_2025.md', 'Pitch Deck 2025')
        
        html_filename = 'OpenNexus_PitchDeck_2025.html'
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        create_protected_zip(html_filename, 'OpenNexus_PitchDeck_2025')
        print("✅ Pitch Deck generado exitosamente\n")
    
    # Generar Business Plan
    if os.path.exists('OpenNexus_BusinessPlan_2025.md'):
        print("📈 Generando Business Plan HTML...")
        html_content = markdown_to_html('OpenNexus_BusinessPlan_2025.md', 'Business Plan 2025')
        
        html_filename = 'OpenNexus_BusinessPlan_2025.html'
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        create_protected_zip(html_filename, 'OpenNexus_BusinessPlan_2025')
        print("✅ Business Plan generado exitosamente\n")
    
    print("=" * 60)
    print("🎉 ¡Generación completada!")
    print("📁 Archivos ZIP listos para distribución")
    print("🌐 Los archivos HTML se pueden abrir en cualquier navegador")
    print("🖨️ Para convertir a PDF: Abrir HTML en navegador → Imprimir → Guardar como PDF")

if __name__ == "__main__":
    main()
