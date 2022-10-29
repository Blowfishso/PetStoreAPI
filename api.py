import requests
import json
# Pet
# Add new pet to the store
url = 'https://petstore.swagger.io/v2/pet'
headers = {'accept': 'application/json', 'content-type': 'application/json'}
data = {
    "id": 23,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "Гура",
    "photoUrls": [
        "string"
    ],
    "tags": [{
        "id": 0,
        "name": "string"
    }],
    "status": "available"
}

res = requests.post(url, headers=headers, data=json.dumps(data))
print('Add new pet to the store')
print(res.status_code)
print(res.json())

# Update an existing pet
url = 'https://petstore.swagger.io/v2/pet'
headers = {'accept': 'application/json', 'content-type': 'application/json'}
data = {
    "id": 23,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "Гура",
    "photoUrls": [
        "string"
    ],
    "tags": [{
        "id": 0,
        "name": "string"
    }],
    "status": "available"
}

res = requests.put(url, headers=headers, data=json.dumps(data))
print('Update an existing pet')
print(res.status_code)
print(res.json())


# Find pet by status
res = requests.get("https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'},
                   headers={'accept': 'application/json'})
print('Find pet by status')
print(res.status_code)
print(res.json())


# Find pet by id
res = requests.get(f'https://petstore.swagger.io/v2/pet/{data["id"]}')
print('Find pet by id')
print(res.status_code)
print(res.json())


# Updates a pet in a store with form data
res = requests.post(f'https://petstore.swagger.io/v2/pet/{data["id"]}')
data = {
    "id": 23,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "Gura",
    "photoUrls": [
        "string"
    ],
    "tags": [{
        "id": 0,
        "name": "string"
    }],
    "status": "sold"
}
print('Updates a pet in a store with form data')
print(res.status_code)
print(res.json())


# Uploads an image
res = image = 'gura.jpg'
files = {'file': (image, open(image, 'rb'), 'image/jpeg')}
res = requests.post(f'https://petstore.swagger.io/v2/pet/{data["id"]}/uploadImage', headers={'accept': 'application/json'}, files=files)
print('Uploads an image')
print(res.status_code)
print(res.json())



# # Deletes pet
res = requests.delete(f'https://petstore.swagger.io/v2/pet/{data["id"]}')
print('Deletes pet')
print(res.status_code)
print(res.json())

# store
# Place an order for a pet
data = {
  "id": 5,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2022-10-28T08:45:38.992Z",
  "status": "placed",
  "complete": True
}

header = {'accept': 'application/json', 'Content-Type': 'application/json'}

res = requests.post(f'https://petstore.swagger.io/v2/store/order', headers=header, data=json.dumps(data))
print('Place an order for a pet')
print(res.status_code)
print(res.json())


# Find purchase order by ID
res = requests.get(f'https://petstore.swagger.io/v2/store/order/{data["id"]}', headers=header)
print('Find purchase order by ID')
print(res.status_code)
print(res.json())


# Delete purchase order by ID
res = requests.delete(f'https://petstore.swagger.io/v2/store/order/{data["id"]}', headers=header)
print('Delete purchase order by ID')
print(res.status_code)
print(res.json())


# Returns pet inventories by status
res = requests.get(f'https://petstore.swagger.io/v2/store/inventory', headers=header)
print('Returns pet inventories by status ')
print(res.status_code)
print(res.json())


# User
# Creates list of users with given input array
data = [
  {
    "id": 34,
    "username": "blowf",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
]

res = requests.post(url='https://petstore.swagger.io/v2/user/createWithArray', headers=header, data=json.dumps(data))
print('Creates list of users with given input array')
print(res.status_code)
print(res.json())


# Creates list of users with given input array
data = [
  {
    "id": 34,
    "username": "blowf",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
]

res = requests.post(url='https://petstore.swagger.io/v2/user/createWithList', headers=header, data=json.dumps(data))
print('Creates list of users with given input array')
print(res.status_code)
print(res.json())


# Get user by username
res = requests.get(f'https://petstore.swagger.io/v2/user/{data[0]["username"]}')
print('Get user by username')
print(res.status_code)
print(res.json())


# Updated user
data = {
  "id": 34,
  "username": "blowf",
  "firstName": "Greg",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}
res = requests.put(url=f'https://petstore.swagger.io/v2/user/{data["username"]}', headers=header, data=json.dumps(data))
print('Updated user')
print(res.status_code)
print(res.json())


# Delete user
res = requests.delete(f'https://petstore.swagger.io/v2/user/{data["username"]}')
print('Delete user')
print(res.status_code)
print(res.json())


# Create user
data = {
  "id": 34,
  "username": "blowf",
  "firstName": "Greg",
  "lastName": "string",
  "email": "string",
  "password": "blowf",
  "phone": "string",
  "userStatus": 0
}

res = requests.post(url='https://petstore.swagger.io/v2/user', headers=header, data=json.dumps(data))
print('Create user')
print(res.status_code)
print(res.json())


# Logs user into the system
res = requests.get(f'https://petstore.swagger.io/v2/user/login?username={data["username"]}&password={data["password"]}')
print('Logs user into the system')
print(res.status_code)
print(res.json())


# Logs out current logged in user session
res = requests.get('https://petstore.swagger.io/v2/user/logout')
print('Logs out current logged in user session')
print(res.status_code)
print(res.json())