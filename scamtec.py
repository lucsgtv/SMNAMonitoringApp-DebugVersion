import os
import requests
from bs4 import BeautifulSoup

base_url = "https://dataserver.cptec.inpe.br/dataserver_dimnt/das/carlos.bastarz/"
folder_name = "scamtec"

os.makedirs(folder_name, exist_ok=True)

def download_file(url, folder):
    local_filename = os.path.join(folder, os.path.basename(url))
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status() 
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Baixando {local_filename}...")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")

def download_directory(url, folder):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                full_url = os.path.join(url, href).replace("\\", "/").strip('/')

                if href.endswith('/'): 
                    new_folder = os.path.join(folder, href[:-1])  
                    os.makedirs(new_folder, exist_ok=True)  
                    download_directory(full_url, new_folder)  
                else: 
                    download_file(full_url, folder) 
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")

download_directory(base_url, folder_name)
