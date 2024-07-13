import json

import requests

def createObject():
   url = "https://api.restful-api.dev/objects"

   headers = {
       'content-type': 'application/json'
   }

   data =  {
        "name": "Dinesh Test",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

   response = requests.post(url, data=json.dumps(data), headers = headers)

   if response.status_code != 200:
        print("Error in creating object")

   return response

def getAllObjects():

    url = "https://api.restful-api.dev/objects"
    response = requests.get(url)
    return response.json()

def getObjectById(id):

    url = "https://api.restful-api.dev/objects/" + id
    response = requests.get(url)
    return response.json()
def put(id):
   url = "https://api.restful-api.dev/objects/"+id

   headers = {
       'content-type': 'application/json'
   }   

   data =  {
        "name": "Dinesh Test1",
        "data": {
            "year": 20,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

   response = requests.put(url, data=json.dumps(data), headers = headers)

   if response.status_code != 200:
        print("Error in creating object")

   return response.json()


def dell(id):
    url = "https://api.restful-api.dev/objects/"+id
    response = requests.delete(url)
    return response.json()

response = createObject().json()
id = response['id']
print("id ",id)
print("create response ",createObject().json())
print("get response ",getAllObjects())
print("get response ",getObjectById(id))
print("put method:",put(id))
print("\n deleted:",dell(id))