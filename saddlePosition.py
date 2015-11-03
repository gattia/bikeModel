# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:53:29 2015

@author: gatti
"""

import math 

def seatPosition (inseam, seatTubeAngle):
    saddleHeight = 0.883 * inseam   # 1.11 to bottom of pedal spindle or can use 0.883 to bottom bracket. 
    saddleX = math.cos(math.radians(seatTubeAngle)) * saddleHeight 
    saddleY = math.sin(math.radians(seatTubeAngle)) * saddleHeight
    saddleCentre = [saddleX, saddleY]
    return (saddleX, saddleY, saddleCentre)
    