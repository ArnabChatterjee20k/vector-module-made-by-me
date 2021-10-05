#TODO: making a class for vector
import math
class Vector:
    object_created=0
    convention={
        "i":"x-axis",
        "j":"y-axis",
        "k":"z-axis"
    }
    def __init__(self,magnitude,direction):
        self.magnitude=magnitude
        self.direction=direction.lower()
        Vector.object_created+=1
    def axis(self):
        return(f"the object of magnitude {self.magnitude} is going towards {Vector.convention[self.direction]}")

    @staticmethod
    def vectors_object():
        return(f"Total vector objects created:{Vector.object_created}")

    def __add__(self,other):
        a=self.magnitude
        b=other.magnitude
        if self.direction==other.direction:
            resltant= math.sqrt( a**2 + b**2 + 2*a*b )
            return(f"the resultant is {resltant}")
    
    def __repr__(self):
        return "Vector Object"
# a=Vector(2,"i")
# a=Vector(2,"i")
# print(a+a)
# print(a.axis())
# print(Vector.vectors_object())
