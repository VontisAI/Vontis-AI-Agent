import pandas as pd
import json

def csv_to_json(csv_file, json_file):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert DataFrame to JSON and save it to a file
    df.to_json(json_file, orient='records', lines=True)
    return f"File converted and saved as {json_file}"

# Example usage
csv_file = 'data.csv'  # Make sure this file exists
json_file = 'data.json'
conversion_result = csv_to_json(csv_file, json_file)
print(conversion_result)
