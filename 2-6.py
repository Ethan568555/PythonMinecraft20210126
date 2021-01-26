from mcpi .minecraft import Minecraft
pe = Minecraft.create()


x,y,z = pe.player.getTilePos()

answer = int(input("你右邊要放甚麼方塊")）
pe.setBlock(x+1,y,z,answer)

