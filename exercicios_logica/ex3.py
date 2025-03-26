
# Explique o código abaixo. -> OK

import requests # biblioteca para requisições HTTP
import json # biblioteca para manipulação de JSON

url = 'https://api.github.com/some/endpoint' # URL da api que será consumida

headers = {'header': 'header1'} # header são os cabeçalhos que serão enviados na requisição para a API
payload = {data: 'data1'} # payload são os dados que serão enviados na requisição para a API

resp = requests.post(url, data=json.dumps(payload), headers=headers) # faz uma requisição POST para a URL com os dados e cabeçalho especificados

if resp.status_code != 200: # se o status code for diferente de 200 (200 == sucesso)
    print(resp.content) # exibe o conteúdo da resposta
    
    