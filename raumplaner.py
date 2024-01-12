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
        """
        tisch_1 = Tisch(True)
        tisch_1.BewegeHorizontal(50)
        tisch_1.BewegeVertikal(50)

        stuhl_1 = Stuhl(True)
        stuhl_1.BewegeHorizontal(50)
        stuhl_1.BewegeVertikal(40)

        stuhl_4 = Stuhl(True)
        stuhl_4.BewegeHorizontal(230)
        stuhl_4.BewegeVertikal(40)
        stuhl_4.Drehe(180)

        stuhl_2 = Stuhl(True)
        stuhl_2.BewegeHorizontal(110)
        stuhl_2.BewegeVertikal(-20)
        stuhl_2.Drehe(90)

        stuhl_3 = Stuhl(True)
        stuhl_3.BewegeHorizontal(170)
        stuhl_3.BewegeVertikal(-20)
        stuhl_3.Drehe(90)

        stuhl_5 = Stuhl(True)
        stuhl_5.BewegeHorizontal(110)
        stuhl_5.BewegeVertikal(100)
        stuhl_5.Drehe(-90)

        stuhl_6 = Stuhl(True)
        stuhl_6.BewegeHorizontal(170)
        stuhl_6.BewegeVertikal(100)
        stuhl_6.Drehe(-90)
        """

        x = MoreShelfs()
        x.Drehe(90)




### ---------------------------------------------------
if __name__ == "__main__":
    app = MyApp(redirect=False)
    # Parameterwert True, wenn Ausgaben in der Standard E/A angezeigt werden sollen
    app.MainLoop()
