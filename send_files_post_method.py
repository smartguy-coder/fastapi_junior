import requests

url = 'http://127.0.0.1:8000/file'

headers = {
    'accept': 'application/json',
    'type': 'video/mp4'
}

files = {
    'file': open('2023-06-09_18-40.png', 'rb'),
}

response = requests.post(
    url=url,
    headers=headers,
    files=files,
)

print(response)
