import pandas as pd

# Load the CSV file
df = pd.read_csv('/Users/nethann/Downloads/Programming/Python/CS2/survey.csv')

# Display the first few rows of the dataframe
print(df.columns)




age_median = df['What is your age?'].mean()
print(age_median)