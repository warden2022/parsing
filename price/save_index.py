import time
import requests

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def save_index(url):
    ua = UserAgent()
    headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'User-Agent': ua.random
    }

    response = requests.get(url=url, headers=headers)

    with open(f'./blank/index.html', 'w', encoding='utf8') as file:
        file.write(response.text)

def save_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')
    try:
        driver = webdriver.Firefox(
            executable_path='C:\\parsing\\price\\geckodriver.exe',
            options=options,
        )
        driver.get(url=url)
        time.sleep(8)

        with open('./blank/index_selenium.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)

    except Exception as ex:
        print(ex)
        with open('./blank/index_selenium.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
    finally:
        driver.close()
        driver.quit()