import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
options = ['1. Print CSV',
           '2. Count missing values per column',
           '3. Fill missing values in [email] with "n/a"',
           '4. Fill missing values in [age] with the median',
           '5. Fill missing values in [city] with "Unknown"',
           '6. Drop rows where [signup_date] is missing',
           '7. Exit']
for item in options:
    print(item)

while True:
    option = input('Select option: ')
    if option == '1':
        print(df.to_string())
        print('-' * 8)
    elif option == '2':
        output = df.isnull().sum()
        print(output.to_string())
        print('-' * 8)
    elif option == '3':
        output = df['email'].fillna('n/a')
        print(output.to_string())
        print('-' * 8)
    elif option == '4':
        output = df['age'].fillna(df['age'].median())
        print(output.to_string())
        print('-' * 8)
    elif option == '5':
        output = df['city'].fillna('Unknown')
        print(output.to_string())
        print('-' * 8)
    elif option == '7':
        print('Program closed')
        break
    else:
        print('Invalid input')
