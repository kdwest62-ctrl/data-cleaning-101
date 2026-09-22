import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
options = ['1. Print CSV',
           '2. Identify fully duplicated rows',
           '3. Remove exact duplicates',
           '4. Exit']
for item in options:
    print(item)
