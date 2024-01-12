# grafikfenster.py
# Auf der Grundlage der wxPython Demo
# kommentierte Version
# Version 02'20 mit Bildexport und Absicherung bei self.gc

import wx
import colorsys

USE_BUFFER = "wxMSW" in wx.PlatformInfo  # use buffered drawing on Windows


### ---------------------------------------------------
class Zeichenflaeche(wx.Panel):
    """Die Klasse stellt eine Zeichenflaeche fuer Vektorgrafik bereit.
    Sie wendet das Singleton-Muster an, also kein Konstruktoraufruf,
    sondern Methode GibZeichenflaeche()"""

    __zeichenflaeche = None

    @staticmethod
    def GibZeichenflaeche(parent=None):
        if Zeichenflaeche.__zeichenflaeche == None:
            if parent == None:
                return None
            else:
                Zeichenflaeche.__zeichenflaeche = Zeichenflaeche(parent)
        return Zeichenflaeche.__zeichenflaeche

    def __init__(self, parent):
        """Konstruktor
        !nicht direkt aufrufen!"""
        wx.Panel.__init__(self, parent, -1)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        if USE_BUFFER:
            self.Bind(wx.EVT_SIZE, self.OnSize)
        self.objekte = []
        self.gc = None
        self.__image = None

    def OnSize(self, evt):
        """Ereignismethode, die beim Aendern der Groesse
        des fensters aufgerufen wird."""
        self.InitBuffer()
        evt.Skip()

    def OnPaint(self, evt):
        """Ereignismethode fuer das Zeichnen
        Die erste Anweisung ist im Unterschied zur Demo notwendig,
        um unter Windows beim ersten Zeichnen
        den Puffer richtig zu initialisieren"""
        self.InitBuffer()
        if USE_BUFFER:
            dc = wx.BufferedPaintDC(self, self._buffer)
        else:
            dc = wx.PaintDC(self)
            self.gc = self.MakeGC(dc)
            self.Draw(self.gc)

    def InitBuffer(self):
        """Initialisierungsmethode fuer den Zeichenpuffer"""
        sz = self.GetClientSize()
        sz.width = max(1, sz.width)
        sz.height = max(1, sz.height)
        self._buffer = wx.Bitmap(sz.width, sz.height, 32)
        dc = wx.MemoryDC(self._buffer)
        dc.SetBackground(wx.Brush("WHITE"))
        dc.Clear()
        self.gc = self.MakeGC(dc)
        self.Draw(self.gc)

    def MakeGC(self, dc):
        """erzeugt den 'Graphics-Context'"""
        try:
            gc = wx.GraphicsContext.Create(dc)
        except NotImplementedError:
            dc.DrawText(
                "This build of wxPython does not support the wx.GraphicsContext "
                "family of classes.",
                25,
                25,
            )
            return None
        self.gc = gc
        return gc

    def Draw(self, gc):
        """Die eigentliche Zeichenmethode
        wxPython transformiert den Zeichenpfad.
        Wenn man mehrfach Zeichnen will, muss man daher
        vor einer Transformation den Zustand sichern und
        anschliessend wiederherstellen."""
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetWeight(wx.BOLD)
        gc.SetFont(font, wx.BLACK)

        # weissen Hintergrund zeichnen
        back = gc.CreatePath()
        gc.PushState()  # save current translation/scale/other state
        back.AddRectangle(0, 0, self.GetClientSize().width, self.GetClientSize().height)
        gc.SetBrush(wx.Brush("white"))
        gc.FillPath(back)  # nur Fuellung
        gc.PopState()  # restore saved state

        for objekt in self.objekte:
            if objekt.GibFigur() == NotImplemented:
                continue
            if not (objekt.GibSichtbar()):
                continue
            ## Modellierung 02'20:
            ## Texte ermoeglichen, Sichtbarkeit abfragen
            gc.PushState()
            istText = False
            try:
                istText = objekt.IstText()
            except AttributeError as e:
                pass
            if istText:
                f = self._HoleFarbe(objekt.GibFarbe())
                if objekt.GibFont() != None:
                    gc.SetFont(objekt.GibFont(), f)
                else:
                    gc.SetFont(font, f)
                if versionsNummer == "2":
                    ## angle funktioniert nicht entgegen Doku
                    gc.Translate(objekt.GibX(), objekt.GibY())
                    gc.Rotate(-radians(objekt.GibWinkel()))
                    gc.DrawText(objekt.GibText(), 0, 0)
                else:
                    gc.DrawText(
                        objekt.GibText(),
                        objekt.GibX(),
                        objekt.GibY(),
                        radians(objekt.GibWinkel()),
                    )
            else:
                path = gc.CreatePath()
                path.AddPath(objekt.GibFigur())
                f = self._HoleFarbe(objekt.GibFarbe())
                if f == None:
                    f = wx.BLACK
                gc.SetPen(wx.Pen(f))
                try:
                    fuellFarbe = objekt.GibFuellFarbe()
                except AttributeError as e:
                    fuellFarbe = None
                if fuellFarbe != None:
                    ff = self._HoleFarbe(fuellFarbe)
                    if ff == None:
                        gc.StrokePath(path)
                    else:
                        gc.SetBrush(wx.Brush(ff))
                        gc.DrawPath(path)
                else:
                    gc.StrokePath(path)
            gc.PopState()

    def _HoleFarbe(self, farbe):
        if type(farbe) == tuple:
            if len(farbe) == 3:
                rot, gruen, blau = farbe
                f = wx.Colour(rot, gruen, blau)
            elif len(farbe) == 4:
                rot, gruen, blau, alpha = farbe
                f = wx.Colour(rot, gruen, blau, alpha)
            else:
                return None
        else:
            f = wx.TheColourDatabase.Find(farbe)
        if f[0] == -1:
            return None
        return f

    def Zeichne(self, objekt):
        """Erweiterungen für das Raumplanerprojekt:
        Ruft nacheinander das Zeichnen fuer alle Objekte auf."""
        if objekt in self.objekte:
            self.objekte.remove(objekt)
        self.objekte.append(objekt)
        self.Refresh()

    def Entferne(self, objekt):
        """Entfernt ein Objekt aus der Darstellung."""
        if objekt in self.objekte:
            self.objekte.remove(objekt)
        self.Refresh()

    def GibGC(self):
        """Gibt den aktuellen Graphics-Context zurueck."""
        if self.gc == None:
            self.InitBuffer()
        return self.gc

    def GibPfad(self):
        """Gibt einen Zeichenpfad zurueck."""
        if self.gc == None:
            self.InitBuffer()
        return self.gc.CreatePath()

    def BildExport(self, dateiname):
        """exportiert im png- oder jpg-Format"""
        self.InitBuffer()
        typ = dateiname.partition(".")[2].upper()
        if not (typ in ("PNG", "JPG")):
            return "Dateityp png oder jpg"
        self.__image = self._buffer.ConvertToImage()
        bitmap_type = {"PNG": wx.BITMAP_TYPE_PNG, "JPG": wx.BITMAP_TYPE_JPEG}[typ]
        try:
            with open(dateiname, "wb") as bild_datei:
                self.__image.SaveFile(dateiname, bitmap_type)
        except IOError as ioerr:
            return "Dateifehler: " + str(ioerr)


### ---------------------------------------------------
from wx.py.shell import ShellFrame
from wx.py.filling import FillingFrame


### ---------------------------------------------------
class GrafikFenster(wx.Frame):
    """
    Die Klasse GrafikFenster erzeugt einen Frame.
    """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, pos=(20, 50), size=(400, 400))
        if wx.PlatformInfo[1] == "wxMSW":
            self.SetSize((400, 420))
        self.panel = Zeichenflaeche.GibZeichenflaeche(self)
        self.shellFrame = ShellFrame(parent=self, pos=wx.Point(450, 100))
        self.fillingFrame = FillingFrame(parent=self, pos=wx.Point(40, 500))

    def ZeigeShellFrame(self, zeigen=True):
        """Zeigt die interaktive Shell an."""
        self.shellFrame.Show(zeigen)

    def ZeigeFillingFrame(self, zeigen=True):
        """Zeigt den Monitor an."""
        self.fillingFrame.Show(zeigen)
