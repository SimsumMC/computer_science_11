# tisch.py
from washing_machine import *


### ---------------------------------------------------
class WonderfulPiano(Furniture):
    def GibFigur(self):
        """definiert und transformiert die zu zeichnende Figur"""
        gc = Zeichenflaeche.GibZeichenflaeche().GibGC()
        path = gc.CreatePath()

        # normale

        start_x = self.x * (20/70)
        start_height = self.y * 5
        key_height = self.y * 6

        path.AddLineToPoint(start_x, start_height)
        path.AddLineToPoint(self.b - start_x, start_height)

        for n in range(17):
            path.MoveToPoint(start_x, start_height)
            path.AddLineToPoint(start_x, start_height)
            path.AddLineToPoint(start_x, key_height)

            start_x += 5

        path.AddRectangle(0, 0, self.b, self.t)

        gc.PushState()
        gc.Translate(self.x + self.b / 2, self.y + self.t / 2)
        gc.Rotate(radians(self.w))
        gc.Translate(-self.b / 2, -self.t / 2)
        transformation = gc.GetTransform()
        gc.PopState()
        path.Transform(transformation)
        return path
