import random as rnd
import matplotlib.pyplot as plt
from math import sqrt,cos,sin,atan2

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,p):
        return sqrt(abs(self.x - p.x)*abs(self.x - p.x) + abs(self.y - p.y)*abs(self.y - p.y))


def nearPoint(p1,p2):
    if p1.distance(p2)<10 :
        return True
    else:
        return False

def get_random_point(maxx,maxy):
    x = rnd.randint(0,maxx)
    y = rnd.randint(0,maxy)
    p = Point(x,y)
    return p


def get_a_point_along_the_line(startPoint,endPoint,distance):
    theta = atan2(endPoint.y-startPoint.y,endPoint.x-startPoint.x)
    return Point(startPoint.x + distance*cos(theta), startPoint.y +distance*sin(theta))

def get_next_point(p1,p2,distance):
    if(p1.distance(p2))<distance:
        return p2
    else:
        return get_a_point_along_the_line(p1,p2,distance)


class Graph():
    #Goal point
    #Start point
    def __init__(self,startPoint,GoalPoint,length):
        self.startPoint = startPoint
        self.GoalPoint = GoalPoint
        self.length = length
    
    def rtt(self,maxDistance,iterations):
        plt.axis([0, 800, 0, 800])
        plt.plot([self.startPoint.x],[self.startPoint.y],"bs")
        plt.plot([self.GoalPoint.x],[self.GoalPoint.y],"g^")
        nodes = []
        nodes.append(self.startPoint)
        while iterations>0:
            randomPoint = get_random_point(self.length,self.length)
            nn = nodes[0]
            for p in nodes:
                if randomPoint.distance(p) < randomPoint.distance(nn):
                    nn = p
            distance = randomPoint.distance(nn)
            newPoint = get_next_point(nn,randomPoint,distance)
            plt.plot([nn.x,newPoint.x],[nn.y,newPoint.y],"r-")
            nodes.append(newPoint)
            if(nearPoint(self.GoalPoint,newPoint)):
                plt.plot([newPoint.x],[newPoint.y],"rs")
                break
            plt.show()
            iterations -= 1

#         x = []
#         y = []
#         for i in nodes:
#             x.append(i.x)
#             y.append(i.y)
#         plt.plot(x,y,'ro')
        




graph = Graph(Point(10,10),Point(530,530),800)
graph.rtt(10,2000)

        


        
