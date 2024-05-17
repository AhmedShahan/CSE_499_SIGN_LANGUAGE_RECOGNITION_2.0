### Gloss wise video id extraction
import time
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
glose_video=[]
for gloss, video_ids in gloss_video_ids.items():
    string= "Gloss: "+str(gloss)+ " Video IDs: "+str(video_ids)+"\n"
    # print(f"Gloss: {gloss}, Video IDs: {video_ids}")
    print(string)
    time.sleep(5)
    glose_video.append(string)


# file1.write(str(glose_video))
