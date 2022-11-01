from asyncio.windows_events import NULL
from dis import dis
from locale import currency
from math import sqrt
import re
from tkinter import N
from turtle import st


class Square:
    def __init__(self,startX,startY,length):
        self.startX = startX
        self.startY = startY
        self.length = length
    


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Gcost = 0
        self.Hcost = 0
        self.Fcost = 0
        self.parent = None
    def setParent(self, parent):
        self.parent = parent

    def setGcost(self, gcost):
        self.Gcost = gcost

    def setHcost(self, hcost):
        self.Hcost = hcost

    def setFcost(self):
        self.Fcost = self.Gcost + self.Hcost

    def distance(self, p):
        return sqrt((abs(self.x - p.x)*abs(self.x - p.x)) + (abs(self.y - p.y)*abs(self.y - p.y)))


def compare(x, y):
    if x.x == y.x and x.y == y.y:
        return True
    else:
        return False


def contains(list, node):
    for i in list:
        if(compare(i, node)):
            return True
    return False


def f_cost_key(obj):
    return obj.Fcost


def getNeighbours(node):
    list = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            checkX = node.x + x
            checkY = node.y + y
            if checkX >= 0 and checkX < 11 and checkY >= 0 and checkY < 11:
                list.append(Node(node.x+x, node.y+y))
    return list


def getDistance(a, b):
    distX = abs(a.x - b.x)
    distY = abs(a.y - b.y)

    if distX > distY:
        return 14*distX + 10 * (distX - distY)

    return 14*distX + 10 * (distY - distX)


def Astar(start, end):
    open = []
    close = set()
    open.append(start)
    # t = 10
    while len(open) > 0:
        current = open[0]
        for i in open:
            if(i.Fcost < current.Fcost or i.Fcost == current.Fcost and i.Hcost < current.Hcost):
                current = i
        open.remove(current)
        close.add(current)
        if compare(current, end):
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            for i in path:
                print(i.x,i.y)
            return
            
        neighbours = getNeighbours(current)
        for i in neighbours:
            if contains(close, i) or compare(i,Node(1,5)):
                continue
            movingCost = current.Gcost + i.distance(current)
            if movingCost < i.Gcost or (not contains(open, i)):
                i.setGcost(movingCost)
                i.setHcost(i.distance(end))
                i.setFcost()
                i.parent = current
                if not contains(open, i):
                    open.append(i)
        # t-=1


a = Node(1, 1)
b = Node(0, 10)
Astar(a, b)
# a = Node(1,1)
# print(a.distance(Node(1,0)))
# print(a.distance(Node(0,10)))


"""
0,0 - > 1.4 , 9.05

"""
