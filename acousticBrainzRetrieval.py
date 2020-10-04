import json
import requests
import csv
import pandas

def getUrl(path):
    return 'https://acousticbrainz.org/api/v1/' + path

def getHighLevelData(path):
    resp = requests.get('https://acousticbrainz.org/api/v1/' + path + '/high-level')
    return resp.json()

def getLowLevelData(path):
    resp = requests.get('https://acousticbrainz.org/api/v1/' + path + '/low-level')
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
    return dictList

