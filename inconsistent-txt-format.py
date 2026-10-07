import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
tasks = ['1. Print CSV',
         '2. Standardize [first_name] and [last_name] to title case',
         '3. Standardize [department] to title case',
         '4. Lowercase all emails',
         '5. Exit']
for item in tasks:
    print(item)
while True:
    task = input('Select task: ')
    if task == '1':
        print(df)
    elif task == '5':
        print('Program closed')
        break
    else:
        print('Invalid input')
