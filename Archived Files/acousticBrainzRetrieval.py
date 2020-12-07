import json
import requests
import csv
import pandas as pd
import spotifyPlayback
import string

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
    title = highLevelData['metadata']['tags']['title']
    title = (str(title)).translate(str.maketrans('', '', '\"[]\''))
    return title

def getArtist(highLevelData):
    artist = highLevelData['metadata']['tags']['artist']
    return (str(artist)).translate(str.maketrans('', '', '\"[]\''))

def getAlbum(highLevelData):
    album = highLevelData['metadata']['tags']['album']
    return (str(album)).translate(str.maketrans('', '', '\"[]\''))

def getDanceability(highLevelData):
    return highLevelData['highlevel']['danceability']['all']

def getGenre(highLevelData):
    return highLevelData['highlevel']['genre_rosamerica']['all']

def getMood(highLevelData):
    # mood_mirexDict = highLevelData['highlevel']['moods_mirex']['all']
    # mood_relaxedDict = highLevelData['highlevel']['mood_relaxed']['all']
    # return mood_mirexDict.update(mood_relaxedDict)
    return highLevelData['highlevel']['moods_mirex']['all']

def getTimbre(highLevelData):
    return highLevelData['highlevel']['timbre']['all']

def getInstrumental(highLevelData):
    return highLevelData['highlevel']['voice_instrumental']['all']

def getLoudness(lowLevelData):
    return lowLevelData['lowlevel']['average_loudness']

def getBpm(lowLevelData):
    return lowLevelData['rhythm']['bpm']

def makeSongDict(highLevelData, lowLevelData):
    dance = getDanceability(highLevelData)
    genre = getGenre(highLevelData)
    mood = getMood(highLevelData)
    timbre = getTimbre(highLevelData)
    instrumental = getInstrumental(highLevelData)
    title = getTitle(highLevelData)
    artist = getArtist(highLevelData)
    album = getAlbum(highLevelData)
    song = {
        'title' : title, 
        'artist' : artist, 
        'album' : album, 
        'danceable' : dance['danceable'],
        'not_danceable' : dance['not_danceable'],
        'genre_cla' : genre['cla'], 
        'genre_dan' : genre['dan'], 
        'genre_hip' : genre['hip'], 
        'genre_jaz' : genre['jaz'], 
        'genre_pop' : genre['pop'], 
        'genre_rhy' : genre['rhy'], 
        'genre_roc' : genre['roc'],
        'genre_spe' : genre['spe'],
        'mood_cluster1' : mood['Cluster1'], 
        'mood_cluster2' : mood['Cluster2'],
        'mood_cluster3' : mood['Cluster3'],
        'mood_cluster4' : mood['Cluster4'],
        'mood_cluster5' : mood['Cluster5'],
        'timbre_bright' : timbre['bright'], 
        'timbre_dark' : timbre['dark'],
        'instrumental' : instrumental['instrumental'],
        'voice' : instrumental['voice'],
        'loudness' : getLoudness(lowLevelData),
        'bpm' : getBpm(lowLevelData),
        'spotifyURI' : spotifyPlayback.getSpotifyURI(title=title, artist=artist, album=album)
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
    with open('testSongData.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictList)
    return dictList

def makeCsv(filePath):
    df = pd.read_csv(filePath, header=0, sep='\t')
    mbids = df.recordingmbid.to_list()
    count = int(len(mbids)/25)
    keys = ['title','artist','album','danceable', 'not_danceable', 'genre_cla', 
            'genre_dan','genre_hip', 'genre_jaz', 'genre_pop', 'genre_rhy', 'genre_roc', 'genre_spe',
            'mood_cluster1', 'mood_cluster2', 'mood_cluster3', 'mood_cluster4', 'mood_cluster5', 
            'timbre_bright', 'timbre_dark', 'instrumental', 'voice', 'loudness','bpm', 'spotifyURI']
    for i in range(count):
        songsDict = get25IDs(i, mbids)
        # dictList.append(songsDict)
        # keys = songsDict[0].keys()
        with open('songData2.csv', 'a', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            # dict_writer.writeheader()
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

makeCsv('acousticbrainz-mediaeval-discogs-validation.tsv')

