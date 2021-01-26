from mcpi .minecraft import Minecraft
pe = Minecraft.create()
userName = input("write your name")
message = input("speak you idiot!!!!!!!!!!!!")
pe.postToChat(" <"+userName + "> " + message)