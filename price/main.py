'''
py -m venv env
env/Scripts/activate
python.exe -m pip install --upgrade pip
pip install requests
pip install bs4
pip install lxml
'''
'''
pip install fake-useragent
pip install asyncio
pip install aiogram
pip install aiofiles
pip install aiocsv

deactivate
'''
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import save_index as save
import itertools
import json
import csv

def parse_url():
    with open('./blank/index.html', 'r', encoding='utf8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    names = soup.find_all('span', class_='_106rrj0')
    level_divs = soup.find_all('div', {'style':'grid-area:firstCell-1', 'class':'_pjql8'})
    levels = []
    for i in level_divs:
        level_span = i.find('span')
        levels.append(level_span)
    intervals_divs = soup.find_all('div', {'style':'grid-area:secondCell-1', 'class':'_pjql8'})
    intervals = []
    for i in intervals_divs:
        interval_span = i.find('span')
        intervals.append(interval_span)
    prices = soup.find_all('span', class_='_e9qrci _k8dl2y')

    items = []
    for (n, l, i, p) in zip(names, levels, intervals, prices):
        name = n.text.strip()
        level = l.text.strip()
        interval = i.text.strip()
        price = p.text.strip().replace('\xa0','')
        items.append(
            {
                'name' : name,
                'level' : level,
                'interval' : interval,
                'price' : price,
            }
        )
    
    # save json file
    with open("./data/items.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)
    

def main():
    # save.save_index()
    parse_url()

if __name__ == '__main__':
    main()
