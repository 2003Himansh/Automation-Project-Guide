import os
import shutil
from datetime import datetime
import logging


class FileOrganizer:

    def __init__(self, watch_folder, organized_folder):

        self.watch_folder = watch_folder
        self.organized_folder = organized_folder

        self.categories = {
            "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
            "Images": [".jpg", ".png", ".jpeg"],
            "Videos": [".mp4", ".avi"],
            "Music": [".mp3", ".wav"],
            "Code": [".py", ".js", ".html"],
            "Archives": [".zip", ".rar"]
        }

        logging.basicConfig(
            filename="logs/file_organizer.log",
            level=logging.INFO,
            format="%(asctime)s - %(message)s"
        )

    def create_folders(self):

        os.makedirs(self.organized_folder, exist_ok=True)

        for category in self.categories:
            os.makedirs(os.path.join(self.organized_folder, category), exist_ok=True)

        os.makedirs(os.path.join(self.organized_folder, "Others"), exist_ok=True)

    def organize(self):

        self.create_folders()

        for file in os.listdir(self.watch_folder):

            file_path = os.path.join(self.watch_folder, file)

            if os.path.isfile(file_path):

                ext = os.path.splitext(file)[1].lower()

                moved = False

                for category, extensions in self.categories.items():

                    if ext in extensions:

                        dest_folder = os.path.join(self.organized_folder, category)
                        dest_path = os.path.join(dest_folder, file)

                        if os.path.exists(dest_path):
                            name, ext = os.path.splitext(file)
                            new_name = name + "_" + datetime.now().strftime("%H%M%S") + ext
                            dest_path = os.path.join(dest_folder, new_name)

                        shutil.move(file_path, dest_path)

                        logging.info(f"{file} moved to {category}")
                        print(f"{file} moved to {category}")

                        moved = True
                        break

                if not moved:

                    dest_folder = os.path.join(self.organized_folder, "Others")

                    shutil.move(file_path, os.path.join(dest_folder, file))

                    logging.info(f"{file} moved to Others")
                    print(f"{file} moved to Others")