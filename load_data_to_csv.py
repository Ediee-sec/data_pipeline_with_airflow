import pandas as pd
import get_data_api_coinbase
from datetime import datetime

df = pd.DataFrame(get_data_api_coinbase.ticker())

today = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

path = '/home/emerson/codes/python/Dados/projetos_etl/data_pipeline_with_airflow/data_lake'

df.to_csv(f'{path}/file_cripto_coins_{today}.csv', sep=';', encoding='utf-8', index=False)

#Cria um arquivo .txt para exportar a variavel que contem o nome do arquivo para o shell script
file_name = f'{path}/file_cripto_coins_{today}.csv'

with open('file_today_data_lake.txt', 'w') as file:
    file.write(file_name)
