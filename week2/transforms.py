"""Provides a scripting component.
    Inputs:
        c: The curve that specifies the transformation
        g: The base geometry to transform
        o: The offset for stacking / nesting
        s: The scale factor for iteratively created geometries
        N: The number of objects to create
    Output:
        a: The a output variable"""

__author__ = "soniahashim"

import rhinoscriptsyntax as rs
import Rhino.Geometry as geom
import math

'''
method: init_transform
params: i; initial curve that specifies the transformation
-------------------------------------------------------------
Constructs a change of basis using input curve (assumes curve
starts at the origin). Scale factor determined by length of
curve. Translates geometry to end of curve.
'''
def init_transform(i):
    p0 = i.PointAtStart
    p1 = i.PointAtEnd

    # Calculate inital basis and scale factor
    t0 = p1-p0; v0 = geom.Vector3d(t0)
    v2 = rs.CreateVector(0,0,1)
    v1 = geom.Vector3d.CrossProduct(v0,v2)
    v2 = geom.Vector3d.CrossProduct(v0,v1)
    scaleFactor = t0.Length/5

    # Normalize constructed basis
    v0.Unitize()
    v1.Unitize()
    v2.Unitize()

    # Standard basis
    e0 = geom.Vector3d.XAxis
    e1 = geom.Vector3d.YAxis
    e2 = geom.Vector3d.ZAxis

    # Get change of basis transform (standard --> curve)
    b = geom.Transform.ChangeBasis(e0,e1,e2,v0,v1,-v2)

    # Get scale transform matching scale factor set by curve length
    s = geom.Transform.Scale(geom.Point3d.Origin,scaleFactor)

    # Get translation transform to curve endpoint
    r = geom.Transform.Translation(t0)

    # Return geometry in new basis, scaled, and translated
    return b

'''
method: scale
params: x,y,z; scale factors in x,y,z
-------------------------------------------------------------
Returns an affine scale matrix that scales by x, y, z
'''
def scale(x,y,z):
    t = geom.Transform.Identity
    t.M00 = x
    t.M11 = y
    t.M22 = z
    return t;

'''
method: translate
params: x,y,z; translation in x,y,z
-------------------------------------------------------------
Returns an affine translation matrix that translates by x,y,z
'''
def translate(x,y,z):
    t = geom.Transform.Identity
    t.M03 = x
    t.M13 = y
    t.M23 = z
    return t

'''
method: rotateZ
params: theta; degree in angles
-------------------------------------------------------------
Returns an affine transformation matrix that rotates around
the z axis by the specified amount
'''
def rotateZ(theta):
    t = geom.Transform.Identity
    a = math.radians(theta)
    t.M00 = math.cos(a)
    t.M01 = -math.sin(a)
    t.M10 = math.sin(a)
    t.M11 = math.cos(a)
    return t

# Set initial transformation of geometry
t = init_transform(c)
g.Transform(t)
f = (c.PointAtEnd - c.PointAtStart).Length/15
t = scale(f,f,f)
g.Transform(t)


h0 = o    # height offset
# s = .85 # iterative scaling
# N = 5   # number of objects

w = 0
objects = []
# Create series via iteration to make N objects
for i in range(0,N):
    x = g.Duplicate()
    if i != 0:
        w += (s**(i-1))*(1+s)*h0
        t = scale(s**i, s**i, s**i)
        x.Transform(t)
        t = translate(0, 0, w)
        x.Transform(t)
        t = rotateZ(i*90)
        x.Transform(t)
    objects.append(x)


a = objects
