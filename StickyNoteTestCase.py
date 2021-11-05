import Canvas
import StickyNote
import MagicBox
import time
import Screenshot
import Compare

def TestStickyNote_Pen(self):
    MagicBox.OpenMagicBox(self)
    StickyNote.ClickStickynote(self)
    StickyNote.StickynoteColor(self, 1)
    StickyNote.SelectPen(self)
    StickyNote.PenColor(self, "Red")
    StickyNote.PenThickness(self, 8)
    my_draw = [[1000,350],[850,350],[850,650],[1000,650],[1000,500],[850,500]]
    Canvas.Draw(self, my_draw)
    Screenshot.screenshotStickyNoteCanvas(self, "./ScreenShots/StickyNote/Canvas_Pen.png")
    Screenshot.screenshotStickyNoteBar(self, "./ScreenShots/StickyNote/Bar_Pen.png")
    time.sleep(3)
    StickyNote.CloseStickynote(self)
    if not Compare.isImgEqual("./ScreenShots/StickyNote/Canvas_Pen.png", "./Samples/StickyNote/Canvas_Pen.png"):
        print("Pen Case: Canvas Fail!")
    if not Compare.isImgEqual("./ScreenShots/StickyNote/Bar_Pen.png", "./Samples/StickyNote/Bar_Pen.png"):
        print("Pen Case: Bar Fail!")

def TestStickyNote_Text(self):
    MagicBox.OpenMagicBox(self)
    StickyNote.ClickStickynote(self)
    StickyNote.StickynoteColor(self,3)
    StickyNote.SelectText(self)
    StickyNote.ChangeFont(self,6)
    StickyNote.ChangeSize(self,20)
    StickyNote.TextBold(self)
    StickyNote.TextItalic(self)
    StickyNote.TextUnderLine(self)
    StickyNote.TypeText(self,"teststickynote")
    Screenshot.screenshotStickyNoteBar(self, "./ScreenShots/StickyNote/Bar_Text.png")
    StickyNote.SelectPen(self)
    Screenshot.screenshotStickyNoteCanvas(self, "./ScreenShots/StickyNote/Canvas_Text.png")
    time.sleep(3)
    StickyNote.CloseStickynote(self)
    if not Compare.isImgEqual("./ScreenShots/StickyNote/Canvas_Text.png", "./Samples/StickyNote/Canvas_Text.png"):
        print("Text Case: Canvas Fail!")
    if not Compare.isImgEqual("./ScreenShots/StickyNote/Bar_Text.png", "./Samples/StickyNote/Bar_Text.png"):
        print("Text Case: Bar Fail!")