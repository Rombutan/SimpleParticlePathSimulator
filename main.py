#----------------------------------------------------Setup--------------------------------------------------------


import numpy as np
import matplotlib as plt
from random import *
import struct

x = 0
y = 0
z = 0
xSpeed = 0
ySpeed = 0
zSpeed = 0
RunningParticleCounter = 0
TickCounter = 0

ParticleDensity = input("desired particle concentration(% full): ")
xSize = input("xSize: ")
ySize = input("ySize: ")
zSize = input("zSize: ")
oSize = input("particle 1 size: ")
oSpeed = input("Points Per Tick Max: ")
sTicks = input("Total Ticks to simulate: ")

#----------------------------------------------------Obstacle Creation--------------------------------------------------------


StartingObstacleParticles = np.zeros([int(zSize),int(ySize),int(xSize),4])
#print(StartingObstacleParticles)

RunningObstacleParticles = StartingObstacleParticles

while(z < int(zSize)):
    y = 0
    #print("z increment")

    while(y < int(ySize)):
        x = 0
        #print("y increment")

        while(x < int(xSize)):
            random = randint(0,101)
            #print("random int:", random)

            if(random < int(ParticleDensity)):
                #print("placing obstacle center at:", x, y, z)

                xSpeed = random(0,int(oSpeed))
                ySpeed = random(0,int(oSpeed))
                zSpeed = random(0,int(oSpeed))

                RunningObstacleParticles[z,y,x,0] = RunningParticleCounter
                RunningObstacleParticles[z,y,x,1] = xSpeed
                RunningObstacleParticles[z,y,x,2] = ySpeed
                RunningObstacleParticles[z,y,x,2] = zSpeed
                RunningObstacleParticles[z,y,x,2] = oSize


                RunningParticleCounter = RunningParticleCounter  + 1


            #print("x increment")
            x = x + 1

        y = y + 1

    z = z + 1

#print(RunningObstacleParticles)
print("number of obstacles is:", RunningParticleCounter, "total number of spots is:", int(zSize) * int(ySize) * int(xSize))
print("real percent particles is:", int(zSize) * int(ySize) * int(xSize) / RunningParticleCounter)

x = 0
y = 0
z = 0
xSpeed = 0
ySpeed = 0
zSpeed = 0
RunningParticleCounter = 0
TickCounter = 0
#----------------------------------------------------TICK LOOP--------------------------------------------------------

while(TickCounter < sTicks):
    while(z < int(zSize)):
        y = 0
        #print("z increment")

        while(y < int(ySize)):
            x = 0
            #print("y increment")

            while(x < int(xSize)):
                print(x,y,z)
                x = x + 1

            y = y + 1

        z = z + 1
