### How many mp4 files

import os
def count_avi_files(directory):
    avi_count = 0

    # Iterate over all the items in the directory
    for item in os.listdir(directory):
        # Get the full path of the item
        item_path = os.path.join(directory, item) 
        # If it's a directory, recursively call count_avi_files
        if os.path.isdir(item_path):
            avi_count += count_avi_files(item_path)
        # If it's a file and ends with '.avi', increment avi_count
        elif os.path.isfile(item_path) and item.endswith('.mp4'):
            avi_count += 1
    return avi_count
# Specify the directory you want to start from
directory_to_start = '/media/shahan/Projects/CSE499B/archive/videos'

# Call the function to count .avi files recursively
avi_count = count_avi_files(directory_to_start)
print(f"Total .avi files: {avi_count}")


