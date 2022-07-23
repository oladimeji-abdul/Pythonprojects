import requests as rq
from bs4 import BeautifulSoup as bs
import urllib.request
def imgFunctio():
    gitUser = input('github username: ')

    url = 'http://github.com/' + gitUser
    r = rq.get(url)
    soup = bs(r.content, 'html.parser')
    profile_image = soup.find('img', {'alt': 'Avatar'})['src']
    return profile_image
abdulcodes = imgFunctio()

urllib.request.urlretrieve(abdulcodes, 'abdul.jpg')