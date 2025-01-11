import os

def upload_file(file_path, destination_folder):
    # Check if the file exists
    if os.path.exists(file_path):
        # Move the file to the destination folder
        file_name = os.path.basename(file_path)
        destination = os.path.join(destination_folder, file_name)
        os.rename(file_path, destination)
        return f"File successfully uploaded to {destination}"
    return "File not found."

# Example usage
result = upload_file('test.txt', '/path/to/destination')
print(result)
