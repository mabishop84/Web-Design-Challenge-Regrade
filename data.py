import pandas as pd

# Read the csv file in
data = pd.read_csv('cities.csv')

# Save to file
data.to_html('data.html', index=False)

# Assign to string
table = data.to_html()
print(table)