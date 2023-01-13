import time

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


s = Service("C:/Users/Anton/chrome_driver_for_selenium/chromedriver.exe")
options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=options, service=s)


def check_wiki():
    with open("cars.csv", "r") as f:
        for text in f:
            url = "https://en.wikipedia.org/w/index.php?search=" + text + "&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
            driver.get(url)

            driver.find_element(By.CLASS_NAME, "searchResultImage-thumbnail").click()
            try:
                years = driver.find_element(By.XPATH, '//table[@class="infobox hproduct"]').text.split("Production")[1]
                print(years[1:10])
            except NoSuchElementException:
                print("Not found")

    driver.close()


if __name__ == "__main__":
    start = time.time()
    check_wiki()
    end = time.time() - start
    print(f'total time is: {end}')
