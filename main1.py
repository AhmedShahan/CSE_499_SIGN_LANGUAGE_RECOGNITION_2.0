
### All the glosses are in txt file

import json
file1 = open('/media/shahan/Projects/CSE499B/archive/gloss.txt','a')

# Path to the JSON file
json_file_path = '/media/shahan/Projects/CSE499B/archive/WLASL_v0.3.json'  # Replace 'file_name.json' with your actual JSON file name

i=0
total_gloss=[]
with open(json_file_path, 'r') as file:
    data = json.load(file)
    for entry in data:
        gloss=entry.get("gloss")
        total_gloss.append(gloss)

print(len(total_gloss))
# file1.write(str(total_gloss))