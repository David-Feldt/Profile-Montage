import cv2
import os

# Set the path to your source directory (where the original files are)
source_folder = 'heic'
# Set the path to your destination directory (where centered images will go)
destination_folder = 'output3'

# Ensure the destination directory exists, create it if it doesn't
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Function to crop the image to a specific size around its center
def crop_center(img, cropx, cropy):
    y, x, _ = img.shape
    startx = x // 2 - (cropx // 2)
    starty = y // 2 - (cropy // 2)    
    return img[starty:starty + cropy, startx:startx + cropx]

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

        # Crop to the center with a predefined size (you can adjust the crop size)
        crop_width = 512  # Desired crop width
        crop_height = 512  # Desired crop height

        # If the image is smaller than the crop size, resize it first
        if img.shape[1] < crop_width or img.shape[0] < crop_height:
            img = cv2.resize(img, (crop_width, crop_height), interpolation=cv2.INTER_AREA)

        # Center crop the image
        cropped_img = crop_center(img, crop_width, crop_height)

        # Save the centered and cropped image
        output_file_path = os.path.join(destination_folder, filename)
        cv2.imwrite(output_file_path, cropped_img)
        print(f'Cropped and saved: {filename}')
