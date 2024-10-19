import requests

urls = [
    'http://ftp1.cptec.inpe.br/pesquisa/das/carlos.bastarz/SMNAMonitoringApp/anls/catalog_anl.yml',
    'http://ftp1.cptec.inpe.br/pesquisa/das/carlos.bastarz/SMNAMonitoringApp/anls/catalog_bkg.yml'
]

filenames = ['catalog_anl.yml', 'catalog_bkg.yml']

for url, filename in zip(urls, filenames):
    try:
        
        response = requests.get(url)
        response.raise_for_status() 
        
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f'Baixado: {filename}')
    except requests.exceptions.RequestException as e:
        print(f'Erro ao baixar {filename}: {e}')
