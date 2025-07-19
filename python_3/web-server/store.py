import requests
def get_categories():
	r = requests.get('https://api.escuelajs.co/api/v1/products')
	print(r.status_code)
	print(r.text)
	print(type(r.text)) # muestra formato lista
	categories = r.json() # lo pasa a formato lista json
	for category in categories:
		print(category['title'])