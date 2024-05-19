import os
import shutil

# Definiere die Pfade für den Download- und den Dokumente-Ordner
download_folder = os.path.expanduser('~/Downloads')
documents_folder = os.path.expanduser('~/Documents')
desktop_folder = os.path.expanduser('~/Desktop')

# Erstelle eine Liste der Dateitypen, die gelöscht werden sollen
delete_extensions = ['.dmg']

# Definiere eine Zuordnung von Dateierweiterungen zu Ordnernamen
folder_mapping = {
    '.pdf': 'PDFs',
    '.docx': 'Word_Documents',
    '.xlsx': 'Excel_Sheets',
    '.jpg': 'Images',
    '.png': 'Images',
    '.zip': 'Archives',
    # Weitere Dateitypen und zugehörige Ordner können hier hinzugefügt werden
}

def cleanup_download_folder():
    # Gehe durch alle Dateien im Download-Ordner
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)

        # Überspringe, wenn es sich um ein Verzeichnis handelt
        if os.path.isdir(file_path):
            continue

        # Prüfe, ob die Datei gelöscht werden soll
        if any(filename.endswith(ext) for ext in delete_extensions):
            print(f"Lösche Datei: {filename}")
            os.remove(file_path)
        else:
            # Bestimme den Zielordner basierend auf der Dateierweiterung
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in folder_mapping:
                target_folder = os.path.join(documents_folder, folder_mapping[file_extension])
            else:
                target_folder = os.path.join(documents_folder, 'Others')
            
            # Erstelle den Zielordner, falls er noch nicht existiert
            os.makedirs(target_folder, exist_ok=True)

            # Verschiebe die Datei in den Zielordner
            new_path = os.path.join(target_folder, filename)
            print(f"Verschiebe Datei: {filename} nach {new_path}")
            shutil.move(file_path, new_path)
            
            
def cleanup_desktop_folder():
    # Gehe durch alle Dateien im Download-Ordner
    for filename in os.listdir(desktop_folder):
        file_path = os.path.join(desktop_folder, filename)

        # Überspringe, wenn es sich um ein Verzeichnis handelt
        if os.path.isdir(file_path):
            continue

        # Prüfe, ob die Datei gelöscht werden soll
        if any(filename.endswith(ext) for ext in delete_extensions):
            print(f"Lösche Datei: {filename}")
            os.remove(file_path)
        else:
            # Bestimme den Zielordner basierend auf der Dateierweiterung
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in folder_mapping:
                target_folder = os.path.join(documents_folder, folder_mapping[file_extension])
            else:
                target_folder = os.path.join(documents_folder, 'Others')
            
            # Erstelle den Zielordner, falls er noch nicht existiert
            os.makedirs(target_folder, exist_ok=True)

            # Verschiebe die Datei in den Zielordner
            new_path = os.path.join(target_folder, filename)
            print(f"Verschiebe Datei: {filename} nach {new_path}")
            shutil.move(file_path, new_path)            

if __name__ == "__main__":
    cleanup_download_folder()
    cleanup_desktop_folder()
