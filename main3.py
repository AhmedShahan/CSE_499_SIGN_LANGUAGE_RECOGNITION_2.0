### Gloss wise video id extraction in a folder

import json
file1 = open('/media/shahan/Projects/CSE499B/archive/glosswiseVideo.txt','a')

# Path to the JSON file
json_file_path = '/media/shahan/Projects/CSE499B/archive/WLASL_v0.3.json'  # Replace 'file_name.json' with your actual JSON file name

gloss_video_ids = {}  # Dictionary to store video IDs for each gloss

# Iterate through JSON data
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
    for entry in data:
        gloss = entry.get("gloss")
        instances = entry.get("instances", [])
        for instance in instances:
            video_id = instance.get("video_id")
            if gloss not in gloss_video_ids:
                gloss_video_ids[gloss] = [video_id]
            else:
                gloss_video_ids[gloss].append(video_id)

# Print or use the gloss_video_ids dictionary as needed
for gloss, video_ids in gloss_video_ids.items():
    print(f"Gloss: {gloss}, Video IDs: {video_ids}")


import os
import shutil

# Function to create folders for glosses and move videos
source_folder= '/media/shahan/Projects/CSE499B/archive/videos'
destination_video_path= '/media/shahan/Projects/CSE499B/archive/videoFolder'
def create_folders_and_move_videos(gloss_video_ids, source_folder):
    for gloss, video_ids in gloss_video_ids.items():
        gloss_folder = os.path.join(source_folder, gloss)
        os.makedirs(gloss_folder, exist_ok=True)
        for video_id in video_ids:
            source_video_path = os.path.join(source_folder, f"{video_id}.mp4")
            if os.path.exists(source_video_path):
                destination_video_path = os.path.join(gloss_folder, f"{video_id}.mp4")
                shutil.move(source_video_path, destination_video_path)

# Specify the path to the folder containing all videos

# Call the function to create folders and move videos
create_folders_and_move_videos(gloss_video_ids, source_folder)
