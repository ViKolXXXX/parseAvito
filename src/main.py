import requests
from bs4 import BeautifulSoup


def get_new_ads():
    url = 'https://www.avito.ru/your_category'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    ads = []
    for ad in soup.find_all('div', class_='item'):
        title = ad.find('h3').text
        link = ad.find('a')['href']
        ads.append({'title': title, 'link': link})

    return ads