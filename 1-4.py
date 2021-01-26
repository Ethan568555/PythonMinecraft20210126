#檔名1-4
from mcpi .minecraft import Minecraft
import time
pe = Minecraft.create()
x = 200
y = 200
z = 100

pe.player.setTilePos(x,y,z)
time.sleep(2)

x = 150
y = 250
pe.player.setTilePos(y,x,z)

x=100
y=300
pe.player.setTilePos(y,x,z)
time.sleep(2)

x=50
y=350
pe.player.setTilePos(y,x,z)
time.sleep(2)