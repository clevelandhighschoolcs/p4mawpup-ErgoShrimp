import urllib2
from bs4 import BeautifulSoup
import time


def main():
    blog_page = 'https://nathan440.wordpress.com/'
    webUrl = urllib2.urlopen(blog_page)
    if (webUrl.getcode() == 200):
        soup = BeautifulSoup(webUrl, 'html.parser')
        name_box = soup.find('div', attrs={'class': 'entry-meta'})
        name = name_box.text.strip()
        print(name)
        f = open("textfile.txt","w+")
        f.write(str(soup))
        f.close()
        print("One scrape has passed")
        time.sleep(5)
    else:
        print("unable to access website")
        print("One scrape has passed")
        time.sleep(5)
	#f = open("textfile.txt","w+")
	#data = webUrl.read()
	#if(str(Predata) == str(data)):
	#	print("There has been no change!")
	#else:
	#	print("There has been a change!")
	#f.write(Predata)
	#f.close()


print("Welcome to Nathan's Web scraper")
time.sleep(1)
print("Please note that the script runs forever until you press ctrl+c")
time.sleep(1)
while True:
    main()