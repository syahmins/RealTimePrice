# script base on video https://www.youtube.com/watch?v=VLFT65xX8Qw

from bs4 import BeautifulSoup
import requests

url = 'https://finance.yahoo.com/quote/TRX-USD?p=TRX-USD'


def ParsePrice():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')  # lxml need to install manually from your terminal
    price = soup.find('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    return price


while True:
    print('Harga saat ini adalah: USD'+str(ParsePrice()) +'/koin.')
