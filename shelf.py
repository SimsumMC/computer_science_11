# tisch.py

from grafikfenster import *
from math import radians

from furniture import Furniture


### ---------------------------------------------------
class Shelf(Furniture):
    """Klasse Tisch
    ermoeglicht das Zeichnen und Bearbeiten eines
    Tisch-Symbols fuer den Raumplaner"""

    def GibFigur(self):
        """definiert und transformiert die zu zeichnende Figur"""
        gc = Zeichenflaeche.GibZeichenflaeche().GibGC()
        path = gc.CreatePath()

        # normale
        path.AddLineToPoint(self.b, 0)
        path.AddLineToPoint(0, self.t)

        path.AddLineToPoint(self.b, self.t)
        path.AddLineToPoint(0, 0)

        path.AddRectangle(0, 0, self.b, self.t)

        gc.PushState()
        gc.Translate(self.x + self.b / 2, self.y + self.t / 2)
        gc.Translate(-self.b / 2, -self.t / 2)
        transformation = gc.GetTransform()
        gc.PopState()
        path.Transform(transformation)
        return path
