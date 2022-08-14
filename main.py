import requests
import json
from bs4 import BeautifulSoup
#find('div', class_)
#find_all('div')


def get_html(url):
    req = requests.get(url)
    return req.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-root-2oCjZ').find_all('span', class_='pagination-item-1WyVp')[-2]
    total_pages = pages.text
    return int(total_pages)


def write_json(data):
    with open('result2.json', 'w') as result_file:
        result_file.write(json.dumps(data, indent=4))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='js-catalog_serp').find_all('div', class_='description item_table-description')
    for ad in ads:
        try:
            title = ad.find('div', class_='snippet-title-row').find('h3').text.strip()
        except:
            title = ''
        try:
            price = ad.find('div', class_='about').find('span', class_='price').text.strip()
        except:
            price = ''

        data = + {
            'title': title,
            'price': price
        }

        write_json(data)


def main():
    url = 'https://www.avito.ru/rossiya/telefony/htc?p=1'
    base_url = 'https://www.avito.ru/rossiya/telefony/'
    query_part = 'iphone?'
    page_part = 'p='
    total_pages = get_total_pages(get_html(url))

    for i in range(1, 2):
        url_gen = base_url + query_part + page_part + str(i)
        html = get_html(url_gen)
        get_page_data(html)


if __name__ == '__main__':
    main()
