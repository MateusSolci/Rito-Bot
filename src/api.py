import requests
import json

# retorna o resultado de qualquer request em json
def makeRequest(url):
    try:
        response = requests.get(url).json()
    except:
        response = '*Bad Request*'

    return response

