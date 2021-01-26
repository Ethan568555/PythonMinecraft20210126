from mcpi .minecraft import Minecraft
pe = Minecraft.create()
x,y,z, = mc.player.getTilePos

pe.setBlock(x,y,z+1,7)
pe.setBlock(x,y,z-1,7)
pe.setBlock(x-1,y,z,7)
pe.setBlock(x+1,y,z,7)
pe.setBlock(x-1,y,z+1,7)
pe.setBlock(x+1,y,z+1,7)
pe.setBlock(x-1,y,z+1,7)
pe.setBlock(x+1,y,z-1,7)
pe.setBlock(x-1,y,z-1,7)