import os
import csv
from exiftool import extract_metadata

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

def save_metadata_to_csv(metadata, output_file):
    with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in metadata.items():
            writer.writerow([key, value])

def save_metadata_to_html(metadata, output_file):
    with open(output_file, 'a', encoding='utf-8') as htmlfile:
        htmlfile.write("<table border='1'>")
        for key, value in metadata.items():
            htmlfile.write(f"<tr><td>{key}</td><td>{value}</td></tr>")
        htmlfile.write("</table><br><br>")

def analyze_image(image_path, output_file_csv, output_file_html):
    if os.path.exists(image_path):
        print(f"Analizando la imagen: {image_path}\n")
        metadata_raw = extract_metadata(image_path)
        metadata = parse_metadata(metadata_raw)
        save_metadata_to_csv(metadata, output_file_csv)
        save_metadata_to_html(metadata, output_file_html)
    else:
        print(f"El archivo {image_path} no existe.")

def analyze_folder(folder_path, output_file_csv, output_file_html):
    # Inicializar los archivos de salida
    with open(output_file_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Key', 'Value'])
    with open(output_file_html, 'w', encoding='utf-8') as htmlfile:
        htmlfile.write("<html><body>")
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            analyze_image(file_path, output_file_csv, output_file_html)
    with open(output_file_html, 'a', encoding='utf-8') as htmlfile:
        htmlfile.write("</body></html>")

if __name__ == "__main__":
    folder_path = r"C:\Users\Joel-Nayde\Documents\Joel\Ciberseguridad\image_analysis_project\images"
    output_file_csv = r"C:\Users\Joel-Nayde\Documents\Joel\Ciberseguridad\image_analysis_project\reports\metadata_report.csv"
    output_file_html = r"C:\Users\Joel-Nayde\Documents\Joel\Ciberseguridad\image_analysis_project\reports\metadata_report.html"
    analyze_folder(folder_path, output_file_csv, output_file_html)
