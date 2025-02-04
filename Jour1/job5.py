class Point:
    def  __init__(self,x,y):
        self.x=x
        self.y=y

    def afficherLesPoints(self):
        coordonees=((self.x,self.y))
        print(self.x)
        print(self.y)

coord=Point('x','y')
coord.afficherLesPoints()