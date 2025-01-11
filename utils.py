import pandas as pd

# Sample data for analysis
data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 24, 35]}
df = pd.DataFrame(data)

# Simple statistical analysis
def analyze_data():
    return df.describe()
