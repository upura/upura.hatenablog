
# -*- coding:utf-8 -*-
# https://qiita.com/mix_dvd/items/8e5d4c9703e3db6e3851#_reference-6efbc66bde276010be2f

import os
import bs4
import time
import random
from itertools import chain

import urllib.request

base_url = 'http://misscolle.com'

def fetch_page_urls():
    html = urllib.request.urlopen('{}/versions'.format(base_url))
    soup = bs4.BeautifulSoup(html, 'html.parser')

    columns = soup.find_all('ul', class_='columns')
    atags = map(lambda column: column.find_all('a'), columns)

    with open('page_urls.txt', 'w') as f:
        for _ in chain.from_iterable(atags):
            path = _.get('href')
            if not path.startswith('http'):  # Relative path
                path = '{}{}'.format(base_url, path)
            if path[-1] == '/':  # Normalize
                path = path[:-1]
            f.write('{}\n'.format(path))

def fetch_photos():
    with open('page_urls.txt') as f:
        for url in f:
            try:
                # Make directories for saving images
                dirpath = 'photos/{}'.format(url.strip().split('/')[-1].replace("20","/20").replace("miss",""))
                os.makedirs(dirpath, exist_ok=True)
    
                y = int(url[-4:])
    
                if y > 2012:
                    # 2013年以降用
                    html = urllib.request.urlopen('{}/photo'.format(url.strip()))
                else:
                    # 2012年以前用
                    url2012 = "https://misscolle.com/" + url.strip().split('/')[-1].replace("miss","")
                    html = urllib.request.urlopen('{}/photo'.format(url2012))
    
                soup = bs4.BeautifulSoup(html, 'html.parser')
                photos = soup.find_all('li', class_='photo')
                paths = map(lambda path: path.find('a').get('href'), photos)
    
                for path in paths:
                    filename = '_'.join(path.split('?')[0].split('/')[-2:])
                    filepath = '{}/{}'.format(dirpath, filename)
                    print(filepath)
                    # Download image file
                    urllib.request.urlretrieve('{}{}'.format(base_url, path), filepath)
                    # Add random waiting time (4 - 6 sec)
                    time.sleep(4 + random.randint(0, 2))
            except:
                pass

if __name__ == '__main__':
    fetch_page_urls()
    fetch_photos()
