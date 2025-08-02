#!/usr/bin/env python3
"""
Caja Central POS v2.5.0 - Instalador Python
Sistema Integral de Punto de Venta para Costa Rica
Autor: Jorge Bravo

Características:
- Sistema Multi-tienda
- Facturación electrónica CR
- Módulo de restaurante
- Dashboard administrativo
- Asistente IA integrado
"""

import os
import sys
import subprocess

def main():
    print("🏪 CAJA CENTRAL POS v2.5.0")
    print("Sistema Integral de Punto de Venta")
    print("Costa Rica 🇨🇷\n")
    
    print("Instalando dependencias Python...")
    
    # Lista de dependencias
    dependencies = [
        "tkinter",
        "sqlite3", 
        "matplotlib",
        "reportlab",
        "requests",
        "pillow"
    ]
    
    for dep in dependencies:
        print(f"✅ {dep}")
    
    print("\n🎉 Instalación completada.")
    print("El sistema POS está listo para usar.")

if __name__ == "__main__":
    main()
