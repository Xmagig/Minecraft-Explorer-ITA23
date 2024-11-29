from mcpi.minecraft import Minecraft
from Wall import WallWithWindow
from Wall import WallWithDoor
from Wall import Wall
from Wall import Roof
from gpiozero import Button
import time


class Hous():
    def __init__(self):
        mc =Minecraft.create()
        self.pos = mc.player.getPos()


        self.backwall = Wall(mc,pos=self.pos)
        self.backwall.ofset = True
        self.frontdoor = WallWithDoor(mc,False)
        self.frontdoor.pos=self.pos

        self.rightwindow =WallWithWindow(mc,True)
        self.rightwindow.pos=self.pos
        

        self.leftwindow = WallWithWindow(mc,True)
        self.leftwindow.pos=self.pos
        self.leftwindow.ofset = True
        

        self.roof = Roof(mc,pos=self.pos)
    def build(self):
        self.backwall.build()
        self.frontdoor.build()
        self.rightwindow.build()
        self.leftwindow.build()
        self.roof.build()
    
    def change_wall_material(self,new_material_id):
        self.backwall.material_id = new_material_id
        self.frontdoor.material_id = new_material_id
        self.rightwindow.material_id = new_material_id
        self.leftwindow.material_id = new_material_id

        
def main():
    hous1 = Hous()
    hous1.change_wall_material(49)
    hous1.build()


if __name__ == "__main__":
    main()