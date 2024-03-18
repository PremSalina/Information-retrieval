import json
import re
import os

# Specify the directory where the JSON file is located
directory = "/Users/prem/Downloads/Prem_IR_Project_1/Scraped_data"

# Load the data from the "Final_Merged_Data.json" file
file_path = os.path.join(directory, "Final_Merged_Data.json")
with open(file_path, 'r') as file:
    data = json.load(file)

# Define a function to clean and extract alphanumeric characters from a text
def clean_summary(text):
    # Use regex to keep only alphanumeric characters and spaces
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text

# Iterate through the data and preprocess the "summary" part
for item in data:
    if "summary" in item:
        item["summary"] = clean_summary(item["summary"])

# Save the cleaned data to a new JSON file
output_file_path = os.path.join(directory, "cleaned_Final_Merged_Data.json.json")
with open(output_file_path, 'w') as output_file:
    json.dump(data, output_file, indent=2)

print(f"Data preprocessing complete. Cleaned data saved to {output_file_path}.")

