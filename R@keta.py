import math
import matplotlib.pyplot as mpp

MODEL_G = 10
MODEL_DT = 0.8
MODEL_M = 0.9

class Body:
    def __init__(self, x, y, vx, vy):

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
        self.trajectory_x = []
        self.trajectory_y = []
        

    def advance(self):
        
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT

    def plot(self):
         mpp.plot(self.trajectory_x,self.trajectory_y)
         mpp.show()



class Rocket(Body):

    def __init__(self,x,y,vx,vy,m,a,v):
        super().__init__(x,y,vx,vy)

        self.m = m
        self.a = a
        self.v = v

    def advance(self):
        super().advance()

        if self.m > 10:
            F = MODEL_M * self.v / MODEL_DT
            self.a = F / self.m
            self.vy -= MODEL_G * MODEL_DT - self.a * MODEL_DT
        else:
            self.vy -= MODEL_G * MODEL_DT

        self.m -= MODEL_M      

        
R = Rocket(1,2,6,3,40,5,70)
B = Body(8,9,10,11)

for a in range(10000):
    R.advance()
    B.advance()

R.plot()
B.plot()
