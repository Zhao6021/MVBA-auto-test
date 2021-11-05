import Canvas
import Text
import time
import Screenshot
import Compare

def testCase1(self):
    time.sleep(5)
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    Canvas.Tap(self, 900,250)
    Canvas.Tap(self, 900,250)
    Text.ChangeFont(self, 3)
    Text.ChangeSize(self,9)
    Text.Bold(self)
    Text.Italic(self)
    Text.UnderLine(self)
    Text.TypeText(self,"testcaseone")
    Screenshot.screenshotTextEditor(self, "./Screenshots/Text/Case1_Editor.png")
    Text.CloseEditor(self)
    Screenshot.screenshotCanvas(self, "./Screenshots/Text/Case1_Cavas.png")
    if not Compare.isImgEqual("./Screenshots/Text/Case1_Editor.png", "./Samples/Text/Case1_Editor.png"):
        print("Case 1: Text Editor Fail!")
    if not Compare.isImgEqual("./Screenshots/Text/Case1_Cavas.png", "./Samples/Text/Case1_Cavas.png"):
        print("Case 1: Text Canvas Fail!")

def testCase2(self):
    time.sleep(5)
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    Canvas.Tap(self, 900,500)
    Canvas.Tap(self, 900,500)
    Text.ChangeFont(self, 6)
    Text.ChangeSize(self,19)
    Text.ChangeColor(self,"Advanced",R=130,G=107,B=70)
    Text.ChangeColorBg(self,ColorNum=9)
    Text.TypeText(self,"testcasetwo")
    Screenshot.screenshotTextEditor(self, "./Screenshots/Text/Case2_Editor.png")
    Text.CloseEditor(self)
    Screenshot.screenshotCanvas(self, "./Screenshots/Text/Case2_Cavas.png")
    Screenshot.screenshotCanvas(self, "./Screenshots/Text/Case2_Cavas.png")
    if not Compare.isImgEqual("./Screenshots/Text/Case2_Editor.png", "./Samples/Text/Case2_Editor.png"):
        print("Case 2: Text Editor Fail!")
    if not Compare.isImgEqual("./Screenshots/Text/Case2_Cavas.png", "./Samples/Text/Case2_Cavas.png"):
        print("Case 2: Text Canvas Fail!")

def testCase3(self):
    time.sleep(5)
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    Canvas.Tap(self, 900,750)
    Canvas.Tap(self, 900,750)
    Text.ChangeFont(self, 9)
    Text.ChangeSize(self,23)
    Text.ChangeColor(self,ColorNum=6)
    Text.ChangeColorBg(self,"Advanced",R=110,G=200,B=90)
    Text.TypeText(self,"testcasethree")
    Screenshot.screenshotTextEditor(self, "./Screenshots/Text/Case3_Editor.png")
    Text.CloseEditor(self)
    Screenshot.screenshotCanvas(self, "./Screenshots/Text/Case3_Cavas.png")
    if not Compare.isImgEqual("./Screenshots/Text/Case3_Editor.png", "./Samples/Text/Case3_Editor.png"):
        print("Case 3: Text Editor Fail!")
    if not Compare.isImgEqual("./Screenshots/Text/Case3_Cavas.png", "./Samples/Text/Case3_Cavas.png"):
        print("Case 3: Text Canvas Fail!")
