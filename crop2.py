import cv2
import os

# Set the path to your source directory (where the original files are)
source_folder = 'heic'
# Set the path to your destination directory (where centered images will go)
destination_folder = 'output-crop'

# Ensure the destination directory exists, create it if it doesn't
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Function to crop the image to a centered square
def crop_center_square(img):
    y, x, _ = img.shape
    min_side = min(x, y)
    startx = (x - min_side) // 2
    starty = (y - min_side) // 2
    return img[starty:starty + min_side, startx:startx + min_side]

# Iterate through each file in the source folder
for filename in os.listdir(source_folder):
    # Get the full path to the file in the source folder
    source_file_path = os.path.join(source_folder, filename)

    # Check if it's a file (and not a directory)
    if os.path.isfile(source_file_path):
        # Read the image using OpenCV
        img = cv2.imread(source_file_path)

        if img is None:
            print(f"Skipping {filename}, not a valid image.")
            continue

        # Crop to the center square
        cropped_img = crop_center_square(img)

        # Resize the cropped image to 512x512
        resized_img = cv2.resize(cropped_img, (512, 512), interpolation=cv2.INTER_AREA)

        # Save the centered and resized image
        output_file_path = os.path.join(destination_folder, filename)
        cv2.imwrite(output_file_path, resized_img)
        print(f'Cropped, resized, and saved: {filename}')
