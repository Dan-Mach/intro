#!/usr/bin/env python3

import os
import shutil

flash_drive_path = "/media/username/DIMAR"
destination_folder = "/home/username/Documents/codingC"
def copy_files(source, destination):
    try:
        for item in os.listdir(source):
            source_item = os.path.join(source, item)
            if os.path.isdir(source_item):
                shutil.copytree(source_item, os.path.join(destination, item))
            else:
                shutil.copy2(source_item, destination)
        print("Files copied successfully.")
    except Exception as e:
        print(f"Error: {e}")

if os.path.exists(flash_drive_path):
    copy_files(flash_drive_path, destination_folder)
else:
    print("Flash drive not detected.")
