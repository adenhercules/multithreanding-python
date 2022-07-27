import requests
import time

url_list = [
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
    img_data = requests.get(url).content
    img_name = url.split('/')[4]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_data)
        print(f'downloading {img_name}')
        
t1 = time.perf_counter()
for i in url_list:
    download(i)
t2 = time.perf_counter()
print(f'Tempo gasto:  {t2-t1} segundos') 