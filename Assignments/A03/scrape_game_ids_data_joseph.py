import urllib.request
from time import sleep
import json
from pprint import pprint
from bs4 import BeautifulSoup
from beautifulscraper import BeautifulScraper


scraper = BeautifulScraper()


years =[x for x in range(2009,2018)]
weeks = [x for x in range(1,18)]
stype = "REG"
gameids =[]



f = open("nfldata.json", "w")
#f.write(json.dumps("REG"))
for year in years:    
    
    for week in weeks:
        url="http://www.nfl.com/schedules/%d/%s%s"%(year,stype,str(week))
        page = scraper.go(url)  
        divs = page.find_all('div',{"class":"schedules-list-content"})  
        for div in divs:
            #print (div['data-gameid'])
            #gameids=(div['data-gameid']), year, stype
            gameids.append(div['data-gameid'])
            f.write(json.dumps(gameids))
            #print (gameids)
        
        #print (url)
        
#print (div['data-gameid'])

stype = "POST"

#f.write(json.dumps("POST"))
for year in years:    
    
    for week in weeks:
        url="http://www.nfl.com/schedules/%d/%s%s"%(year,stype,str(week))
        page = scraper.go(url)  
        divs = page.find_all('div',{"class":"schedules-list-content"})  
        for div in divs:
            #print (div['data-gameid'])
            #gameids=(div['data-gameid']), year, stype
            gameids.append(div['data-gameid'])
            #print (gameids)
            f.write(json.dumps(gameids))
        #print (url)

#f.write(json.dumps(gameids))        

for gameid in gameids:
        #print (gameid)
        urllib.request.urlretrieve("http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json"%(gameid,gameid),gameid+'.json')    
        sleep(.02)
    #data = json.loads(url.read().decode())
        

         
