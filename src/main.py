import requests
from bs4 import BeautifulSoup


url 


def get_new_ads():
    html = get_html(url, params={'bt': 1, 'pmax': max_price, 'pmin': min_price, 'q': search, 's': '2', 'view': 'gallery'})
    soup = BeautifulSoup(html.text, 'lxml')
    url = 'https://www.avito.ru/moskva_i_mo/avtomobili'
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)


    ads = []
    for ad in soup.find_all('div', class_='item'):
        title = ad.find('h3').text
        link = ad.find('a')['href']
        ads.append({'title': title, 'link': link})

    return ads