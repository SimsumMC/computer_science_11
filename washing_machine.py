# tisch.py

from grafikfenster import *
from math import radians

from furniture import MoveType, Furniture


### ---------------------------------------------------
class WashingMaschine(Furniture):
    def GibFigur(self):
        """definiert und transformiert die zu zeichnende Figur"""
        gc = Zeichenflaeche.GibZeichenflaeche().GibGC()
        path = gc.CreatePath()

        # normale

        mid = 30
        path.AddCircle(mid, mid, 25)
        path.AddCircle(mid, mid, 3)
        path.AddRectangle(0, 0, 60, 60)

        gc.PushState()
        gc.Translate(self.x + self.b / 2, self.y + self.t / 2)
        gc.Rotate(radians(self.w))
        gc.Translate(-self.b / 2, -self.t / 2)
        transformation = gc.GetTransform()
        gc.PopState()
        path.Transform(transformation)
        return path