import requests
import datetime
## Api Get
# response = requests.get('http://127.0.0.1:8000/api/whatsapp')
# json = response.json()
# for data in json:
#     print(data['nomor'])
# print(response.json())

## Api Post
# r = requests.put("http://127.0.0.1:8000/api/update-whatsapp",
#                   data={'id': 1, 'stts': 'Terkirim'})
# print(r.status_code, r.reason)

## Test waktu
# now = datetime.datetime.now().strftime('%H:%M')
# time = now.replace(hour=8, minute=0, second=0, microsecond=0)

## Test Looping
# import time
# starttime = time.time()
# while True:
#     print ("tick")
#     time.sleep(60.0 - ((time.time() - starttime) % 60.0))

## Menghapus +62 dan 0
# prefix = "0"
# # prefix = '+6282134626598'
# nomor = '082134626598'
# nomor.removeprefix(prefix)

#mengambil pesan txt file
with open('data.txt', 'r') as file:
    data = file.read().replace('\n', '')

# Suryo
