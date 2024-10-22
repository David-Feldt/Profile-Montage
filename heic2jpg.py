import os
import pyheif
from PIL import Image

# Set the path to your folder containing HEIC files
source_folder = 'output2'
# Set the path where converted images will be saved
destination_folder = 'heic'

# Ensure the destination directory exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Iterate through each file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".HEIC") or filename.endswith(".heic"):
        # Full path of the HEIC file
        source_file_path = os.path.join(source_folder, filename)
        
        # Read the HEIC file
        heif_file = pyheif.read(source_file_path)
        
        # Convert HEIC to a Pillow Image object
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data, 
            "raw", 
            heif_file.mode, 
            heif_file.stride,
        )

        # Create a new filename with .jpg or .png extension
        new_filename = os.path.splitext(filename)[0] + ".jpg"  # Change to ".png" if needed
        destination_file_path = os.path.join(destination_folder, new_filename)

        # Save the image as a JPEG or PNG
        image.save(destination_file_path, "JPEG")  # Use "PNG" for saving as PNG

        print(f"Converted: {filename} -> {new_filename}")
