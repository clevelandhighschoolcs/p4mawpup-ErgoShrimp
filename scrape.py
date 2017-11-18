import urllib2
from bs4 import BeautifulSoup
import time

#Updating soup




def main():
    #Updates Page
    blog_page = 'https://nathan440.wordpress.com/'
    webUrl = urllib2.urlopen(blog_page)
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
        blog_page = 'https://nathan440.wordpress.com/'
        webUrl = urllib2.urlopen(blog_page)
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
    if(time_input > 4):
        print("parameter acceptable. new time interval set")
    else:
        print("parameter too small. Using 5 seconds instead")
        time_input = 5
except TypeError:
    print("request not understood. using 5 seconds instead")
    time_input = 5

"""
blog_page = 'https://nathan440.wordpress.com/'
webUrl = urllib2.urlopen(blog_page)
"""
while True:
    main()