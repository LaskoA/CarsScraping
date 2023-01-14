import asyncio
import csv
import json
import time
import aiohttp
from bs4 import BeautifulSoup


async def save_product(book_name, product_info):
    json_file_name = book_name.replace(' ', '_')
    with open(f'data/{json_file_name}.json', 'w') as book_file:
        json.dump(product_info, book_file)


async def scrape(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            body = await resp.text()
            soup = BeautifulSoup(body, 'html.parser')
            article = soup.select_one(".searchResultImage-thumbnail > a")
            link = str(article).split('href="')[1].split('" ')[0]
            async with session.get("https://en.wikipedia.org/" + link) as resp1:
                body1 = await resp1.text()
                soup1 = BeautifulSoup(body1, 'html.parser')
                infobox = soup1.select_one(".hproduct")
                production = str(infobox).split('Production')[1].split('data">')[1].split('<')[0]
                print(production)


async def main():
    start_time = time.time()

    tasks = []
    with open('cars.csv', 'r') as file:
        for text in file:
            url = "https://en.wikipedia.org/w/index.php?search=" + text + "&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
            task = asyncio.create_task(scrape(url))
            tasks.append(task)

    await asyncio.gather(*tasks)

    time_difference = time.time() - start_time
    print(f'Scraping time: %.2f seconds.' % time_difference)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
