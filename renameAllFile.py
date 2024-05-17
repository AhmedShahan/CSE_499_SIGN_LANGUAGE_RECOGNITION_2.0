import os

# Directory path
directory = "/media/shahan/Projects/CSE499B/archive/videos/POC_10_Class/across"

# List all files in the directory
files = os.listdir(directory)

# Filter only .mp4 files
mp4_files = [file for file in files if file.endswith(".mp4")]

# Sort the files alphabetically
mp4_files.sort()

# Rename each file sequentially
for index, file in enumerate(mp4_files, start=1):
    new_filename = f"{index}.mp4"
    os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))
