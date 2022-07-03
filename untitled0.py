from mcpi.minecraft import Minecraft
import time

time.sleep(2)
mc = Minecraft.create()
position = mc.player.getTilePos()
t = 0

"""
while True:
    mc.postToChat("哈囉!!")
"""
  
while True : 
    t = t+1
    mc.postToChat("第"+str(t)+"次")
    
    