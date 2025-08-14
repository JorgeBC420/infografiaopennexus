#!/usr/bin/env python3
"""
Script especializado para generar la propuesta de Schneider Electric
con estilos corporativos profesionales
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
    
    # Convertir a contraseña legible
    hash_int = int(hash_hex[:6], 16)
    password = f"ONX{str(hash_int)[:6]}Tech"
    return password

def schneider_markdown_to_html(md_file):
    """Convierte Markdown a HTML con estilos corporativos para Schneider Electric"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content, extensions=['tables'])
    
    # HTML con estilos corporativos profesionales
    styled_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NexusOptim IA - Schneider Electric Partnership</title>
        <style>
            @media print {{
                @page {{ 
                    size: A4; 
                    margin: 2cm;
                    @top-center {{ 
                        content: "NexusOptim IA - Schneider Electric Partnership"; 
                        font-size: 10pt; 
                        color: #666; 
                    }}
                    @bottom-right {{ 
                        content: "Page " counter(page); 
                        font-size: 10pt; 
                        color: #666; 
                    }}
                }}
                .page-break {{ page-break-before: always; }}
                .no-print {{ display: none !important; }}
            }}
            
            body {{
                font-family: 'Segoe UI', Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                font-size: 12pt;
                margin: 0;
                padding: 20px;
                background-color: #ffffff;
            }}
            
            .header {{
                text-align: center;
                background: linear-gradient(135deg, #2E7D32, #1976D2);
                color: white;
                padding: 30px;
                border-radius: 10px;
                margin-bottom: 30px;
                box-shadow: 0 4px 20px rgba(46, 125, 50, 0.3);
            }}
            
            .header h1 {{
                font-size: 28pt;
                margin: 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }}
            
            .header h2 {{
                font-size: 16pt;
                margin: 10px 0 0 0;
                opacity: 0.9;
            }}
            
            .confidential-banner {{
                background: linear-gradient(135deg, #051923 0%, #003554 100%);
                color: #00F5D4;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                font-weight: 600;
                text-align: center;
                border: 2px solid #00A6FB;
            }}
            
            .info-box {{
                background: #F8F9FA;
                border: 2px solid #E9ECEF;
                border-radius: 8px;
                padding: 20px;
                margin: 20px 0;
            }}
            
            h1 {{
                color: #1976D2;
                font-size: 24pt;
                margin-top: 30px;
                margin-bottom: 15px;
                border-bottom: 3px solid #2196F3;
                padding-bottom: 10px;
                page-break-after: avoid;
            }}
            
            h2 {{
                color: #1976D2;
                font-size: 18pt;
                margin-top: 30px;
                margin-bottom: 15px;
                border-left: 5px solid #2196F3;
                padding-left: 15px;
                background: #E3F2FD;
                padding: 10px 0 10px 15px;
                page-break-after: avoid;
            }}
            
            h3 {{
                color: #F57C00;
                font-size: 14pt;
                margin-top: 20px;
                margin-bottom: 10px;
                page-break-after: avoid;
            }}
            
            .highlight {{
                background: #FFF3E0;
                border-left: 4px solid #FF9800;
                padding: 15px;
                margin: 15px 0;
                border-radius: 5px;
            }}
            
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                page-break-inside: avoid;
            }}
            
            th {{
                background: #2196F3;
                color: white;
                padding: 12px;
                text-align: left;
                font-weight: bold;
            }}
            
            td {{
                padding: 10px 12px;
                border-bottom: 1px solid #DDD;
            }}
            
            tr:nth-child(even) {{
                background: #F8F9FA;
            }}
            
            .metric-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin: 20px 0;
            }}
            
            .metric-card {{
                background: white;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            
            .metric-number {{
                font-size: 24pt;
                font-weight: bold;
                color: #2E7D32;
                margin-bottom: 5px;
            }}
            
            .metric-label {{
                font-size: 11pt;
                color: #666;
            }}
            
            ul {{
                padding-left: 25px;
            }}
            
            li {{
                margin-bottom: 8px;
            }}
            
            ol {{
                padding-left: 25px;
            }}
            
            ol li {{
                margin-bottom: 8px;
            }}
            
            .contact-info {{
                background: #E8F5E8;
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 25px;
                margin-top: 30px;
                page-break-inside: avoid;
            }}
            
            .footer {{
                text-align: center;
                color: #666;
                font-size: 10pt;
                margin-top: 40px;
                padding-top: 20px;
                border-top: 2px solid #E0E0E0;
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
            
            blockquote {{
                background: #f9f9f9;
                border-left: 4px solid #ccc;
                margin: 1.5em 10px;
                padding: 0.5em 10px;
                font-style: italic;
            }}
            
            strong {{
                color: #1976D2;
            }}
        </style>
    </head>
    <body>
        <div class="confidential-banner">
            <strong>🔒 CONFIDENTIAL PARTNERSHIP PROPOSAL</strong><br>
            Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
            Document Password: <strong>{generate_dynamic_password()}</strong>
        </div>
        
        <div class="print-instruction no-print">
            💡 <strong>For PDF conversion:</strong> Use Ctrl+P → Save as PDF in your browser
        </div>
        
        {html_content}
        
        <div class="footer">
            <p><strong>© 2025 OpenNexus - NexusOptim IA</strong></p>
            <p><em>Transforming Infrastructure Through Edge AI</em></p>
            <p>Costa Rica 🇨🇷 - Technology for LATAM • Document generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
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
    print("🏢 Generando Propuesta Schneider Electric - Versión Corporativa...")
    
    if os.path.exists('OpenNexus_SchneiderPartnership_2025.md'):
        print("📊 Procesando documento Schneider Electric...")
        html_content = schneider_markdown_to_html('OpenNexus_SchneiderPartnership_2025.md')
        
        html_filename = 'SchneiderElectric_Partnership_Proposal.html'
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        create_protected_zip(html_filename, 'SchneiderElectric_Partnership_Proposal')
        print("✅ Propuesta Schneider Electric generada exitosamente")
        
        print(f"\n📄 Archivo HTML: {html_filename}")
        print(f"🔐 Archivo ZIP: SchneiderElectric_Partnership_Proposal.zip")
        print(f"🔑 Contraseña: {generate_dynamic_password()}")
        print("\n💼 Documento listo para presentación corporativa")
        print("🎯 Optimizado para impresión profesional y conversión a PDF")
    else:
        print("❌ No se encontró el archivo OpenNexus_SchneiderPartnership_2025.md")

if __name__ == "__main__":
    main()
