import json

import requests
#1 запрос
r = requests.get(f'https://petstore.swagger.io/v2/store/inventory')
print(r.json())



#2 запрос
data = {
    "id": 0,
    "username": "vvvv",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}
headers = {
    "Content-Type": "application/json"
}

r1 = requests.post(f'https://petstore.swagger.io/v2/user', data=json.dumps(data), headers=headers)
print(r1.json())



#3 запрос

r3 = requests.delete(f'https://petstore.swagger.io/v2/user/vvvv')
print(r3.json())

#4 запрос

data = {"username": "vvv876v"}

r4 = requests.put(f'https://petstore.swagger.io/v2/user/vvvv', data=json.dumps(data))
print(r1.json())

#test
rtr=requests.get(f'https://petstore.swagger.io/v2/user/vvvv')
print(rtr)