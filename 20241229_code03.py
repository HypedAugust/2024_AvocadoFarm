import json
import textwrap

# Specify the full path to the JSON file
file_path2 = r"C:\Users\82106\Desktop\causal_judgement.json"

# Open the JSON file and load its contents
with open(file_path2, "r") as f:  # Open the file in read mode ("r")
    data = json.load(f)  # Load the file content into a Python dictionary

# Function to process and format long strings, replacing \n with actual spaces
def process_text(json_data, wrap_length=80):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if isinstance(value, str):
                # Replace \n with spaces and wrap the text
                json_data[key] = "\n".join(textwrap.wrap(value.replace("\n", " "), wrap_length))
            elif isinstance(value, (dict, list)):
                process_text(value, wrap_length)  # Recursive processing
    elif isinstance(json_data, list):
        for index, item in enumerate(json_data):
            if isinstance(item, str):
                json_data[index] = "\n".join(textwrap.wrap(item.replace("\n", " "), wrap_length))
            elif isinstance(item, (dict, list)):
                process_text(item, wrap_length)  # Recursive processing
    return json_data

# Apply text processing to the loaded data
processed_data = process_text(data)

# Print the processed data without escaping special characters
def print_readable_json(json_data):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            print(f"{key}:")
            if isinstance(value, str):
                print(f"{value}\n")
            elif isinstance(value, (dict, list)):
                print_readable_json(value)
    elif isinstance(json_data, list):
        for item in json_data:
            print_readable_json(item)

# Print the processed data
print_readable_json(processed_data)
