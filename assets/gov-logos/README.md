# Logos de Entidades Gubernamentales de Costa Rica

Esta carpeta debe contener los logos oficiales de las siguientes entidades gubernamentales costarricenses que aparecen en la sección NexusOptimIA de la infografía:

## Logos Requeridos:

### 1. ICE (Instituto Costarricense de Electricidad)
- **Archivo:** `ice-logo.png`
- **Descripción:** Logo oficial del ICE
- **Uso:** Sección de optimización eléctrica
- **Dimensiones recomendadas:** 256x256px (transparent background)

### 2. AyA (Acueductos y Alcantarillados)
- **Archivo:** `aya-logo.png`
- **Descripción:** Logo oficial de AyA
- **Uso:** Sección de gestión hídrica
- **Dimensiones recomendadas:** 256x256px (transparent background)

### 3. MINAE (Ministerio de Ambiente y Energía)
- **Archivo:** `minae-logo.png`
- **Descripción:** Logo oficial del MINAE
- **Uso:** Sección de calidad del aire y ambiente
- **Dimensiones recomendadas:** 256x256px (transparent background)

### 4. MOPT (Ministerio de Obras Públicas y Transportes)
- **Archivo:** `mopt-logo.png`
- **Descripción:** Logo oficial del MOPT
- **Uso:** Sección de optimización de tráfico
- **Dimensiones recomendadas:** 256x256px (transparent background)

### 5. SENASA (Servicio Nacional de Sanidad Animal)
- **Archivo:** `senasa-logo.png`
- **Descripción:** Logo oficial de SENASA
- **Uso:** Sección de agricultura inteligente
- **Dimensiones recomendadas:** 256x256px (transparent background)

## Notas Importantes:

1. **Derechos de autor:** Todos los logos son propiedad de sus respectivas entidades gubernamentales
2. **Uso educativo:** Estos logos se utilizan únicamente con fines educativos y de demostración
3. **Formato:** Preferiblemente PNG con fondo transparente
4. **Calidad:** Logos de alta resolución para mejor presentación
5. **Fallback:** Si un logo no se puede cargar, se mostrará un icono emoji como respaldo

## Cómo obtener los logos:

- Visitar los sitios web oficiales de cada entidad
- Contactar directamente a las oficinas de comunicación
- Usar versiones de dominio público si están disponibles

## Implementación:

Los logos se implementan con un sistema de fallback usando `onerror` que muestra un emoji si el logo no se puede cargar:

```html
<img src="assets/gov-logos/[entity]-logo.png" alt="[Entity] Logo" 
     class="w-8 h-8 object-contain" 
     onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
<span class="text-2xl hidden">[emoji]</span>
```

---
**Autor:** Jorge Eduardo Bravo Chaves  
**Proyecto:** OpenNexus Infografía  
**Fecha:** 2025
