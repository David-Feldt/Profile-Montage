import cv2
import os

# Directory containing your selfies
input_dir = 'Mega/'
output_dir = 'output/'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the face detection model (Haar Cascades)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Loop through each image
for img_name in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_name)
    img = cv2.imread(img_path)

    if img is None:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        # Get the first detected face
        (x, y, w, h) = faces[0]

        # Calculate the center of the face
        face_center_x = x + w // 2
        face_center_y = y + h // 2

        # Crop the image around the face
        crop_size = min(img.shape[0], img.shape[1])  # Make sure it's square
        start_x = max(0, face_center_x - crop_size // 2)
        start_y = max(0, face_center_y - crop_size // 2)

        cropped_img = img[start_y:start_y + crop_size, start_x:start_x + crop_size]

        # Resize the cropped image to a consistent size (optional, e.g., 512x512)
        final_img = cv2.resize(cropped_img, (512, 512))

        # Save the centered image
        cv2.imwrite(os.path.join(output_dir, img_name), final_img)

    else:
        # If no face is detected, just copy the image
        cv2.imwrite(os.path.join(output_dir, img_name), img)

print("Images have been centered and saved to:", output_dir)
