import tkinter as tk
from tkinter import filedialog
from exiftool import extract_metadata
import os

def parse_metadata(metadata_raw):
    metadata = {}
    for line in metadata_raw.split('\n'):
        if line.strip() == '':
            continue
        key_value = line.split(':', 1)
        if len(key_value) == 2:
            key, value = key_value
            metadata[key.strip()] = value.strip()
    return metadata

def analyze_image(image_path, text_widget):
    if os.path.exists(image_path):
        text_widget.insert(tk.END, f"Analizando la imagen: {image_path}\n")
        metadata_raw = extract_metadata(image_path)
        metadata = parse_metadata(metadata_raw)
        for key, value in metadata.items():
            text_widget.insert(tk.END, f"{key}: {value}\n")
    else:
        text_widget.insert(tk.END, f"El archivo {image_path} no existe.\n")

def analyze_folder(folder_path, text_widget):
    text_widget.delete(1.0, tk.END)  # Limpiar el área de texto antes de iniciar el análisis
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            analyze_image(file_path, text_widget)

def open_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        analyze_folder(folder_path, text_widget)

def clear_results():
    text_widget.delete(1.0, tk.END)

# Interfaz gráfica
root = tk.Tk()
root.title("Análisis de Imágenes")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

btn_open_folder = tk.Button(frame, text="Seleccionar Carpeta", command=open_folder)
btn_open_folder.pack(side=tk.LEFT, padx=5)

btn_clear_results = tk.Button(frame, text="Limpiar Resultados", command=clear_results)
btn_clear_results.pack(side=tk.LEFT, padx=5)

text_widget = tk.Text(frame, wrap=tk.WORD, width=80, height=20)
text_widget.pack()

root.mainloop()
