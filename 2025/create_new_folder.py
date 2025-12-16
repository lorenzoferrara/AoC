import os
import shutil

#list all folders in the current directory

# set the current directory where this script is
current_directory = os.path.dirname(os.path.abspath(__file__))

folders = [f for f in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, f))]
print(folders)

# find the last folder
last_folder = max(folders) if folders else None
print("Last folder:", last_folder)

#get number removing from last folder the word day
number = int(last_folder.replace("day", "")) if last_folder else 0
next_number = number + 1

#format next number with leading zeros
new_folder_name = f"day{next_number:02d}"

# copy in new folder the content of the last folder


if last_folder:
    new_folder_path = os.path.join(current_directory, new_folder_name)
    last_folder_path = os.path.join(current_directory, last_folder)
    shutil.copytree(last_folder_path, new_folder_path)