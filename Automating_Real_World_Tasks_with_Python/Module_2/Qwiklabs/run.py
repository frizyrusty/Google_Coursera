#! /usr/bin/env python3
"""
This script reads feedback data stored in text files within a specified directory.
Each text file contains feedback details in a structured format, and the script:
1. Extracts the data from each file.
2. Converts the data into a dictionary with predefined keys: title, name, date, and feedback.
3. Sends the feedback data to a web server using an HTTP POST request.

The script also provides debug information by printing the feedback data and server response.
"""

import os
import requests

# Define the directory containing feedback files.
feedback_directory = "/data/feedback/"

# Define the keys used to structure feedback data from the text files.
keys = ["title", "name", "date", "feedback"]

# List all files in the feedback directory.
feedback_files = os.listdir(feedback_directory)

# Process each feedback file.
for feedback_file in feedback_files:
    feedback_data = {}  # Dictionary to hold the feedback data.

    # Open and read the content of the feedback file.
    file_path = os.path.join(feedback_directory, feedback_file)
    with open(file_path, "r") as file:
        for index, line in enumerate(file):
            # Strip whitespace and map the content to the corresponding key.
            feedback_data[keys[index]] = line.strip()

    # Print the feedback data for debugging purposes.
    print("Feedback data to be sent:", feedback_data)

    # Send the feedback data to the web server.
    response = requests.post("http://<Change to your lab IP Address>/feedback/", json=feedback_data)

    # Print the response body and status code for debugging.
    print("Request body:", response.request.body)
    print("Response status code:", response.status_code)

