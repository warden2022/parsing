''' installs
py -m venv env
env/Scripts/activate
python.exe -m pip install --upgrade pip
pip install requests
pip install bs4
pip install lxml
pip install selenium

'''
'''
pip install asyncio
pip install aiogram
pip install aiofiles
pip install aiocsv

deactivate
'''

import json
import csv
import time
import itertools

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def save_selenium(url):
    link = url
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')
    try:
        driver = webdriver.Firefox(
            executable_path='C:\\parsing\\price\\geckodriver.exe',
            options=options,
        )
        driver.get(url=link)
        time.sleep(5)

        with open('./blank/otl_oge.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)

    except Exception as ex:
        print(ex)
        #with open('./blank/otl_oge.html', 'w', encoding='utf-8') as f:
        #    f.write(driver.page_source)
    finally:
        driver.close()
        driver.quit()

def parse_url():
    # open index.html
    with open('./blank/otl_oge.html', 'r', encoding='utf8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml') # create soup object
    price = soup.find('table').find('tr').next_sibling.next_sibling.find('td').next_sibling.next_sibling.text # scraping name
    #print(price)
    # save json file
    items = []
    items.append(
            {
                'name' : 'Математика ОГЭ',
                'url' : 'https://otl-ege.ru/prices',
                'price' : price,
            }
        )
    print(items)
    with open("./data/otl_oge.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)
    
    with open("./data/otl_oge.csv", 'a', encoding="utf-8") as file:
        
        writer = csv.writer(file)
        writer.writerow(
                (
                    items[0]['name'],
                    items[0]['url'],
                    items[0]['price']
                )
        )

def main():
    #save_selenium('https://otl-ege.ru/prices')
    parse_url()

if __name__ == '__main__':
    main()
