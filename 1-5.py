from mcpi .minecraft import Minecraft
pe = Minecraft.create()
import time

y=0
while True:
    y = y+1
    
    pe.postToChat("第"+str(i)+次)
    time.sleep(3)