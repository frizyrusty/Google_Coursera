#!/usr/bin/env python3
"""
This script processes all image files in a specified input directory by performing
the following operations:
1. Rotates the image 90 degrees counterclockwise.
2. Resizes the image to 128x128 pixels.
3. Converts the image to the RGB color mode.
4. Saves the processed image in JPEG format to an output directory.
"""

from PIL import Image
import os

# Define the input directory containing the images to be processed.
input_directory = "images/"

# Define the output directory where the processed images will be saved.
output_directory = "/opt/icons/"

# Ensure the output directory exists. Create it if it does not.
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each file in the input directory.
for filename in os.listdir(input_directory):
    # Exclude non-image files like .DS_Store (commonly found on macOS).
    if filename.endswith(".DS_Store"):
        continue

    # Open the image file.
    input_path = os.path.join(input_directory, filename)
    with Image.open(input_path) as im:
        # Apply image transformations.
        im = im.rotate(-90)  # Rotate 90 degrees counterclockwise.
        im = im.resize((128, 128))  # Resize to 128x128 pixels.
        im = im.convert("RGB")  # Convert to RGB color mode.

        # Save the processed image in the output directory with .jpeg extension.
        output_filename = filename.split('.')[0] + ".jpeg"
        output_path = os.path.join(output_directory, output_filename)
        im.save(output_path, "JPEG")

        print(f"Processed {filename} -> {output_filename}")
