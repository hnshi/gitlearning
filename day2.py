import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

resp = requests.get(url)
a = resp.json()
print(a['userId'])
print(type(resp.text))