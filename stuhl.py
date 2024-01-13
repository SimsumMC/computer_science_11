# stuhl.py

from grafikfenster import *
from math import radians

from furniture import Furniture


### ---------------------------------------------------

class Stuhl(Furniture):
    def __init__(self, x, y, b, t, w, f, sichtbar):
        super().__init__(x, y, b, t, w, f, sichtbar)

    def GibFigur(self):
        """definiert und transformiert die zu zeichnende Figur"""
        gc = Zeichenflaeche.GibZeichenflaeche().GibGC()
        path = gc.CreatePath()

        # normale

        path.AddLineToPoint(20, 50)
        path.AddLineToPoint(self.b - 20, 50)

        x = 20
        for n in range(17):
            path.MoveToPoint(x, 50)
            path.AddLineToPoint(x, 50)
            path.AddLineToPoint(x, 60)

            x += 5

        path.AddRectangle(0, 0, self.b, self.t)

        gc.PushState()
        gc.Translate(self.x + self.b / 2, self.y + self.t / 2)
        gc.Rotate(radians(self.w))
        gc.Translate(-self.b / 2, -self.t / 2)
        transformation = gc.GetTransform()
        gc.PopState()
        path.Transform(transformation)
        return path
