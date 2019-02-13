import os,sys
import json
import pprint as pp
#import ujson

"""
Assumes you have all of your game data in a folder called '/json_data/live_update_data'
and your files are named gameid.json where gameid can be something like 2009102505.json
"""

"""
Returns a list of files in given directory
"""
def getFiles(path):
    files = []
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all subdirectories first.
        # for subdirname in dirnames:
        #     print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            #print(os.path.join(dirname, filename))
            files.append(os.path.join(dirname, filename))

        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if '.git' in dirnames:
            # don't go into any .git directories.
            dirnames.remove('.git')
    return files

"""
Checks to see if it is json
"""
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

"""
Tries to open a file 
"""
def openFileJson(path):
    try:
      f = open(path, "r")
      data = f.read()
      if is_json(data):
          return json.loads(data)
      else:
          print("Error: Not json.")
          return {}
    except IOError:
        print ("Error: Game file doesn't exist.")
        return {}

path = './live_update_data'
files = getFiles(path)

files = sorted(files)

# loop through files
for file in files:

    # read in json data and convert to dictionary
    data = openFileJson(file)

    # pull out the game id and game data
    for gameid,gamedata in data.items():
        if gameid != "nextupdate":
            print(gameid)
            # go straight for the drives
            for driveid,drivedata in gamedata['drives'].items():
                #print(driveid)
                if driveid != 'crntdrv':
                    for playid,playdata in drivedata['plays'].items():
                        print(playid)
                        for nameid,namedata in drivedata['time'].items():
                            print(nameid)              



##############################################################
# getPlayIds(data,gameId,driveid)
# This function gets the play ids and reads them into a list
# 
# Params: 
#    p1 [data] : 
#    p2 [gameId] :  
#    p3 [driveId]
# Returns: 
#    returns the play ids in a list
def getPlayIds(data,gameId,driveid):
    playIds = []
    if type(data[gameid]["drives"][driveid]) is dict:
        for playId,playData in data[gameId]["drives"][driveid]['plays'].items():
            playIds.append(playId)
            print(playId)
        return playIds
    return []