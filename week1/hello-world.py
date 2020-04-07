"""Provides a scripting component.
    Inputs:
        p1: The origin point
        p2: The other grid control point
        rx: The interval spacing
        mod: The value for modulo ops
        mtype: The type of modulo operand
        rad: The radius of the form
    Output:
        a: The a output variable"""

__author__ = "soniahashim"

import rhinoscriptsyntax as rs

''' print hello world'''
print("hello world")

''' dist squared func '''
def dist2(a,b):
    return (a.X-b.X)*(a.X-b.X) + (a.Y-b.Y)*(a.Y-b.Y) + (a.Z-b.Z)*(a.Z-b.Z)

''' select mod operand '''
if mtype == 0:
    op = lambda x,y: x*x - y*y
elif mtype == 1:
    op = lambda x,y: x*x + y*y
elif mtype == 2:
    op = lambda x,y: x*y
else:
    op = lambda x,y: x*y+y+1

''' Center of form '''
pcenter = .5*p1+.5*p2

''' Square of radius '''
rad2 = rad*rad

''' create list of points '''
pt = []
dx = (p2.X - p1.X)/(rx-1)
ry = int(0.5+(p2.Y-p1.Y)/dx)
for i in range(0,ry+1):
    for j in range(0,rx):
        x = p1.X + j*dx
        y = p1.Y + i*dx

        if op(i,j)%mod == 0:
            p = rs.CreatePoint(x,y,0.0)
            d = dist2(p, pcenter)
            if d < rad2:
                z = 0.02*d
                pt.append(rs.CreatePoint(x,y,z))

a = pt


''' create list of lines '''
ln = []
d2 = dist*dist
for j in range(0,len(pt)):
    for i in range(0,len(pt)):
        if i != j and dist2(pt[i],pt[j]) < d2:
            ln.append(rs.AddLine(pt[i],pt[j]))

b = ln
