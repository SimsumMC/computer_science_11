# tisch.py

from grafikfenster import *
from math import radians

from furniture import Furniture
from shelf import Shelf


### ---------------------------------------------------
class MoreShelfs(Furniture):
    """Klasse Tisch
    ermoeglicht das Zeichnen und Bearbeiten eines
    Tisch-Symbols fuer den Raumplaner"""

    def GibFigur(self):
        """definiert und transformiert die zu zeichnende Figur"""

        gc = Zeichenflaeche.GibZeichenflaeche().GibGC()
        path = gc.CreatePath()

        path.AddRectangle(0, 0, 400, 300)
        y = 0
        while y < 300:
            path.AddLineToPoint(0, y)
            path.AddLineToPoint(400, y)
            y = y + 300 / 3
        """
        schrank1 = Shelf(b=self.b / 3)
        schrank2 = Shelf(b=self.b / 3)
        schrank3 = Shelf(b=self.b / 3)
        schrank2.BewegeHorizontal(self.b / 3)
        schrank3.BewegeHorizontal(self.b / 3 * 2)

        # einzel schränke standard position berücksichtigen

        path.AddPath(schrank1.GibFigur())
        path.AddPath(schrank2.GibFigur())
        path.AddPath(schrank3.GibFigur())

        for shelf in [schrank1, schrank2, schrank3]:
            shelf.Verberge()
        
        """

        """
        gc.PushState()
        gc.Translate(self.x + self.b / 2, self.y + self.t / 2)
        gc.Rotate(radians(self.w))
        gc.Translate(-self.b / 2, -self.t / 2)
        transformation = gc.GetTransform()
        gc.PopState()
        path.Transform(transformation)
        """

        gc.PushState()
        gc.Translate(self.x + self.b / 2, self.y + self.t / 2)
        #gc.Rotate(radians(self.w))
        gc.Translate(-self.b / 2, -self.t / 2)
        transformation = gc.GetTransform()
        gc.PopState()
        path.Transform(transformation)

        return path
