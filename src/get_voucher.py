''' Este modulo permite recuperar el voucher de la conexion
wifi de la UNLP desde una URL '''
import urllib
from bs4 import BeautifulSoup

def get_voucher(html):
    ''' parses html and returns the voucher '''
    soup = BeautifulSoup(html, 'html.parser')
    contents = soup.find(string="Voucher").find_next('h2').contents
    return contents[0].strip() if contents else "0"

def open_url(url):
    ''' opens url given by parameter '''
    response = urllib.urlopen(url)
    html = response.read()
    return html