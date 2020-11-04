import requests
import json

# retorna o resultado de qualquer request em json
def make_request(url):
    try:
        response = requests.get(url).json()
    except:
        response = '*Bad Request*'

    return response
