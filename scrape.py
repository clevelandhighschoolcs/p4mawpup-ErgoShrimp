import urllib2
from bs4 import BeautifulSoup
import time

#Updating soup

'''
Things to do:

1. Make sure the URL can be substitued for blog_page
2. Make sure different parsing is used depending on whether it is blog_page or user inputted url_input
3. Have a general parser
'''



"""
if (url_input == 'https://nathan440.wordpress.com/'):
    name = blog_update()
else:
    name = html_update()

def blog_update():
        webUrl = urllib2.urlopen(url_input)
    if (webUrl.getcode() == 200):
        soup = BeautifulSoup(webUrl, 'html.parser')
        name_box = soup.find('div', attrs={'class': 'entry-meta'})
        name = name_box.text.strip()
        return name
def blog_update():
    name = "working on it"
    return name
""" 


def main():
    #Updates Page
    webUrl = urllib2.urlopen(url_input)
    if (webUrl.getcode() == 200):
        soup = BeautifulSoup(webUrl, 'html.parser')
        name_box = soup.find('div', attrs={'class': 'entry-meta'})
        name = name_box.text.strip()
        print(name)
        f = open("textfile.txt","w+")
        f.write(name)
        #Unable to get the f = read()
        fileContent = name
        #print(fileContent)
        f.close()
        time.sleep(float(time_input))
    #Checks for change
        webUrl = urllib2.urlopen(url_input)
        soup = BeautifulSoup(webUrl, 'html.parser')
        name_box = soup.find('div', attrs={'class': 'entry-meta'})
        name2 = name_box.text.strip()
        print(name2)
        if(str(name2)) == (str(fileContent)):
            print("There has been no change!")
        else:
            print("There has been a change!")
        print("One scrape has passed")
        time.sleep(float(time_input))
    else:
        print("unable to access website")



print("Welcome to Nathan's Web scraper")
time.sleep(1)
print("Please note that the script runs forever until you press ctrl+c")
time.sleep(2)
print("Default waiting time is 5 seconds. Please input another interval you want.")
time.sleep(1)
time_input = raw_input("What time interval do you want? (input as a number)")
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
        print("Going with Unity blog")
        url_input = 'https://nathan440.wordpress.com/'
except Exception:
    print("Request either nothing or not understand. Using Nathan's Unity Blog")
    url_input = 'https://nathan440.wordpress.com/'
"""
blog_page = 'https://nathan440.wordpress.com/'
webUrl = urllib2.urlopen(blog_page)
"""
while True:
    main()