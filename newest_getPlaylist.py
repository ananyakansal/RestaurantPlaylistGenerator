import numpy as np
import pandas as pd
from random import seed
from random import randint
import math
import random
from collections import deque
from operator import itemgetter

global queue
queue = deque()
global list1
list1 = []

staticList = []

class SelectionError(Exception):
    pass

    
def getStaticList():
    global staticList
    return staticList

def setStaticList(genre=None, mood=None, timbre=None, instrument=None, tempo=None, dance=None):
    global staticList
    staticList = []
    staticList = setStaticListHelper(genre=genre[0], mood=mood, timbre=timbre, instrument=instrument, tempo=tempo, dance=dance)
    if len(genre) > 1:
        for i in range(1, len(genre)):
            tempList = setStaticListHelper(genre[i], mood, timbre, instrument, tempo, dance)
            staticList = staticList + tempList
        staticList = sorted(staticList)
    if not staticList:
        raise SelectionError("Please make a new selection")
    a,staticList = map(list,zip(*staticList))

def setStaticListHelper(genre=None, mood=None, timbre=None, instrument=None, tempo=None, dance=None):
    global list1
    global staticList

    # Classical
    if genre == 'classical' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaAggBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'classical' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaAggBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'classical' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaAggDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'classical' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaAggDarVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'classical' and mood == 'aggressive' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaAggSloNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'classical' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaButBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'classical' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaBitBriInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'classical' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaBitBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'classical' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaBitBriVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'classical' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaBitDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'classical' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaBitDarInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'classical' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaBitDarVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'classical' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaBitDarVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'classical' and mood == 'cheerful' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaCheBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'classical' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaCheBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'classical' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaCheBriVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'classical' and mood == 'cheerful' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaCheDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'classical' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/ClaDan.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'classical' and mood == 'humorous' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaHumNot.csv')
        list1 = np.transpose(df1.values.tolist())

    # Dance
    if genre == 'dance' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/DanAggBriInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'dance' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/DanAggBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
    
    if genre == 'dance' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/DanAggDarInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
    
    if genre == 'dance' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/DanAggDarVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'dance' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/DanNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'dance' and mood == 'passionate' or mood == 'cheerful' or mood == 'bittersweet' or mood == 'humorous' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/DanNotaggInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'dance' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/DanSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    # Hip Hop
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast':
        df1 = pd.read_csv('songDataCSVs/HipAggBriInsFas.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/HipAggBriInsSlo.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast':
        df1 = pd.read_csv('songDataCSVs/HipAggBriVoiFas.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/HipAggBriVoiSlo.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/HipAggDarInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/HipAggDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/HipAggDarInsSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
    
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/HipAggDarInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/HipAggDarVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/HipAggDarVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/HipAggDarVoiSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/HipAggDarVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'bittersweet' :
        df1 = pd.read_csv('songDataCSVs/HipBit.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'humorous' :
        df1 = pd.read_csv('songDataCSVs/HipHum.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'hiphop' and mood == 'passionate' or mood == 'cheerful' :
        df1 = pd.read_csv('songDataCSVs/HipPas&Che.csv')
        list1 = np.transpose(df1.values.tolist())
       
    # Jazz
    if genre == 'jazz' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/JazAggBriInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazAggBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/JazAggDarInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazAggDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'jazz' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice':
        df1 = pd.read_csv('songDataCSVs/JazAggDarVoi.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'jazz' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice':
        df1 = pd.read_csv('songDataCSVs/JazAggDarVoi.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'jazz' and mood == 'aggressive' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/JazAggSlo.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'jazz' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazBitBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazBitBriInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazBitBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazBitBriVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'bittersweet' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/JazBitDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazBitDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazBitDarInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazBitDarVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'jazz' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazBitDarVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
    
    if genre == 'jazz' and mood == 'cheerful' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazCheBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
          
    if genre == 'jazz' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazCheBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
          
    if genre == 'jazz' and mood == 'cheerful' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/JazCheDan.csv')
        list1 = np.transpose(df1.values.tolist())
         
    if genre == 'jazz' and mood == 'cheerful' and timbre == 'dark' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazCheDarFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
          
    if genre == 'jazz' and mood == 'cheerful' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/JazCheSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
          
    if genre == 'jazz' and mood == 'passionate' or mood == 'humorous':
        df1 = pd.read_csv('songDataCSVs/JazPas&Hum.csv')
        list1 = np.transpose(df1.values.tolist())
         
    # Pop
    if genre == 'pop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopAggBriInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopAggBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' :
        df1 = pd.read_csv('songDataCSVs/PopAggBriInsSlo.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopAggBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopAggBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopAggBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/PopAggBriVoiSlo.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and ance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopAggDarInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and ance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopAggDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'pop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'slow' and ance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopAggDarInsSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
         
    if genre == 'pop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'slow' and ance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopAggDarInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and ance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopAggDarVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and ance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopAggDarVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow' and ance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopAggDarVoiSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow' and ance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopAggDarVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopBitBriInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopBitBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' :
        df1 = pd.read_csv('songDataCSVs/PopBitBriInsSlo.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopBitBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopBitBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopBitBriVoiSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopBitBriVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
             
    if genre == 'pop' and mood == 'bittersweet' and timbre == 'dark':
        df1 = pd.read_csv('songDataCSVs/PopBitDar.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'cheerful' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopCheBriInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'cheerful' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopCheBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'cheerful' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/PopCheBriInsSlo.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopCheBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopCheBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopCheBriVoiSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopCheBriVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'cheerful' and timbre == 'dark':
        df1 = pd.read_csv('songDataCSVs/PopCheDar.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'humorous' and timbre == 'bright' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/PopHumBriSlo.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'pop' and mood == 'humorous' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/PopHumBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'humorous' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/PopHumBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'humorous' and timbre == 'dark':
        df1 = pd.read_csv('songDataCSVs/PopHumDar.csv')
        list1 = np.transpose(df1.values.tolist())
        
    if genre == 'pop' and mood == 'passionate':
        df1 = pd.read_csv('songDataCSVs/PopPas.csv')
        list1 = np.transpose(df1.values.tolist())
        
    # Rhythmic
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyAggBriInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyAggBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/RhyAggBriInsSlo.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyAggBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyAggBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/RhyAggBriVoiSlo.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyAggDarInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyAggDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyAggDarInsSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyAggDarInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyAggDarVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyAggDarVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/RhyAggDarVoiSlo.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitBriInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/RhyBitBriInsSlo.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitBriVoiSloDan.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitBriVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitDarInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitDarInsSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitDarInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitDarVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitDarVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitDarVoiSloDan.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rhythmic' and mood == 'bittersweet' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyBitDarVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rhythmic' and mood == 'cheerful' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyCheBriInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'cheerful' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyCheBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'cheerful' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyCheBriInsSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rhythmic' and mood == 'cheerful' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyCheBriInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rhythmic' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyCheBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyCheBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RhyCheBriVoiSloDan.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rhythmic' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RhyCheBriVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rhythmic' and mood == 'cheerful' and timbre == 'dark' :
        df1 = pd.read_csv('songDataCSVs/RhyCheDar.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'humorous' :
        df1 = pd.read_csv('songDataCSVs/RhyHum.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rhythmic' and mood == 'passionate' :
        df1 = pd.read_csv('songDataCSVs/RhyPas.csv')
        list1 = np.transpose(df1.values.tolist())

    # Rock
    if genre == 'rock' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocAggBriInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocAggBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/RocAggBriInsSlo.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rock' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocAggBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocAggBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocAggBriVoiSloDan.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'aggressive' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocAggBriVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocAggDarInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'aggressive' and timbre == 'dark' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocAggDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocAggDarInsSloDan.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rock' and mood == 'aggressive' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocAggDarInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rock' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocAggDarVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocAggDarVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocAggDarVoiSloDan.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'aggressive' and timbre == 'dark' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocAggDarVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())
            
    if genre == 'rock' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocBitBriInsFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocBitBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'instrumental' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/RockBitBriInsSlo.csv')
        list1 = np.transpose(df1.values.tolist())
      
    if genre == 'rock' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocBitBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocBitBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'bittersweet' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/RocBitBriVoiSlo.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'bittersweet' and timbre == 'dark' and tempo == 'fast':
        df1 = pd.read_csv('songDataCSVs/RocBitDarFas.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'bittersweet' and timbre == 'dark' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/RocBitDarSlo.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'cheerful' and timbre == 'bright' and instrument == 'instrumental':
        df1 = pd.read_csv('songDataCSVs/RocCheBriIns.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocCheBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocCheBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocCheBriVoiSloDan.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'cheerful' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocCheBriVoiSloNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'cheerful' and timbre == 'dark':
        df1 = pd.read_csv('songDataCSVs/RocCheDar.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'humorous' and timbre == 'bright' and instrument == 'instrumental':
        df1 = pd.read_csv('songDataCSVs/RocHumBriIns.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'humorous' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'dance':
        df1 = pd.read_csv('songDataCSVs/RocHumBriVoiFasDan.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'humorous' and timbre == 'bright' and instrument == 'voice' and tempo == 'fast' and dance == 'not_dance':
        df1 = pd.read_csv('songDataCSVs/RocHumBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())
       
    if genre == 'rock' and mood == 'humorous' and timbre == 'bright' and instrument == 'voice' and tempo == 'slow':
        df1 = pd.read_csv('songDataCSVs/RocHumBriVoiSlo.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'humorous' and timbre == 'dark' :
        df1 = pd.read_csv('songDataCSVs/RocHumDar.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'passionate' and tempo == 'fast' :
        df1 = pd.read_csv('songDataCSVs/RocPasFas.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre == 'rock' and mood == 'passionate' and tempo == 'slow' :
        df1 = pd.read_csv('songDataCSVs/RocPasSlo.csv')
        list1 = np.transpose(df1.values.tolist())
        
    # staticList = list1[24]
    if len(list1) == 0:
        return list1
    merged_list = list(zip(list1[23], list1[24]))
    return merged_list

def initQueue():
    global queue
    queue.append(randomNext())
    queue.append(randomNext())
    queue.append(randomNext())
    # print(queue)

def playQueue(useSPL, spl=None):
    global queue
    if (not useSPL):
        queue.append(randomNext())
    elif splAvg(spl) == None:
        queue.append(randomNext())
    else:
        queue.append(splNext(splAvg(spl)))
    return queue.popleft()

def randomNext():
    seed()
    ind = randint(0, len(staticList))
    song = staticList.pop(ind)
    while ('Not Found' in song):
        ind = randint(0, len(staticList))
        song = staticList.pop(ind)
    return song

def splNext(spl):
    ind = gaussian_pick(spl, staticList)
    song = staticList.pop(ind)
    while ('Not Found' in song):
        ind = gaussian_pick(spl, staticList)
        song = staticList.pop(ind)
    return song

def splAvg(songSPL):
    if songSPL is None:
        return None
    if len(songSPL) ==  0:
        return None
    return sum(songSPL)/len(songSPL)

def gaussian_pick(ave,static_list): # takes in 'ave': spl value and the (length of the) static playlist
    # this generates a gaussian white noise
    mean = 0
    std = 1
    num_samples = 100
    samples = np.random.normal(mean, std, size=num_samples)
    # this adds the spl value to the gaussian white noise
    # the spl == now a range of values centered around the 'ave' value
    samples = samples+ave
    # divide the spl range (-50 to -5) according to the playlist length
    # find the nearest value of the min and max in the spl range, and map the index to the playlist
    ranking = np.linspace(-50,-5,len(static_list))
    def find_nearest(array,value):
        idx = np.searchsorted(array, value, side="left")
        if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
            return idx-1
        else:
            return idx
    #gives range of index
    picks = [find_nearest(ranking,min(samples)),find_nearest(ranking,max(samples))]
    #gives one random index
    onepick = random.randint(picks[0],picks[1]) 
    return(onepick)
    # or return(onepick)

def getQueue():
    temp = []
    temp.append(queue[0])
    temp.append(queue[1])
    temp.append(queue[2])
    return temp


# initStaticLists()
# setStaticList(['classical'], 'aggressive', 'bright', 'instrumental', 'fast', 'not_dance')
# print(getStaticList())
# # print(randomNext())
# initQueue()


