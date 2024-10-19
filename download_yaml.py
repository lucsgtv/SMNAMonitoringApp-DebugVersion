import intake
import requests
import os

remote_catalog_url = 'http://ftp1.cptec.inpe.br/pesquisa/das/carlos.bastarz/SMNAMonitoringApp/berror/catalog_berror.yml'

local_save_path = 'C:/Users/ll7nt/SMNAMonitoringApp/examples'
os.makedirs(local_save_path, exist_ok=True)

data_key = '2024100806'

def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Arquivo salvo em: {save_path}")
    else:
        print(f"Erro ao baixar o arquivo: {response.status_code}")

catalog = intake.open_yaml_file_cat(remote_catalog_url)

if data_key in catalog:
    data_entry = catalog[data_key]
    
    urlpath = data_entry['args']['urlpath']
    file_name = os.path.basename(urlpath) 
    local_file_path = os.path.join(local_save_path, file_name)
    download_file(urlpath, local_file_path)
else:
    print(f"Data '{data_key}' não encontrada no catálogo.")
