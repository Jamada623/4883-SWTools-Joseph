import urllib
from time import sleep
import json
from pprint import pprint
from bs4 import BeautifulSoup
from beautifulscraper import BeautifulScraper


scraper = BeautifulScraper()


sleep(.02)


years =[x for x in range(2009,2019)]
weeks = [x for x in range(1,18)]
stype = "REG"
gameids ={}
'REG'
'POST'

f = open("nfldata.json", "w")

for year in years:    
    
    for week in weeks:
        url="http://www.nfl.com/schedules/%d/%s%s"%(year,stype,str(week))
        page = scraper.go(url)  
        divs = page.find_all('div',{"class":"schedules-list-content"})  
        for div in divs:
            print (div['data-gameid'])
            gameids=(div['data-gameid']), year, stype
            
            print (gameids)
        
        print (url)
        
print (div['data-gameid'])

stype = "POST"
for year in years:    
    
    for week in weeks:
        url="http://www.nfl.com/schedules/%d/%s%s"%(year,stype,str(week))
        page = scraper.go(url)  
        divs = page.find_all('div',{"class":"schedules-list-content"})  
        for div in divs:
            print (div['data-gameid'])
            gameids=(div['data-gameid']), year, stype
           
            print (gameids)
        
        print (url)
        

for game in gameids:
    
    with urllib.request.urlopen("http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json"%(game,game)) as url:
        data = json.loads(url.read().decode())
        f.write(json.dumps(data))
         
    print(data)