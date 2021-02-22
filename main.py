import numpy as np
import matplotlib as plt
from random import *
import struct

x = 0
y = 0
z = 0
RunningParticleCounter = 0

ParticleDensity = input("desired particle concentration(% full): ")
xSize = input("xSize: ")
ySize = input("ySize: ")
zSize = input("zSize: ")

StartingObstacleParticles = np.zeros([int(zSize),int(ySize),int(xSize)])
print(StartingObstacleParticles)

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
                print("placing obstacle center at:", x, y, z)

                values = (1, 'ab', 2.7)
                s = struct.Struct('I 2s f')
                packed = s.pack(*values)
                RunningObstacleParticles[z,y,x] = packed

                RunningParticleCounter = RunningParticleCounter  + 1


            #print("x increment")
            x = x + 1

        y = y + 1

    z = z + 1

print(RunningObstacleParticles)
print("number of obstacles is:", RunningParticleCounter, "total number of spots is:", int(zSize) * int(ySize) * int(xSize))
print("real percent particles is:", int(zSize) * int(ySize) * int(xSize) / RunningParticleCounter)
