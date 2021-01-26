from mcpi .minecraft import Minecraft
pe = Minecraft.create()
x,y,z=pe.player.getTilePos()

long=50
big=50
high=50

block=46
air=-0

pe.setBlocks(x,y,z,x+long,y+high,z+big,block)
pe.setBlocks(x+1,y+1,z+1,x+long-1,y+high-1,z+big-1,air)