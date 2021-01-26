from mcpi .minecraft import Minecraft
pe = Minecraft.create()
x,y,z=pe.player.getTilePos()

pe.setBlock(x,y,z+1,30)
pe.setBlock(x,y,z-1,30)
pe.setBlock(x-1,y,z,30)
pe.setBlock(x+1,y,z,30)
pe.setBlock(x-1,y,z,30)
pe.setBlock(x+1,y,z+1,30)
pe.setBlock(x-1,y,z+1,30)
pe.setBlock(x+1,y,z-1,30)
pe.setBlock(x-1,y,z-1,30)