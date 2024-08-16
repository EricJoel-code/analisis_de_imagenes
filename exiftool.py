import subprocess

EXIFTOOL_PATH = r"C:\ExifTool\exiftool.exe"

def extract_metadata(image_path):
    result = subprocess.run([EXIFTOOL_PATH, image_path], capture_output=True, text=True)
    return result.stdout
