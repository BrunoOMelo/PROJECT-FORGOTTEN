import requests

def cnpj_consult (cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    response = requests.get(url)
    data = response.json()
    return data