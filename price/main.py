'''
py -m venv env
env/Scripts/activate
python.exe -m pip install --upgrade pip
pip install requests
pip install bs4
pip install lxml
pip install selenium
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
    # open index.html
    #with open('./blank/index', 'r', encoding='utf8') as file:
    #    src = file.read()
    with open('./blank/index_selenium.html', 'r', encoding='utf8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml') # create soup object
    parsing_sravni_ru(soup)

def parsing_sravni_ru(soup):
    names = soup.find_all('span', class_='_106rrj0') # scraping names
    
    # scraping age childrens
    age_divs = soup.find_all('div', {'style':'grid-area:firstCell-1', 'class':'_pjql8'})
    ages = []
    for i in age_divs:
        age_span = i.find('span')
        ages.append(age_span)
    
    # scraping course duration
    duration_divs = soup.find_all('div', {'style':'grid-area:secondCell-1', 'class':'_pjql8'})
    durations = []
    for i in duration_divs:
        duration_span = i.find('span')
        durations.append(duration_span)
    
    # scraping price
    prices = soup.find_all('span', class_='_e9qrci _k8dl2y')

    items = []
    for (n, l, i, p) in zip(names, ages, durations, prices):
        name = n.text.strip()
        age = l.text.strip()
        duration = i.text.strip()
        price = p.text.strip().replace('\xa0','')
        items.append(
            {
                'name' : name,
                'age' : age,
                'duration' : duration,
                'price' : price,
            }
        )
        
    # save json file
    with open("./data/items.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)

    with open("./data/items.csv", 'a', encoding="utf-8") as file:
        for i in items:
            
            writer = csv.writer(file)
            writer.writerow(
                (
                    i['name'],
                    i['age'],
                    i['duration'],
                    i['price']
                )
            )

def main():
    save.save_selenium('https://www.sravni.ru/ege-oge/region/sankt-peterburg/?courseSubject=courseMath')
    #save.save_index('https://www.sravni.ru/ege-oge/region/sankt-peterburg/?courseSubject=courseMath')
    parse_url()

if __name__ == '__main__':
    main()
