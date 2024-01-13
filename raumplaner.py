# Raumplaner-Anfangsprojekt.py
# Anfangsprojekt ohne Kapselung (in Stuhl und Tisch)
# So sollte man es also eigentlich nicht machen!

from more_shelfs import MoreShelfs

from shelf import *


### ---------------------------------------------------
class MyApp(wx.App):
    """Testanwendung fuer Raumplaner-Grafik
    ShellFrame: Interaktion mit laufender Anwendung
    FillingFrame: Anzeige der Umgebung"""

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
        stuhl_1 = Stuhl(x, y, b, t, w, f, True)
        




### ---------------------------------------------------
if __name__ == "__main__":
    app = MyApp(redirect=False)
    # Parameterwert True, wenn Ausgaben in der Standard E/A angezeigt werden sollen
    app.MainLoop()
