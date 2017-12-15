import urllib2
try:
	from bs4 import BeautifulSoup
except Exception as e:
	print "Are you sure you have BeautifulSoup installed?"
	print "Type 'pip install BeautifulSoup4' in the terminal to install it."
	sys.exit()
import time
from twilio.rest import Client
#Updating soup

'''
Things to do:

1. Make sure the URL can be substitued for blog_page
2. Make sure different parsing is used depending on whether it is blog_page or user inputted url_input
3. Have a general parser
'''




test = False

def blog_update():
    webUrl = urllib2.urlopen(url_input)
    if (webUrl.getcode() == 200):
        soup = BeautifulSoup(webUrl, 'html.parser')
        name_box = soup.find('div', attrs={'class': 'entry-meta'})
        scrape = name_box.text.strip()
        return scrape
def html_update():
    webUrl = urllib2.urlopen(url_input)
    if (webUrl.getcode() == 200):
        soup = BeautifulSoup(webUrl, 'html.parser')
        page = soup.find('p')
        scrape = page.text.strip()
        return scrape



print("Script runs forever until you press ctrl+c")
time.sleep(2)
time_input = raw_input("Default time interval is 5 seconds. input another time interval you want (input as a number of seconds)")
try:
    float(time_input)
    if(time_input > 4):
        print("parameter acceptable. new time interval set")
    else:
        print("parameter too small. Using 5 seconds instead")
        time_input = 5
except Exception:
    print("request not understood. using 5 seconds instead")
    time_input = 5
time.sleep(2)
print("Default webpage to scrape is Nathan's unity blog")
url_input = raw_input("What URL do you want to scrape (enter full URL or nothing if you do not want change)?")
try:
    webUrl = urllib2.urlopen(url_input)
    if(webUrl.getcode() == 200):
        print("URL acceptable")
        url_input = '%s' %url_input
    else:
        code = webUrl.getcode()
        print("Error, web code return was '%s'" % code)
        print("Using Nathan's Unity Blog")
        url_input = 'https://nathan440.wordpress.com/'
except Exception:
    print("Request either nothing or not understand. Using Nathan's Unity Blog")
    url_input = 'https://nathan440.wordpress.com/'
while (test == False):
    my_phone_number = raw_input("input phone number for twilio to text (just numbers)")
    twilio_phone_number = raw_input("input phone number that twilio texts from (just numbers)")
    account_sid = raw_input("input account_sid")
    auth_token = raw_input("input auth_token")
    try:
        client = Client(account_sid, auth_token)
        client.messages.create(
            body='Test!',
            to=my_phone_number,
            from_=twilio_phone_number
        )
        test = True
    except Exception:
        print "Test message didn't work!"

if (url_input == "https://nathan440.wordpress.com/"):
    scrape = blog_update()
else:
    scrape = html_update()
OlderScrape = scrape
time.sleep(float(time_input))
"""
blog_page = 'https://nathan440.wordpress.com/'
webUrl = urllib2.urlopen(blog_page)
"""
while True:
    if (url_input == 'https://nathan440.wordpress.com/'):
        scrape = blog_update()
    else:
        scrape = html_update()
    if(str(scrape)) == (str(OlderScrape)):
        print("There has been no change!")
    else:
        print("There has been a change!")
        client = Client(account_sid, auth_token)
        client.messages.create(
            body='There has been a change!',
            to=my_phone_number,
            from_=twilio_phone_number
        )
        break
    OlderScrape = scrape
    time.sleep(float(time_input))
