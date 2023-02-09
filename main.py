import requests as r,threading
dem=0
def send():
	dem=dem+1
	response = r.get('https://anhkhoadev.site/grap/index.php?id=49').json()
	print(f'{dem} - {response}')
for o in range(100):
	threading.Thread(target=send).start()
