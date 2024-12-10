'''
파일 명:Ex18-5-getRankPage.py
'''
from http.client import responses

import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,'html.parser')
music_list = soup.find_all('p',class_='title')
artist_list = soup.find_all('p',class_='artist')

for idx, title in enumerate(music_list):
    artist = artist_list[idx].find_all("a")[0]
    print(f'{idx+1} {title.text.strip()}-{artist.text.strip()}')