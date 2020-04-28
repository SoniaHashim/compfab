"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "jenniferjacobs"
__modifiedby__ = "soniahashim"

import rhinoscriptsyntax as rs
import Rhino.Geometry as geom
from datetime import datetime
import math as math
import random
import time

random.seed(time.time())

# Hard code temperatures
BedTemp = 60
NozzleTemp = 205

# Hard code layer height
LayerHeight = .25

def makeGcodeInfo(sb):
    sb.append("; " + datetime.now().strftime("%y%m%d_%H%M%S") + "\n")

def makeGcodeHeatSettings(sb):
    sb.append("M140 S" + str(BedTemp) +" ; Set Bed Temperature\n")
    sb.append("M105\n")
    sb.append("M190 S" + str(BedTemp) +" ; Wait for Bed Temperature\n")
    sb.append("M104 S" + str(NozzleTemp) +" ; Set Nozzle Temperature\n")
    sb.append("M105\n")
    sb.append("M109 S" + str(NozzleTemp) +" ; Wait for Nozzle Temperature\n")

def makeGcodeStartupSettings(sb):
    sb.append("G28\n")
    sb.append("M83\n")
    sb.append("G90\n")
    sb.append("G1 F300 Z0.1\n")
    sb.append("G1 X50 E8 F800\n")


def WriteFile(str, path):

    f = open(path, "w")
    f.write(str)
    f.close()

def makeRetraction(amount, speed, sign):
    mes = "";
    if(sign == -1):
        mes = " ; Retraction"
    else:
        mes = " ; Extraction"
    return "G1 F" + str(speed) + " E" + str(sign * amount) + mes + "\n"

def makeGcodeSpeed(fr, to, speed):

    crvpts.append(to)
    pts.append(to)

    l = (to - fr).Length
    numerator = (_NozzleWidth * l * LayerHeight)
    denominator = (_rfil / 2) * (_rfil / 2) * math.pi

    e = numerator / denominator

    return "G1 F" + str(speed) + " X" + "{:.{}f}".format(to.X,2) + " Y" + "{:.{}f}".format(to.Y,2) + " E" + "{:.{}f}".format(e,8) + "\n"

def makeGcode(to):
    return "G0 F9000 X" + "{:.{}f}".format(to.X,2) + " Y" + "{:.{}f}".format(to.Y,2) + "\n"



crvpts = []
_LayerHeight = LayerHeight;
_NozzleWidth = 0.4;
_RetAmount = 6.0;
_RetSpeed = 1200;
PrintSpeed = 3000;
PrintSpeedHigh = 1000;
_rfil = 1.75

# Params
height = 5.7
nLayers = (int) (height / LayerHeight)
ncore = 21
r_inner = 33
tx = r_inner + ncore*_rfil
ty = tx
s = 300
strsb = ''

p_switch = 0.5
ap = 0

pts = []
apply = True
if(apply == True):
    # Set up print
    sb = []
    makeGcodeInfo(sb)
    makeGcodeHeatSettings(sb)
    makeGcodeStartupSettings(sb)
    sb.append(makeRetraction(_RetAmount, _RetSpeed, -1))
    p_last = geom.Point3d.Origin

    # For every height...
    for k in range(0, nLayers):
        # Extrude height for new set of rings
        sb.append("G0 F300 Z" + str(k*LayerHeight) + "\n")

        # For every ring...
        for i in range(0,ncore):

            # Calculate ring size
            r = r_inner+i*.5
            theta = 10
            npoints = (int)(360/theta)

            # For every point on the ring...
            for p in range(npoints):
                a = math.radians(theta)
                x = r*math.cos(p*a+ap)+tx
                y = r*math.sin(p*a+ap)+ty

                xn = r*math.cos((p+1)*a+ap)+tx
                yn = r*math.sin((p+1)*a+ap)+ty
                p_fr = geom.Point3d(x,y,k)
                p_to = geom.Point3d(xn,yn,k)

                # If this is the first point in the set of rings and there is
                # a layer of previous rings, connect the first point to the last
                # in the old set of rings
                if k != 0 and i== 0 and p == 0:
                    p_last.Z = k
                    sb.append(makeGcodeSpeed(p_last, p_fr, PrintSpeed))

                # If this is the first point in the ring and there is a previous
                # ring, connect the first point to the last point in the old ring
                if i != 0 and p == 0:
                    sb.append(makeGcodeSpeed(p_last, p_fr, PrintSpeed))

                # Extrude filament to make up one side of ring in the print
                sb.append(makeGcodeSpeed(p_fr, p_to, PrintSpeed))
                p_last = p_to

                if (i < 14 and p > 5*npoints/6) or (i >= 14 and p > npoints/8):
                    if random.random() > p_switch:
                        ap = (p+1)*a+ap
                        break



    sb.append(makeRetraction(_RetAmount, _RetSpeed, -1))
    height += 10;
    sb.append("G1 Z" + "{:.{}f}".format(height*1.0,3) + "\n");

    sb.append("M84");
    strsb = ''.join(sb)
    WriteFile(strsb, fname);


# print(strsb)
b = rs.AddInterpCurve(crvpts, degree = 1)
a = pts
