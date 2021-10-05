import math
class Vector:
    convention={
        "i":"x-axis",
        "j":"y-axis",
        "k":"z-axis"
    }
    def __init__(self,magnitude1,direction1,magnitude2,direction2,angle_between_vectors):
        self.vector1=(magnitude1,direction1)
        self.vector2=(magnitude2,direction2)
        self.angle=angle_between_vectors
        
    def resultant(self):
        a=self.vector1[0]
        b=self.vector2[0]
        angle=self.angle
        resultant=math.sqrt( (a**2) + (b**2) + round(2*a*b*math.cos(math.radians(angle)),0) )
        return resultant
    def __add__(self,other):
        pass
# print(Vector(12,2,3,4).vector1)
# print(a.resultant())
# b=math.cos( math.radians(90))
# print(round(b,0))

a=Vector(2,None,2,None,90)
