import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
print('1. Print CSV\n2. Count Missing Values (Column)\n3. Exit')
while True:
    option = input('Select option: ')
    if option == '1':
        print(df.to_string())
        print('-' * 8)
    elif option == '2':
        output = df.isnull().sum()
        print(output)
        print('-' * 8)
    elif option == '3':
        print('Program closed')
        break
    else:
        print('Invalid input')
