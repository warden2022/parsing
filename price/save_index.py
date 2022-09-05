import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def save_index():
    ua = UserAgent()
    url = 'https://www.sravni.ru/ege-oge/region/sankt-peterburg/?courseSubject=courseMath'
    headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'User-Agent': ua.random
    }

    response = requests.get(url=url, headers=headers)

    with open(f'./blank/index.html', 'w', encoding='utf8') as file:
        file.write(response.text)

