from mcpi.minecraft import Minecraft #Importiert die python anbindung fuer minecraft reborn
mc = Minecraft.create()
class Wall():
    def __init__(self,mc,pos):
        self.width=6
        self.width= int(self.width)
        self.hight=5
        self.hight = int(self.hight)
        self.rotated = False
        self.ofset   = False
        self.material_id=1
        self.pos = pos
        self._mc = mc

    def build(self):
        ofset_value = 0 
        if self.ofset == True:
            ofset_value = self.width
            if self.rotated == False:
                ofset_value-=1       
            elif self.rotated== True:
                ofset_value-=1
        if self.rotated == False:
           # mc.setBlocks(xp+1,yp,zp-1,xp+self.width,yp+self.hight,zp-1,1)
            mc.setBlocks(self.pos.x+1           ,self.pos.y               ,self.pos.z-1-ofset_value,
                         self.pos.x+self.width  ,self.pos.y+self.hight-1  ,self.pos.z-1-ofset_value   ,self.material_id)
        elif self.rotated == True:
            mc.setBlocks(self.pos.x+self.width-ofset_value  ,self.pos.y               ,self.pos.z-1,
                         self.pos.x+self.width-ofset_value  ,self.pos.y+self.hight-1  ,self.pos.z-self.width   ,self.material_id)




class WallWithWindow(Wall):
    def __init__(self,mc,rotated):
        super().__init__(mc,rotated)
        self.rotated = rotated
    def build(self):
        super().build()
        ofset_value = 0 
        if self.ofset == True:
            ofset_value = self.width
            if self.rotated == False:
                ofset_value-=1       
            elif self.rotated== True:
                ofset_value-=1
        if self.rotated == False:
            mc.setBlocks(self.pos.x+self.width/2  ,self.pos.y+self.hight/2        ,self.pos.z-1-ofset_value,
                         self.pos.x+self.width/2+1  ,self.pos.y+self.hight/2+1    ,self.pos.z-1-ofset_value   ,20)
        elif self.rotated == True:
            mc.setBlocks(self.pos.x+self.width-ofset_value  ,self.pos.y+self.hight/2  ,self.pos.z-self.width/2,
                         self.pos.x+self.width-ofset_value  ,self.pos.y+self.hight/2+1  ,self.pos.z-self.width/2-1,20)


class WallWithDoor(Wall):
    def __init__(self,mc,rotated):
        super().__init__(mc,rotated)
        self.rotated = rotated
        self.door_material_id =0
    def build(self):
        super().build()
        ofset_value = 0 
        if self.ofset == True:
            ofset_value = self.width
            if self.rotated == False:
                ofset_value-=1       
            elif self.rotated== True:
                ofset_value-=1
        if self.rotated == False:
            mc.setBlocks(self.pos.x+self.width/2  ,self.pos.y+self.hight/2    ,self.pos.z-1-ofset_value,
                         self.pos.x+self.width/2+1  ,self.pos.y+(self.hight-4)/2    ,self.pos.z-1-ofset_value   ,self.door_material_id)
        elif self.rotated == True:
            mc.setBlocks(self.pos.x+self.width-ofset_value  ,self.pos.y+self.hight/2  ,self.pos.z-self.width/2,
                         self.pos.x+self.width-ofset_value  ,self.pos.y+(self.hight-4)/2  ,self.pos.z-self.width/2-1, self.door_material_id)



class Roof():
    def __init__(self,mc,pos):
        self.width = 6 
        #self.width = int(self.width)
        self.depth = 6
        #self.depth = int(self.depth)
        self.roof_material_id = 45 
        self.pos = pos
        self._mc = mc

    def build(self):
        mc.setBlocks(self.pos.x+1            ,self.pos.y+self.depth-1  ,self.pos.z-1,
                     self.pos.x+self.width ,self.pos.y+self.depth-1  ,self.pos.z+self.width*-1, self.roof_material_id)

def main():
    wall1 = WallWithDoor(mc,True)
    wall2 = WallWithDoor(mc,False)
    wall1.build()
    wall2.build()
    





if __name__ == "__main__":
    main()