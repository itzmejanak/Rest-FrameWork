import requests
import json

# URL = "http://127.0.0.1:8000/data/"

# # req = requests.get(url=URL)

# # datas = req.json()
# # print(datas)

# URL = "http://127.0.0.1:8000/register/"

# data = {
#     "name": "janak",
#     "email": "janak@gmail.com",
#     "city": "Pokhara"
# }

# j_data = json.dumps(data)
# req = requests.post(url=URL, data = j_data)

# fdatas = req.json()
# print(fdatas)


def getData(id=None):
    URL = "http://127.0.0.1:8000/student-api/"
    data = {'id':id}
    j_data = json.dumps(data)
    res = requests.get(url=URL, data = j_data)
    r_data = res.json()
    print(r_data)

# getData(1)

def createData():
    URL = "http://127.0.0.1:8000/student-api/"
    datas = {
        'name':"Sita",
        'roll_no':'18',
        'city':'Nepalgunj',
        'stats': 'Yes'
    }
    j_data = json.dumps(datas)
    res = requests.post(url=URL, data = j_data)
    r_data = res.json()
    print(r_data)

# createData()


def updateData():
    URL = "http://127.0.0.1:8000/student-api/"
    datas = {
        'name':"Sita",
        'city':'RameChap',
        'stats': 'No'
    }
    j_data = json.dumps(datas)
    res = requests.put(url=URL, data = j_data)
    r_data = res.json()
    print(r_data)

# updateData()


def deleteData():
    URL = "http://127.0.0.1:8000/student-api/"
    datas = {
        'name':"Sita",
    }
    j_data = json.dumps(datas)
    res = requests.delete(url=URL, data = j_data)
    r_data = res.json()
    print(r_data)

deleteData()