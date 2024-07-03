import requests

r = requests.post("http://127.0.0.1:5000/books", json={
    "title" : "Programming In Python"
})

print(r.text)