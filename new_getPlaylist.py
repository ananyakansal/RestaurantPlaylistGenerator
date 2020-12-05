import numpy as np
import pandas as pd
from random import seed
from random import randint
from collections import deque

global queue
queue = deque()
global list1
list1 = []
    
def getStaticList():
    global staticList
    return staticList

def setStaticList(genre=None, mood=None, timbre=None, instrument=None, tempo=None, dance=None):
    global list1
    global staticList

# Classical
    if genre is 'classical' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaAggBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre is 'classical' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaAggBriVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre is 'classical' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaAggDarInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre is 'classical' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaAggDarVoiFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre is 'classical' and mood is 'aggressive' and tempo is 'slow' and dance is 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaAggSloNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre is 'classical' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaButBriInsFasNot.csv')
        list1 = np.transpose(df1.values.tolist())

    if genre is 'classical' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' and dance is 'not_dance':
        df1 = pd.read_csv('songDataCSVs/ClaBitBriInsSloNot.csv')
        list1 = np.transpose(df1.values.tolist())

#     if genre is 'classical' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('ClaBitBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'classical' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('ClaBitBriVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'classical' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('ClaBitDarInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'classical' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('ClaBitDarInsSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'classical' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('ClaBitDarVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'classical' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('ClaBitDarVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'classical' and mood is 'cheerful' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('songDataCSVs/ClaCheBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'classical' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('songDataCSVs/ClaCheBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'classical' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('ClaCheBriVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'classical' and mood is 'cheerful' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('ClaCheDarInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'classical' and dance is 'dance':
#         df1 = pd.read_csv('ClaDan.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'classical' and mood is 'humorous' and dance is 'not_dance':
#         df1 = pd.read_csv('ClaHumNot.csv')
#         list1 = np.transpose(df1.values.tolist())

#     # Dance
#     if genre is 'dance' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('DanAggBriInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'dance' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('DanAggBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
    
#     if genre is 'dance' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('DanAggDarInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
    
#     if genre is 'dance' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('DanAggDarVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'dance' and dance is 'not_dance':
#         df1 = pd.read_csv('DanNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'dance' and mood is 'passionate' or mood is 'cheerful' or mood is 'bittersweet' or mood is 'humorous' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('DanNotaggInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'dance' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('DanSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     # Hip Hop
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast':
#         df1 = pd.read_csv('HipAggBriInsFas.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow':
#         df1 = pd.read_csv('HipAggBriInsSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast':
#         df1 = pd.read_csv('HipAggBriVoiFas.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow':
#         df1 = pd.read_csv('HipAggBriVoiSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('HipAggDarInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('HipAggDarInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('HipAggDarInsSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
    
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('HipAggDarInsSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('HipAggDarVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('HipAggDarVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('HipAggDarVoiSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('HipAggDarVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'bittersweet' :
#         df1 = pd.read_csv('HipBit.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'humorous' :
#         df1 = pd.read_csv('HipHum.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'hiphop' and mood is 'passionate' or mood is 'cheerful' :
#         df1 = pd.read_csv('HipPas&Che.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     # Jazz
#     if genre is 'jazz' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('JazAggBriInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('JazAggBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('JazAggDarInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('JazAggDarInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'jazz' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice':
#         df1 = pd.read_csv('JazAggDarVoi.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'jazz' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice':
#         df1 = pd.read_csv('JazAggDarVoi.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'jazz' and mood is 'aggressive' and tempo is 'slow':
#         df1 = pd.read_csv('JazAggSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'jazz' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('JazBitBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('JazBitBriInsSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('JazBitBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('JazBitBriVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'bittersweet' and dance is 'dance':
#         df1 = pd.read_csv('JazBitDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('JazBitDarInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('JazBitDarInsSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('JazBitDarVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'jazz' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('JazBitDarVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
    
#     if genre is 'jazz' and mood is 'cheerful' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('JazCheBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
          
#     if genre is 'jazz' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('JazCheBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
          
#     if genre is 'jazz' and mood is 'cheerful' and dance is 'dance':
#         df1 = pd.read_csv('JazCheDan.csv')
#         list1 = np.transpose(df1.values.tolist())
         
#     if genre is 'jazz' and mood is 'cheerful' and timbre is 'dark' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('JazCheDarFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
          
#     if genre is 'jazz' and mood is 'cheerful' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('JazCheSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
          
#     if genre is 'jazz' and mood is 'passionate' or mood is 'humorous':
#         df1 = pd.read_csv('JazPas&Hum.csv')
#         list1 = np.transpose(df1.values.tolist())
         
#     # Pop
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('PopAggBriInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('PopAggBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' :
#         df1 = pd.read_csv('PopAggBriInsSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('PopAggBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('PopAggBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('PopAggBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow':
#         df1 = pd.read_csv('PopAggBriVoiSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and ance is 'dance':
#         df1 = pd.read_csv('PopAggDarInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and ance is 'not_dance':
#         df1 = pd.read_csv('PopAggDarInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'pop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'slow' and ance is 'dance':
#         df1 = pd.read_csv('PopAggDarInsSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
         
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'slow' and ance is 'not_dance':
#         df1 = pd.read_csv('PopAggDarInsSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and ance is 'dance':
#         df1 = pd.read_csv('PopAggDarVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and ance is 'not_dance':
#         df1 = pd.read_csv('PopAggDarVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow' and ance is 'dance':
#         df1 = pd.read_csv('PopAggDarVoiSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow' and ance is 'not_dance':
#         df1 = pd.read_csv('PopAggDarVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('PopBitBriInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('PopBitBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' :
#         df1 = pd.read_csv('PopBitBriInsSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('PopBitBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('PopBitBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('PopBitBriVoiSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('PopBitBriVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
             
#     if genre is 'pop' and mood is 'bittersweet' and timbre is 'dark':
#         df1 = pd.read_csv('PopBitDar.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'cheerful' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('PopCheBriInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'cheerful' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('PopCheBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'cheerful' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow':
#         df1 = pd.read_csv('PopCheBriInsSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('PopCheBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('PopCheBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('PopCheBriVoiSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('PopCheBriVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'cheerful' and timbre is 'dark':
#         df1 = pd.read_csv('PopCheDar.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'humorous' and timbre is 'bright' and tempo is 'slow':
#         df1 = pd.read_csv('PopHumBriSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'pop' and mood is 'humorous' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('PopHumBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'humorous' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('PopHumBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'humorous' and timbre is 'dark':
#         df1 = pd.read_csv('PopHumDar.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     if genre is 'pop' and mood is 'passionate':
#         df1 = pd.read_csv('PopPas.csv')
#         list1 = np.transpose(df1.values.tolist())
        
#     # Rhythmic
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RhyAggBriInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyAggBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow':
#         df1 = pd.read_csv('RhyAggBriInsSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RhyAggBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyAggBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow':
#         df1 = pd.read_csv('RhyAggBriVoiSlo.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RhyAggDarInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyAggDarInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('RhyAggDarInsSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyAggDarInsSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RhyAggDarVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyAggDarVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow':
#         df1 = pd.read_csv('RhyAggDarVoiSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RhyBitBriInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyBitBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow':
#         df1 = pd.read_csv('RhyBitBriInsSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RhyBitBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyBitBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('RhyBitBriVoiSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyBitBriVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RhyBitDarInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyBitDarInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('RhyBitDarInsSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyBitDarInsSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RhyBitDarVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyBitDarVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('RhyBitDarVoiSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rhythmic' and mood is 'bittersweet' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyBitDarVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rhythmic' and mood is 'cheerful' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RhyCheBriInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'cheerful' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyCheBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'cheerful' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('RhyCheBriInsSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rhythmic' and mood is 'cheerful' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyCheBriInsSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rhythmic' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RhyCheBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyCheBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('RhyCheBriVoiSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rhythmic' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('RhyCheBriVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rhythmic' and mood is 'cheerful' and timbre is 'dark' :
#         df1 = pd.read_csv('RhyCheDar.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'humorous' :
#         df1 = pd.read_csv('RhyHum.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rhythmic' and mood is 'passionate' :
#         df1 = pd.read_csv('RhyPas.csv')
#         list1 = np.transpose(df1.values.tolist())

#     # Rock
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RocAggBriInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RocAggBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow':
#         df1 = pd.read_csv('RocAggBriInsSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RocAggBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RocAggBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('RocAggBriVoiSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'aggressive' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('RocAggBriVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RocAggDarInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'dark' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RocAggDarInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('RocAggDarInsSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('RocAggDarInsSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RocAggDarVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RocAggDarVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('RocAggDarVoiSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'aggressive' and timbre is 'dark' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('RocAggDarVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())
            
#     if genre is 'rock' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RocBitBriInsFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RocBitBriInsFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'instrumental' and tempo is 'slow':
#         df1 = pd.read_csv('RockBitBriInsSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
      
#     if genre is 'rock' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RocBitBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RocBitBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'bittersweet' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow':
#         df1 = pd.read_csv('RocBitBriVoiSlo.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'bittersweet' and timbre is 'dark' and tempo is 'fast':
#         df1 = pd.read_csv('RocBitDarFas.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'bittersweet' and timbre is 'dark' and tempo is 'slow':
#         df1 = pd.read_csv('RocBitDarSlo.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'cheerful' and timbre is 'bright' and instrument is 'instrumental':
#         df1 = pd.read_csv('RocCheBriIns.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RocCheBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RocCheBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'dance':
#         df1 = pd.read_csv('RocCheBriVoiSloDan.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'cheerful' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow' and dance is 'not_dance':
#         df1 = pd.read_csv('RocCheBriVoiSloNot.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'cheerful' and timbre is 'dark':
#         df1 = pd.read_csv('RocCheDar.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'humorous' and timbre is 'bright' and instrument is 'instrumental':
#         df1 = pd.read_csv('RocHumBriIns.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'humorous' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'dance':
#         df1 = pd.read_csv('RocHumBriVoiFasDan.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'humorous' and timbre is 'bright' and instrument is 'voice' and tempo is 'fast' and dance is 'not_dance':
#         df1 = pd.read_csv('RocHumBriVoiFasNot.csv')
#         list1 = np.transpose(df1.values.tolist())
       
#     if genre is 'rock' and mood is 'humorous' and timbre is 'bright' and instrument is 'voice' and tempo is 'slow':
#         df1 = pd.read_csv('RocHumBriVoiSlo.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'humorous' and timbre is 'dark' :
#         df1 = pd.read_csv('RocHumDar.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'passionate' and tempo is 'fast' :
#         df1 = pd.read_csv('RocPasFas.csv')
#         list1 = np.transpose(df1.values.tolist())

#     if genre is 'rock' and mood is 'passionate' and tempo is 'slow' :
#         df1 = pd.read_csv('RocPasSlo.csv')
#         list1 = np.transpose(df1.values.tolist())
        
    staticList = list1[24]
    return staticList

def initQueue():
    global queue
    queue.append(randomNext())
    queue.append(randomNext())
    queue.append(randomNext())
    print(queue)

def addToQueue():
    global queue
    queue.append(randomNext())

def playQueue():
    global queue
    queue.append(randomNext())
    print(queue)
    return queue.popleft()

def randomNext():
    seed()
    ind = randint(0, len(staticList))
    song = staticList.pop(ind)
    while ('Not Found' in song):
        ind = randint(0, len(staticList))
        song = staticList.pop(ind)
    return song

def getQueue():
    temp = []
    temp.append(queue[0])
    temp.append(queue[1])
    temp.append(queue[2])
    return temp

# initStaticLists()
setStaticList('classical', 'aggressive', 'bright', 'instrumental', 'fast', 'not_dance')
print(getStaticList())
# # print(randomNext())
# initQueue()


