


import json
import requests
import pandas as pd

resp = requests.get('https://acousticbrainz.org/api/v1/1d185361-aea5-417b-84d9-34c47c4dab16/high-level')
# if resp.status_code != 200:
#     # This means something went wrong.
#     raise ApiError('GET /tasks/ {}'.format(resp.status_code))
data = resp.json()

df =  pd.DataFrame(columns=['mbid', 'title', 'artist', 'album', 'dance', 'genre', 'mood', 'timbre', 'instrument'])

danceDict = data['highlevel']['danceability']['all']
genreDict = data['highlevel']['genre_rosamerica']['all']
mood_mirexDict = data['highlevel']['moods_mirex']['all']
mood_relaxedDict = data['highlevel']['mood_relaxed']['all']
moodsDict = mood_mirexDict.update(mood_relaxedDict)
timbreDict = data['highlevel']['timbre']['all']
instrumDict = data['highlevel']['voice_instrumental']['all']

song = {
    'mbid' : data['metadata']['tags']['acoustid_id'], 
    'title' : data['metadata']['tags']['title'], 
    'artist' : data['metadata']['tags']['artist'], 
    'album' : data['metadata']['tags']['album'], 
    'dance' : danceDict, 
    'genre' : genreDict, 
    'mood' : moodsDict, 
    'timbre' : timbreDict, 
    'instrument' : instrumDict
    }
df = df.append(song, ignore_index=True)
# df.to_csv(r'/Users/jocekav/Documents/GitHub/Group3ProjectStudio/df.csv', index=False)