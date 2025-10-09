from math import sqrt
class Point:
    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y

class Line:
    def __init__(self, point1:Point, point2:Point):
        self.point1=point1
        self.point2=point2

    def slope(self):
        slope=(self.point1.y-self.point2.y)/(self.point1.x-self.point2.x)

        if int(slope)==slope:
            return int(slope)
        return slope

    def length(self):
        delx=(self.point1.x-self.point2.x)
        dely=(self.point1.y-self.point2.y)
        ans=sqrt(delx**2+dely**2)
        if int(ans)==ans:
            return int(ans)
        return ans

p1=Point(0,0)
p2=Point(3,4)

a=Line(p1,p2)

print(a.slope())
print(a.length())



