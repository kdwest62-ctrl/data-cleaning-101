import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
options = ['1. Print CSV',
           '2. Identify fully duplicated rows',
           '3. Remove exact duplicates',
           '4. Exit']
for item in options:
    print(item)

while True:
    option = input('Select option: ')
    if option == '1':
        print(df.to_string())
        print('-' * 8)
    elif option == '2':
        print(df.duplicated())
        print('-' * 8)
    elif option == '3':
        print(df.drop_duplicates())
        print('-' * 8)
    elif option == '4':
        print('Program closed')
        break
    else:
        print('Invalid input')
        print('-' * 8)
