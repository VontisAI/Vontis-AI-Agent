import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_data(df):
    # Create a simple bar plot
    sns.barplot(x="Name", y="Age", data=df)
    plt.title('Age Distribution')
    plt.show()

# Example usage
data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 24, 35]}
df = pd.DataFrame(data)
plot_data(df)
