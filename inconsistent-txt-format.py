import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
print('Tasks')
tasks = ['1. Print CSV',
         '2. Standardize [first_name] and [last_name] to title case',
         '3. Standardize [department] to title case',
         '4. Lowercase all emails',
         '5. Strip any leading/trailing whitespace',
         '6. Exit']
for item in tasks:
    print(item)
while True:
    task = input('Select task: ')
    if task == '1':
        choice = input('(f) full or (t) truncated: ')
        if choice == 'f':
            print(df.to_string())
            print('-' * 8)
        elif choice == 't':
            print(df)
            print('-' * 8)
        else:
            print('Invalid input')
    elif task == '2':
        df['first_name'] = df['first_name'].str.title()
        df['last_name'] = df['last_name'].str.title()
        print('Task complete')
        print('-' * 8)
    elif task == '3':
        df['department'] = df['department'].str.title()
        print('Task complete')
        print('-' * 8)
    elif task == '4':
        df['email'] = df['email'].str.lower()
        print('Task complete')
        print('-' * 8)
    elif task == '5':
        pass
    elif task == '6':
        print('Program closed')
        break
    else:
        print('Invalid input')
