import requests

endpoint = 'http://127.0.0.1:8000/api/' 
get_response = requests.get(endpoint,json={'product_id': 123})


print(get_response.text)
