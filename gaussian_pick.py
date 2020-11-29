import numpy as np
import matplotlib.pyplot as plt
import math
import random

def gaussian_pick(ave,static_list): # takes in 'ave': spl value and the (length of the) static playlist
    # this generates a gaussian white noise
    mean = 0
    std = 1
    num_samples = 100
    samples = np.random.normal(mean, std, size=num_samples)
    # this adds the spl value to the gaussian white noise
    # the spl is now a range of values centered around the 'ave' value
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
    return(picks)
    # or return(onepick)
