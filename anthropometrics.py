# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:04:23 2015

@author: gatti
"""

def anthropometrics (height, weight):
    #anthropometrics taken from exrx.net http://www.exrx.net/Kinesiology/Segments.html     
    # Segment length from height - for males only 
    thigh = 0.232 * height    # female 0.249 
    shank = 0.247 * height    # female 0.257
    foot = 14     # 30 is my whole foot - 14 is from the 1st metatarsal to the malleolus & 0.0425 * height is formula to calc foot length (this is weight though)   femal same 
    ankleHeight = 4  # this was taken form my navicular. 
    inseam = ankleHeight + thigh + shank
    
    # segment wieghts 
    thighWeight = 0.105 * weight   #female 0.105
    shankWeight = 0.0475 * weight   #female 0.0475
    footWeight = 0.0143 * weight    # female 0.0133
    
    # segment CofM - from proximal end
    
    thighCOM = 0.433 * thigh     #female = 0.428
    shankCOM = 0.434 * shank     #female = 0.434
    footCOM = 0.5 * foot           # female = 0.5 
    
    return (thigh, shank, foot, ankleHeight, inseam)