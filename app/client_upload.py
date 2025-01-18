import requests
import time

url = 'http://127.0.0.1:5080/upload'
file = {'file': open('LineasFactura.csv', 'rb')}
start = time.time()
resp = requests.post(url = url, files = file)
end = time.time()
print(f'Time elapsed: {end - start}s')
print(resp.json())
