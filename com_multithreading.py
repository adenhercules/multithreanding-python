import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time

lista_urls = [
     'https://www.irib.org.br/app/webroot/files/downloads/images/82505707_2272119153087587_6591185429532246016_n.jpg',
     'https://images.pexels.com/photos/509922/pexels-photo-509922.jpeg',
     'https://images.pexels.com/photos/325812/pexels-photo-325812.jpeg',
     'https://images.pexels.com/photos/1252814/pexels-photo-1252814.jpeg',
     'https://images.pexels.com/photos/1420709/pexels-photo-1420709.jpeg',
     'https://images.pexels.com/photos/963486/pexels-photo-963486.jpeg',
     'https://images.pexels.com/photos/1557183/pexels-photo-1557183.jpeg',
     'https://images.pexels.com/photos/3023211/pexels-photo-3023211.jpeg',
     'https://images.pexels.com/photos/1031641/pexels-photo-1031641.jpeg',
     'https://images.pexels.com/photos/439227/pexels-photo-439227.jpeg',
     'https://images.pexels.com/photos/696644/pexels-photo-696644.jpeg',
     'https://images.pexels.com/photos/911254/pexels-photo-911254.jpeg',
     'https://images.pexels.com/photos/1001990/pexels-photo-1001990.jpeg',
     'https://images.pexels.com/photos/3518623/pexels-photo-3518623.jpeg',
     'https://images.pexels.com/photos/916044/pexels-photo-916044.jpeg'
]

def download(url):
    img_tamanho = requests.get(url).content
    img_nome = url.split('/')[4]
    img_nome = f'{img_nome}.jpg'
    with open(img_nome, 'wb') as img_arq:
        img_arq.write(img_tamanho)
        print(f'downloading {img_nome}')

inicioContadorTempo = time()
processes = []

with ThreadPoolExecutor(max_workers=10) as executor:
    for url in lista_urls:
        processes.append(executor.submit(download, url))


print(f'Tempo gasto: {time() - inicioContadorTempo}')