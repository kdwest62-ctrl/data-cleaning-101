import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
options = ['1. Print CSV',
           '2. Identify fully duplicated rows',
           '3. Remove exact duplicates',
           '4. Check for duplicates based on [order_id] only',
           '5. Verify final row count',
           '6. Exit']
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
        new_df = df.drop_duplicates(subset=['order_id'])
        print(new_df)
        print('-' * 8)
    elif option == '5':
        new_df = df.drop_duplicates()
        print(new_df)
        print(f'Final row count: {len(new_df)}')
        print('-' * 8)
    elif option == '6':
        print('Program closed')
        break
    else:
        print('Invalid input')
        print('-' * 8)
