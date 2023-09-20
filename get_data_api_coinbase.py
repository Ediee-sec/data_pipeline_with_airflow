import requests

#Faz a consulta na API de cotação para fazer a conversão do dolar para o real de forma atualizada
api_cot = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
req = requests.get(api_cot)
conv_cot = float(req.json()['USDBRL']['bid'])

# Cria o dicionario de dados vazio, para posteriormente preenche-lo quando tiver os dados tratados
dic_df = \
        {
            'Id_Trade'        :   [],
            'Moeda'           :   [],
            'Preco_Dolar'     :   [],
            'Preco_Reais'     :   [],
            'Volume'          :   [],
            'Tamanho'         :   []
        }

# Está função retorna todas as criptomoedas da Coinbase, retorna apenas o nome da criptomeda
def listCoins():
    url = "https://api.exchange.coinbase.com/products"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    ls = response.json()

    coin = []

    for item in ls:
        if "USD" in item['id']:
            coin_id = item['id']
            uri = f"https://api.exchange.coinbase.com/products/{coin_id}"
            req = requests.get(uri, headers=headers)
            prod = req.json()

            if prod.get('status') == 'online' and not prod.get('cancel_only') and req.status_code == 200:
                coin.append(coin_id)
                etl_id = coin_id.replace('-', '').replace('USD', '')
                dic_df['Moeda'].append(etl_id)

    return coin

#Função que retorna o dicionário de dados já totalmente preechido
#Irei importar para o pandas 
def ticker():
    #Itera sobre a função que contem todos os nomes das moedas
    for i in listCoins():
        url = f"https://api.exchange.coinbase.com/products/{i}/ticker"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers)
        ls = response.json()

        #Realizar o append no dicionario de dados preenchendo rodos os atributos
        #Está função é a que chamaremos nos demais modulos, sempre que quisermos acesso aos dados que foram extraidos
        if ls['ask'] != "0":
            dic_df['Id_Trade'].append(int(ls['trade_id']))
            dic_df['Preco_Dolar'].append(round(float(ls['price']), 4))
            dic_df['Preco_Reais'].append(round(float(ls['price']), 4) * conv_cot) #Utiliza a conversão do dolar para o real de forma atualizada
            dic_df['Volume'].append(round(float(ls['volume']), 10))
            dic_df['Tamanho'].append(round(float(ls['size']), 10))

    return dic_df

