import requests
from lxml import html
import json 
from tqdm import tqdm

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
BASE_URL = "https://www.coindesk.com/"

def get_tree(url):
    response = requests.get(url, headers=HEADERS)
    return html.fromstring(response.content)

def first_level_of_crawl():
    tree = get_tree(BASE_URL)
    xpath = '//div[@class="flex w-full flex-col px-8"][.//span[text()="News"]]/ul/li/a/@href'
    categories = tree.xpath(xpath)
    return list(map(lambda x: str(x)[1:] if x[0] == '/' else str(x), categories))

def secound_level_of_crawl(category):
    url = BASE_URL + category
    tree = get_tree(url)
    xpath = '//a[@class="text-color-charcoal-900 mb-4 hover:underline"]/@href'
    news = tree.xpath(xpath)
    news = list(map(lambda x: str(x)[1:] if x[0] == '/' else str(x), news))
    return news

def third_level_of_crawl(new):
    url = BASE_URL + new
    tree = get_tree(url)

    xpath = '//h1/text()'
    title = tree.xpath(xpath)[0]

    xpath = '//h2/text()'
    description = tree.xpath(xpath)[0]

    xpath = '//ul/li/text()'
    what_to_know = tree.xpath(xpath)

    data = {
        'title': title,
        'description': description,
        'what_to_know': what_to_know,
        'source': url
    }
    return data

def save_data_to_json(data, filename="dataset.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def main():
    dataset = []
    news = list(map(secound_level_of_crawl, first_level_of_crawl()))
    for category in tqdm(news, desc='category'):
        for new in tqdm(category, desc='new'):    
            data = third_level_of_crawl(new)
            dataset.append(data)
    save_data_to_json(dataset)

if __name__ == '__main__':
    main()
    