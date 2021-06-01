# script base on video https://www.youtube.com/watch?v=VLFT65xX8Qw

from bs4 import BeautifulSoup
import requests

url = 'https://indodax.com/api/summaries'


def ParsePrice():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')  # lxml need to install manually from your terminal
    price = soup.find('id', class_='table table-bordered table-striped table-markets table-markets-large no-footer dataTable')
    return price


while True:
    print('Harga saat ini adalah: Rp.'+str(ParsePrice()) +'/koin.')
