import urllib2
from bs4 import BeautifulSoup
import sys
import codecs



#url_input = 'http://www.creativebloq.com/web-design/best-404-pages-812505'
url_input = 'http://www.oregonlive.com/'
webUrl = urllib2.urlopen(url_input)
if (webUrl.getcode() == 200):
    soup = BeautifulSoup(webUrl, 'html.parser')
    page = soup.find('p')
    text = page.text.strip()
    print(text)