# tisch.py

from grafikfenster import *


class MoveType:
    horizontal = 1
    vertical = 2
    angle = 3


### ---------------------------------------------------
class Furniture:
    """Klasse Tisch
    ermoeglicht das Zeichnen und Bearbeiten eines
    Tisch-Symbols fuer den Raumplaner"""
    def __init__(self, x, y, b, t, w, f, sichtbar):
        self.x = x
        self.y = y
        self.b = b
        self.t = t
        self.w = w
        self.f = f
        self.s = sichtbar
        if sichtbar:
            self.Zeige()

    def GibFigur(self):
        return None

    def GibFarbe(self):
        """Get-Methode fuer die Farbe"""
        return self.f

    def GibSichtbar(self):
        """Get-Methode fuer die Sichtbarkeit"""
        return self.s

    def BewegeHorizontal(self, weite):
        """Veraendernde Methode fuer die x-Position"""
        self.Verberge()
        self.x += weite
        self.Zeige()

    def move(self, move_type: MoveType, value):
        self.Verberge()

        if move_type == MoveType.horizontal:
            self.x += value
        elif move_type == MoveType.vertical:
            self.y += value
        elif move_type == MoveType.angle:
            self.w += value
        else:
            raise ValueError(f"MoveType does not exist!")
        self.Zeige()

    def BewegeHorizontal(self, weite):
        """Veraendernde Methode fuer die x-Position"""
        self.Verberge()
        self.x += weite
        self.Zeige()

    def BewegeVertikal(self, weite):
        """Veraendernde Methode fuer die y-Position"""
        self.Verberge()
        self.y += weite
        self.Zeige()

    def Drehe(self, winkel):
        """Veraendernde Methode fuer die Orientierung [Winkel]"""
        self.Verberge()
        self.w += winkel
        self.Zeige()

    def Verberge(self):
        """Veraendernde Methode fuer die Sichtbarkeit mit Wert False"""
        self.s = False
        Zeichenflaeche.GibZeichenflaeche().Entferne(self)

    def Zeige(self):
        """Veraendernde Methode fuer die Sichtbarkeit mit Wert True"""
        self.s = True
        Zeichenflaeche.GibZeichenflaeche().Zeichne(self)


### ---------------------------------------------------
class FurnitureApp(wx.App):
    """Test-Anwendung speziell fuer Tisch"""

    def OnInit(self):
        self.fenster = GrafikFenster(None, "Raumplaner-Grafik")
        self.SetTopWindow(self.fenster)
        self.fenster.Show(True)
        self.fenster.panel.Refresh()
        self.fenster.ZeigeShellFrame()
        # self.fenster.ZeigeFillingFrame()
        self.TestAnwendung()
        return True

    def TestAnwendung(self):
        """Allein fuer die Testanwendung:"""
        Furniture(True)


### ---------------------------------------------------
if __name__ == "__main__":
    app = FurnitureApp(redirect=False)
    # Parameterwert True, wenn Ausgaben in der Standard E/A angezeigt werden sollen
    app.MainLoop()
