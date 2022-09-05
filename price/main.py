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

    with open("./data/items.csv", 'a', encoding="utf-8") as file:
        for i in items:
            
            writer = csv.writer(file)
            writer.writerow(
                (
                    i['name'],
                    i['level'],
                    i['interval'],
                    i['price']
                )
            )

def main():
    # save.save_index()
    parse_url()

if __name__ == '__main__':
    main()

'src="https://sravni.go2cloud.org/aff_i?offer_id=1473&aff_id=2&adv_sub=W0IG0N1eerWyUz2h8AceR&aff_sub3=utmccn%253d(not%2520set)%257cutmcct%253d(not%2520set)%257cutmcmd%253d(none)%257cutmcsr%253d(direct)%257cutmctr%253d(not%2520set)&aff_unique3=https%3A%2F%2Fwww.tutoronline.ru%2Fkursy-po-matematike%2Fpodgotovka-k-oge-po-matematike-2022-2023&url=https%3A%2F%2Fwww.tutoronline.ru%2Fkursy-po-matematike%2Fpodgotovka-k-oge-po-matematike-2022-2023&aff_sub4=TutorOnline%7C%D0%9A%D1%83%D1%80%D1%81%20%D0%BF%D0%BE%D0%B4%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BA%D0%B8%20%D0%BA%20%D0%9E%D0%93%D0%AD%20%D0%BF%D0%BE%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%20%7C%202022-2023&aff_sub2=%2Fege-oge%2Fregion%2Fsankt-peterburg%2F&source=search&aff_sub5=%D0%9F%D0%BE%D0%B4%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BA%D0%B0%20%D0%BA%20%D0%95%D0%93%D0%AD&aff_sub=ga_1131926064.1662332076%7Cym_1662332076183692816"'