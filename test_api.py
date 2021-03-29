import requests
## Api Get
# response = requests.get('http://127.0.0.1:8000/api/whatsapp')
# json = response.json()
# for data in json:
#     print(data['nomor'])
# print(response.json())

## Api Post
r = requests.put("http://127.0.0.1:8000/api/update-whatsapp",
                  data={'id': 1, 'stts': 'Terkirim'})
print(r.status_code, r.reason)
