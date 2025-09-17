import pandas as pd

#File path
archive = 'SQLPython\\Pandas\\pandasexample.txt'

# Read dataframe
df = pd.read_csv(archive, header=None, names=['ID', 'Name', 'Surname', "Address", "Age"])

# Show dataframe
print(df.to_string(index=False))
print(pd.DataFrame(df))