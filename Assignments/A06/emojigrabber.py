from bs4 import BeautifulSoup
from beautifulscraper import BeautifulScraper
import urllib
from time import sleep
import os
import errno

""" 
Jamal Joseph
    This program scrapes a page to get emoji images
"""
scraper = BeautifulScraper()
directory = "emoji"
url = 'https://www.webfx.com/tools/emoji-cheat-sheet/'

page = scraper.go(url)

counter =0

#makes emojis folder 
try:  
    os.mkdir('emojis')
except OSError:  
    print ("Creation of the directory %s failed" % directory)
else:  
    print ("Successfully created the directory %s " % directory)

#loops through all the emojis and downloads them
for emoji in page.find_all("span",{"class":"emoji"}):
    image_path = emoji['data-src']
    urllib.request.urlretrieve((url+image_path), "emojis/emoji%d.jpg"%(counter))
    sleep(.02)
    counter +=1
    print(url+image_path)
   
