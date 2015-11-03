# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:52:08 2015

@author: gatti

Bicycling Biomechanical Model 
"""
import math
import numpy 
import scipy 
import matplotlib.pyplot as plt
from saddlePosition import seatPosition
from anthropometrics import anthropometrics


def jointCentre (startX, startY, angle, length):
    jointX = startX + (math.cos(math.radians(angle)) * (length)) 
    jointY = startY + (math.sin(math.radians(angle)) * (length))
    jointCentre = numpy.hstack((jointX, jointY))
    return (jointX, jointY, jointCentre)

height = int(raw_input("What is the individuals height? "))
weight = int(raw_input(" What is the individuals weight?"))
crankArm = int(raw_input("What is your crank arm length? "))
seatTubeAngle = (int(raw_input("What is your seat tube anlge? (normal is 73 degrees)")))


thigh, shank, foot, ankleHeight, inseam = anthropometrics (height, weight)

saddleX, saddleY, saddleCentre = seatPosition(inseam, seatTubeAngle)

seatHeight = 0.883 * (ankleHeight + thigh + shank) # 1.11 to bottom of pedal spindle or can use 0.883 to bottom bracket. 

bottomBracket = [0, 0]






ankleAngles = [10, 0 , 20 , 20]
ankleAngleOneChange = float(ankleAngles[1] - ankleAngles[0])
ankleAngleTwoChange = float(ankleAngles[2] - ankleAngles[1])
ankleAngleThreeChange = float(ankleAngles[3] - ankleAngles[2])
ankleAngleFourChange = float(ankleAngles[0] - ankleAngles[3])

ankleIncrementOne = ankleAngleOneChange/90
ankleIncrementTwo = ankleAngleTwoChange/90
ankleIncrementThree = ankleAngleThreeChange/90
ankleIncrementFour = ankleAngleFourChange/90

ankleOne = numpy.zeros(shape=(90))
ankleTwo = numpy.zeros(shape=(90))
ankleThree = numpy.zeros(shape=(90))
ankleFour = numpy.zeros(shape=(90))

for i in range (90):
    ankleOne[i] = ankleAngles[0] + (ankleIncrementOne * i)
    ankleTwo[i] = ankleAngles[1] + (ankleIncrementTwo * i)
    ankleThree[i] = ankleAngles[2] + (ankleIncrementThree * i)
    ankleFour[i] = ankleAngles[3] + (ankleIncrementFour * i)

ankleRotation = numpy.hstack((ankleOne, ankleTwo, ankleThree, ankleFour))
 #angles taken from bini document and dynamic measurements @ 6 o'clock position
#crankAngle = 180
#ankleAngle = 139   # B
#footAngle = 20  #A
#shankAngle = ankleAngle - footAngle
#kneeAngle = 180 - 38
#thighAngle = kneeAngle - shankAngle

#ANGLES FROM BINI PAPER - & 6 o'clock - Static 

crankAngle = 180
footAngle = 45
ankleAngle = 131
shankAngle = ankleAngle - footAngle
kneeAngle = 180 - 30
thighAngle = kneeAngle - shankAngle

#ANGLES FROM BINI PAPER - & 3 o'clock 
#crankAngle = 90
#footAngle = 40
#ankleAngle = 125
#shankAngle = ankleAngle - footAngle
#kneeAngle = 180 - 62
#thighAngle = kneeAngle - shankAngle

#inverseKneeAngle = (180 - shankAngle) + thighAngle

spindleX = math.sin(math.radians(crankAngle)) * crankArm 
spindleY = math.cos(math.radians(crankAngle)) * crankArm 
spindle = numpy.hstack((spindleX, spindleY))

ankleCentreX, ankleCentreY, ankleCentre = jointCentre (spindleX, spindleY, footAngle, foot)
kneeCentreX, kneeCentreY, kneeCentre = jointCentre (ankleCentreX, ankleCentreY, shankAngle, shank)
hipCentreX, hipCentreY, hipCentre = jointCentre (kneeCentreX, kneeCentreY, thighAngle, thigh)

ankleCenterX = spindleX - (math.cos(math.radians(footAngle)) * (foot)) 
ankleCenterY = (math.sin(math.radians(footAngle)) * (foot)) + spindleY
ankleCenter = numpy.hstack((ankleCenterX, ankleCenterY))

kneeCenterX = ankleCenterX + (math.cos(math.radians(shankAngle)) * shank) 
kneeCenterY = (math.sin(math.radians(shankAngle)) * shank) + ankleCenterY
kneeCenter = numpy.hstack((kneeCenterX, kneeCenterY))

hipCenterX = kneeCenterX - math.cos(math.radians(thighAngle)) * thigh 
hipCenterY = math.sin(math.radians(thighAngle)) * thigh + kneeCenterY
hipCenter = numpy.hstack((hipCenterX, hipCenterY))

print spindle, ankleCenter, kneeCenter, hipCenter, saddleCenter

jointCenters = numpy.vstack ((bottomBracket, spindle, ankleCenter, kneeCenter, hipCenter))
jointCentersX = jointCenters[:,0]
jointCentersY = jointCenters[:,1]

plt.plot(jointCentersX, jointCentersY)
plt.plot(saddleCenter[0], saddleCenter[1])
plt.axis([-20, 80, -20, 80])

