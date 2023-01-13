import asyncio
import time

from concurrent.futures.thread import ThreadPoolExecutor
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


executor = ThreadPoolExecutor()


def scrape(url, *, loop):
    loop.run_in_executor(executor, scraper, url)


def scraper(url):
    s = Service("C:/Users/Anton/chrome_driver_for_selenium/chromedriver.exe")
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(options=options, service=s)
    driver.get(url)
    driver.find_element(By.CLASS_NAME, "searchResultImage-thumbnail").click()
    try:
        years = driver.find_element(By.XPATH, '//table[@class="infobox hproduct"]').text.split("Production")[1]
        print(years[1:10])
    except NoSuchElementException:
        print("Not found")


loop = asyncio.get_event_loop()
with open("cars.csv", "r") as f:
    for text in f:
        url = "https://en.wikipedia.org/w/index.php?search=" + text + "&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
        scrape(url, loop=loop)

if __name__ == "__main__":
    loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))
