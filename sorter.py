import os
from datetime import datetime

DOWNLOAD_DIR = r"YOUR_DOWNLOAD_FOLDER"
LOG_FILE = r"LOG_FOLDER"
RULES = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mpeg", ".mov"],
    "Files": [".zip", ".rar", ".exe"]
}

def sort_and_log():
    """
    Sorts files in a directory acording to type/extension and logs the changes.

    """
    log = []

    for file in os.listdir(DOWNLOAD_DIR):
        file_extension = os.path.splitext(file)[1]

        for folder, extensions in RULES.items():
            if file_extension in extensions:
                source = os.path.join(DOWNLOAD_DIR, file)
                destination_folder = os.path.join(DOWNLOAD_DIR, folder)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                destination = os.path.join(destination_folder, file)

                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination):
                    file = f"{base}_{counter}{ext}"
                    destination = os.path.join(destination_folder, file)
                    counter += 1

                os.rename(source, destination)

                log_entry = {
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'filename': file,
                    'new_location': destination,
                }
                log.append(log_entry)
                break

    with open(LOG_FILE, 'w') as file:
        for entry in log:
            file.write(f"{entry['timestamp']} - {entry['filename']} moved to {entry['new_location']}\n")


if __name__ == "__main__":
    sort_and_log()
