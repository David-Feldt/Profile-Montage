import os
from datetime import datetime
import shutil  # To move the files to a different directory

# Set the path to your source directory (where the original files are)
source_folder = 'Mega'

# Set the path to your destination directory (where renamed files will go)
destination_folder = 'output2'

# Ensure the destination directory exists, create it if it doesn't
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Iterate through each file in the source folder
for filename in os.listdir(source_folder):
    # Get the full path to the file in the source folder
    source_file_path = os.path.join(source_folder, filename)
    
    # Check if it's a file (and not a directory)
    if os.path.isfile(source_file_path):
        # Get the file's last modification time (in seconds since the epoch)
        mod_time = os.path.getmtime(source_file_path)
        
        # Convert the modification time to a readable format (e.g., YYYY-MM-DD_HH-MM-SS)
        mod_time_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d_%H-%M-%S')
        
        # Get the file extension (e.g., .jpg, .txt)
        file_extension = os.path.splitext(filename)[1]
        
        # Construct the new filename using the modification date and original file extension
        new_filename = f'{mod_time_str}{file_extension}'
        
        # Get the full path for the new filename in the destination directory
        destination_file_path = os.path.join(destination_folder, new_filename)
        
        # Move (or copy) the file to the destination folder with the new name
        shutil.copy(source_file_path, destination_file_path)
        print(f'Moved: {filename} -> {new_filename}')
