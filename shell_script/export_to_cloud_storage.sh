#Lê o arquivo que contem o nome do arquivo, esse arquivo é criado no python
file_today=$(cat file_today_data_lake.txt)

#Envia o arquivo do datalake do linux para o datalake no GCP
bq -m cp $file_today gs://emerson254/ingestion/