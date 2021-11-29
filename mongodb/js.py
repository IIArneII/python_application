import requests

choice = -1
while choice != 0:
    choice = int(input('\n1. Get\n2. Post\n3. Put\n4. Delete\n0. Выход\n'))
    if choice == 1:
        userName = input('userName (/ для всех пользователей): ')
        if userName == '/':
            r = requests.get('http://localhost:3000/')
        else:
            r = requests.get('http://localhost:3000/?userName=' + userName)
        if r.status_code == 200:
            print(r.json())
        else:
            print('Не найдено')

    if choice == 2:
        userName = input('userName: ')
        userEmail = input('userEmail: ')
        r = requests.post('http://localhost:3000/', data={'userName': userName, "userEmail": userEmail})
        if r.status_code == 200:
            print(r.json())
        else:
            print('Пользователь уже существует')

    if choice == 3:
        userName = input('userName: ')
        newUserName = input('newUserName: ')
        newUserEmail = input('newUserEmail: ')
        r = requests.put('http://localhost:3000/',
                          data={'userName': userName, "newUserEmail": newUserEmail, "newUserName": newUserName})
        if r.status_code == 200:
            print(r.json())
        else:
            print('Не найдено')

    if choice == 4:
        userName = input('userName: ')
        r = requests.delete('http://localhost:3000/?userName=' + userName)
        if r.status_code == 200:
            print(r.json())
        else:
            print('Не найдено')
