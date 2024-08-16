# Image Analysis Project

Este proyecto permite analizar metadatos de imágenes utilizando ExifTool y Python.

## Estructura del Proyecto

- `analyze.py`: Script principal para analizar imágenes y generar reportes.
- `exiftool.py`: Módulo para manejar la interacción con ExifTool.
- `gui.py`: Script para la interfaz gráfica de usuario utilizando `tkinter`.
- `reports/`: Carpeta para almacenar los reportes generados en formato CSV y HTML.
- `images/`: Carpeta que contiene las imágenes a ser analizadas.
- `imgs_interfaz_grafica/`: Carpeta que contiene las imágenes a ser analizadas para probar la interfaz grafica 
- `requirements.txt`: Archivo que lista las dependencias del proyecto.
- `README.md`: Información del proyecto y cómo utilizarlo.

## Uso

### Análisis de Imágenes

Ejecuta el script `analyze.py` para analizar una carpeta de imágenes y generar reportes en CSV y HTML.

Ejecuta el script `gui.py` para seleccionar cualquier carpeta detro de tu computador que contengan imagenes y poder analizarlas.

```bash
python analyze.py
