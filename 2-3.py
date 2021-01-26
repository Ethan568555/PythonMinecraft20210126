from mcpi .minecraft import Minecraft
pe = Minecraft.create()

import random,time
while True:
    x,y,z=pe.player.getTilePos()
    color = random.randrange(0,16)
    pe.setBlocks(x+50,y,z+50,x-50,y,z-50,95,color)

time.sleep(1)
