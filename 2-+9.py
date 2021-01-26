from mcpi .minecraft import Minecraft
pe = Minecraft.create()

x,y,z, = pe.player.getTilePos()
pe.setSign(x,y,z+1,63,0,"I love minecraft,and"
           ,"I love Python")