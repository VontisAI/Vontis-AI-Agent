import pandas as pd

def clean_data(dataframe):
    # Fill missing values with the mean of the column
    dataframe.fillna(dataframe.mean(), inplace=True)
    
    # Convert all string columns to lowercase
    for column in dataframe.select_dtypes(include=['object']).columns:
        dataframe[column] = dataframe[column].str.lower()

    # Return the cleaned dataframe
    return dataframe

# Example usage
data = {'Name': ['John', 'Anna', None], 'Age': [28, 24, 30]}
df = pd.DataFrame(data)
cleaned_df = clean_data(df)
