import json
import requests
import csv
import pandas as pd

def getUrl(path):
    return 'https://acousticbrainz.org/api/v1/' + path

def getHighLevelData(path):
    resp = requests.get('https://acousticbrainz.org/api/v1/high-level?recording_ids=' + path)
    # resp = requests.get('https://acousticbrainz.org/api/v1/' + path + '/high-level')
    return resp.json()

def getLowLevelData(path):
    resp = requests.get('https://acousticbrainz.org/api/v1/low-level?recording_ids=' + path)
    # resp = requests.get('https://acousticbrainz.org/api/v1/' + path + '/low-level')
    return resp.json()

def getTitle(highLevelData):
    return highLevelData['metadata']['tags']['title']

def getArtist(highLevelData):
    return highLevelData['metadata']['tags']['artist']

def getAlbum(highLevelData):
    return highLevelData['metadata']['tags']['album']

def getDanceability(highLevelData):
    return highLevelData['highlevel']['danceability']['all']

def getGenre(highLevelData):
    return highLevelData['highlevel']['genre_rosamerica']['all']

def getMood(highLevelData):
    mood_mirexDict = highLevelData['highlevel']['moods_mirex']['all']
    mood_relaxedDict = highLevelData['highlevel']['mood_relaxed']['all']
    return mood_mirexDict.update(mood_relaxedDict)

def getTimbre(highLevelData):
    return highLevelData['highlevel']['timbre']['all']

def getInstrumental(highLevelData):
    return highLevelData['highlevel']['voice_instrumental']['all']

def getLoudness(lowLevelData):
    return lowLevelData['lowlevel']['average_loudness']

def getBpm(lowLevelData):
    return lowLevelData['rhythm']['bpm']

def makeSongDict(highLevelData, lowLevelData):
    song = {
        'title' : getTitle(highLevelData), 
        'artist' : getArtist(highLevelData), 
        'album' : getAlbum(highLevelData), 
        'dance' : getDanceability(highLevelData), 
        'genre' : getGenre(highLevelData), 
        'mood' : getMood(highLevelData), 
        'timbre' : getTimbre(highLevelData), 
        'instrumental' : getInstrumental(highLevelData),
        'loudness' : getLoudness(lowLevelData),
        'bpm' : getBpm(lowLevelData)
    }
    return song


def makeListFromCsv(filePath):
    dictList  = []
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            mbid = row[0]
            song = makeSongDict(getHighLevelData(mbid), getLowLevelData(mbid))
            dictList.append(song)
    keys = dictList[0].keys()
    with open('songData.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictList)
    return dictList

def makeCsv(filePath):
    df = pd.read_csv(filePath, header=0, sep='\t')
    mbids = df.recordingmbid.to_list()
    count = int(len(mbids)/25)
    for i in range(count):
        songsDict = get25IDs(i, mbids)
        # dictList.append(songsDict)
        keys = songsDict[0].keys()
        with open('songData.csv', 'a', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(songsDict)

def get25IDs(count, mbids):
    mbidString = ''
    miniList = []
    for i in range(25):
        mbidString += (mbids[i+(count*25)] + ';')
        miniList.append(mbids[i+(count*25)])
    mbidString = mbidString[:-1]
    highLevel = getHighLevelData(mbidString)
    lowLevel = getLowLevelData(mbidString)
    dictList = []
    for i in range(25):
        try:
            song = makeSongDict(highLevel[miniList[i]]['0'], lowLevel[miniList[i]]['0'])
            dictList.append(song)
        except:
            pass
    return dictList

