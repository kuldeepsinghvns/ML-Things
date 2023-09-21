class Angle:
    def __init__(self,angle) -> None:
        while angle >=360:
            angle-=360
        while angle<0:
            angle+=360
        self.angle=angle
    def __str__(self) -> str:
        return "Angle={0}".format(self.angle)
    def __add__(self,aman):
        return Angle(self.angle+aman.angle)
    def __sub__(aman,smart):
        return Angle(aman.angle-smart.angle)
a=Angle(366)
print(a)
a=Angle(360)
print(a)
a=Angle(-366)
print(a)
a=Angle(18)
print(a+a)
print(Angle(19.05))
        
        