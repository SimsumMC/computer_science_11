# tisch.py

from grafikfenster import *
from math import radians

from furniture import MoveType, Furniture


### ---------------------------------------------------
class Tisch(Furniture):
    def GibFigur(self):
        """definiert und transformiert die zu zeichnende Figur"""
        gc = Zeichenflaeche.GibZeichenflaeche().GibGC()
        path = gc.CreatePath()

        path.AddRectangle(0, 0, self.b, self.t)

        #Add Line
        path.MoveToPoint(0, 0)
        path.AddLineToPoint(self.b, 0)
        path.AddLineToPoint(self.b * 1.1, self.t)
        path.AddLineToPoint(-self.b * 0.1, self.t)

        gc.PushState()
        gc.Translate(self.x + self.b / 2, self.y + self.t / 2)
        gc.Rotate(radians(self.w))
        gc.Translate(-self.b / 2, -self.t / 2)
        transformation = gc.GetTransform()
        gc.PopState()
        path.Transform(transformation)
        return path