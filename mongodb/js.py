import requests

#r = requests.put('http://localhost:3000/',
#                data={'userName': 'arne', 'newUserName': 'arne', 'newUserEmail': 'ddd@rrrr'})
r = requests.get('http://localhost:3000/', data={"userName": "1", "userEmail": "1@1"})
if r.status_code == 200:
    print(r.json())
else:
    print('Не найдено')
