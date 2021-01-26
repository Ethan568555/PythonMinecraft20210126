
from mcpi .minecraft import Minecraft
pe = Minecraft.create()

while True:
    x,y,z, = pe.player.getTilePos()
    block1=pe.getBlock(x,y-1,z)
    block2=pe.getBlock(x+1,y-1,z)
    block3=pe.getBlock(x-1,y-1,z)
    block4=pe.getBlock(x,y-1,z+1)
    block5=pe.getBlock(x,y-1,z-1)
    if block1 == 8 or block1 == 9 or block2 == 8 or block2 == 9\
    or block3 == 8 or block3 == 9 or block4 == 8 or block4 == 9\
    or block5 == 8 or block5 == 9:
        pe.setBlock(x,y-1,z,7)
        pe.setBlock(x,y-1,z+1,7)
        pe.setBlock(x,y-1,z-1,7)
        pe.setBlock(x+1,y-1,z,7)
        pe.setBlock(x-1,y-1,z,7)