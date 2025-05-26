import requests

URL = 'http://127.0.0.1:8000/api/students/'

# READ (get)
data = requests.get(url=URL)
print(data.json())


# CREATE (post)
py_data = {
    'name': 'Nitish',
    'rollno': 4,
    'course': 'SQLite',
}
# res = requests.post(url=URL, data=json.dumps(py_data))
# print(res)


# UPDATE (put)
py_data = {
    'name': 'Nitish Kumar',
    'rollno': 4,
    'course': 'ITI',
}
URL2 = 'http://127.0.0.1:8000/api/student/4'
# res = requests.put(url=URL2, data=json.dumps(py_data))
# print(res)


# DELETE
URL3 = 'http://127.0.0.1:8000/api/student/4'
res = requests.delete(url=URL3)
print(res)
