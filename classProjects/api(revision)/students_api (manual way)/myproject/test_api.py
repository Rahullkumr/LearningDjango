import requests
import json

URL = 'http://127.0.0.1:8000/api/students'

# READ (get)
data = requests.get(url=URL)
print(data.json())


# CREATE (post)
py_data = {
    'name': 'Nitish',
    'rollno': 5,
    'course': 'SQLite',
}
# res = requests.post(url=URL, data=json.dumps(py_data))
# print(res)


# UPDATE (put/patch)
# Let's update Student3 (put)
py_data = {
    'name': 'Nitish Mamju',
    'rollno': 5,
    'course': 'ITI',
}
URL2 = 'http://127.0.0.1:8000/api/student/14'
# res = requests.put(url=URL2, data=json.dumps(py_data))
# print(res)


# Let's update Student3 (patch)
py_data = {
    'course': 'Sqlite',  # Only updating the course field
}
URL2 = 'http://127.0.0.1:8000/api/student/14'
# res = requests.patch(url=URL2, data=json.dumps(py_data))
# print(res)


# DELETE
URL3 = 'http://127.0.0.1:8000/api/student/5'
# res = requests.delete(url=URL3)
# print(res)
