import pandas as pd
import get_data_api_coinbase
from datetime import datetime

df = pd.DataFrame(get_data_api_coinbase.ticker())

today = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

path = '/home/emerson/codes/python/Dados/projetos_etl/data_pipeline_with_airflow/data_lake'

df.to_csv(f'{path}/file_cripto_coins_{today}.csv', sep=';', encoding='utf-8', index=False)