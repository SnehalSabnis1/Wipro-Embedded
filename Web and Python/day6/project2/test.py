import requests
import json

username = "bob"
password = "bob@1234"
headers = {"Content-Type": "application/json"}
data = {"username": username, "password": password}

#r = requests.post("http://127.0.0.1:5000/api/register",headers=headers,data=json.dumps(data))
r = requests.get("http://127.0.0.1:5000/api/dothis", auth=("bob","bob@1234"))
#r = requests.get("http://127.0.0.1:5000/api/dothis")
print (r.status_code)
print (r.text)