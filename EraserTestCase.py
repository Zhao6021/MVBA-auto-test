import Eraser
import Canvas
import FileManagement
import PageManagement
import time

#For Case 1-1
T_list = [[60,218],[326,202]]
E_list = [[431,171],[661,159]]
S_list = [[1026,187],[894,159],[882,268],[1049,408],[1034,482],[847,466]]
T2_list = [[1166,179],[1582,148]]
LOCK_list = [[377,692],[1718,707]]

#For Case 1-2
Movepage2_list1 = [[309,321],[1795,305]]
Movepage2_list2 = [[263,789],[1878,797]]
Movepage3_list1 = [[229,237],[1710,249]]
Movepage3_list2 = [[229,237],[1710,249]]
Movepage4_list1 = [[467,330],[1707,342]]
Movepage4_list2 = [[296,760],[1741,781]]
Movepage5_list1 = [[330,363],[1690,380]]
Movepage5_list2 = [[330,810],[1557,818]]
Movepage6_list1 = [[346,355],[1736,367]]
Movepage6_list2 = [[309,781],[1757,781]]
Movepage7_list1 = [[127,300],[1171,280]]
Movepage7_list2 = [[584,657],[1705,657]]
Movepage8_list1 = [[303,319],[1793,288]]
Movepage8_list2 = [[664,691],[1517,680]]
Movepage9_list1 = [[96,472],[1697,453]]

#For case 2-2, 1~8 means page 1 ~ page 8
circle_eraser_2to2 = {
    1 : [[357,538], [349,845], [710,852], [707,538], [369,534]],
    2 : [[420,173], [409,505], [817,505], [810,166], [416,147]],
    3 : [[1006,559], [1022,894], [1376,871], [1369,532], [1080,544]],
    4 : [[1022,339], [628,66], [447,517], [921,467]],
    5 : [[204,131], [247,605], [883,594], [891,135], [266,123]],
    6 : [[251,517], [254,894], [1033,867], [1018,486], [339,490]],
    7 : [[166,166], [170,455], [632,443], [605,112], [154,104]],
    8 : [[204,131], [247,605], [883,594], [891,135], [266,123]],
}

#For case 2-3
circle_eraser_2to3 = [[30,87], [30,932], [1876,910], [1898,127], [100,105]]

def OpenOLF(self):
    FileManagement.OpenFileManagement(self)
    FileManagement.ChooseOpenFile(self)
    FileManagement.SelectFile(self,2)
    FileManagement.SelectFile(self,1)
    FileManagement.SelectFile(self,3)
    FileManagement.SelectFile(self,1)
    time.sleep(8)

def Case1to1(self):
    OpenOLF(self)
    Eraser.OpenEraserMenu(self)
    Eraser.ChooseRegularEraser(self)
    Eraser.AdjustEraserSize(self,40)
    Eraser.CloseEraserMenu(self)
    Eraser.Swipe(self, T_list, 1500)
    Eraser.Swipe(self, E_list, 1500)
    Eraser.Swipe(self, S_list, 1500)
    Eraser.Swipe(self, T2_list, 1500)
    Eraser.Swipe(self, LOCK_list, 1500)

def Case1to2(self):
    OpenOLF(self)
    PageManagement.NextPage(self)
    Eraser.OpenEraserMenu(self)
    Eraser.ChooseRegularEraser(self)
    Eraser.AdjustEraserSize(self,40)
    Eraser.CloseEraserMenu(self)
    Eraser.Swipe(self,Movepage2_list1,1500)
    Eraser.Swipe(self,Movepage2_list2,1500)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Eraser.Swipe(self,Movepage3_list1,1500)
    Eraser.Swipe(self,Movepage3_list2,1500)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Eraser.Swipe(self,Movepage4_list1,1500)
    Eraser.Swipe(self,Movepage4_list2,1500)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Eraser.Swipe(self,Movepage5_list1,1500)
    Eraser.Swipe(self,Movepage5_list2,1500)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Eraser.Swipe(self,Movepage6_list1,1500)
    Eraser.Swipe(self,Movepage6_list2,1500)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Eraser.Swipe(self,Movepage7_list1,1500)
    Eraser.Swipe(self,Movepage7_list2,1500)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Eraser.Swipe(self,Movepage8_list1,1500)
    Eraser.Swipe(self,Movepage8_list2,1500)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Eraser.Swipe(self,Movepage9_list1,1500)

    
def Case1to3(self):
    OpenOLF(self)
    PageManagement.NextPage(self)
    Eraser.OpenEraserMenu(self)
    Eraser.ChooseRegularEraser(self)
    Eraser.AdjustEraserSize(self,40)
    Eraser.CloseEraserMenu(self)
    time.sleep(1)
    Canvas.Tap(self,603,296)
    time.sleep(1)
    Canvas.Tap(self,1137,300)
    time.sleep(1)
    Canvas.Tap(self,438,726)
    time.sleep(1)
    Canvas.Tap(self,1486,714)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Canvas.Tap(self,561,288)
    time.sleep(1)
    Canvas.Tap(self,1194,323)
    time.sleep(1)
    Canvas.Tap(self,549,707)
    time.sleep(1)
    Canvas.Tap(self,1198,722)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Canvas.Tap(self,703,319)
    time.sleep(1)
    Canvas.Tap(self,1313,326)
    time.sleep(1)
    Canvas.Tap(self,403,722)
    time.sleep(1)
    Canvas.Tap(self,1417,695)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Canvas.Tap(self,601,355)
    time.sleep(1)
    Canvas.Tap(self,1411,380)
    time.sleep(1)
    Canvas.Tap(self,547,789)
    time.sleep(1)
    Canvas.Tap(self,1302,797)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Canvas.Tap(self,584,307)
    time.sleep(1)
    Canvas.Tap(self,1321,300)
    time.sleep(1)
    Canvas.Tap(self,611,699)
    time.sleep(1)
    Canvas.Tap(self,1386,730)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Canvas.Tap(self,357,288)
    time.sleep(1)
    Canvas.Tap(self,887,284)
    time.sleep(1)
    Canvas.Tap(self,925,657)
    time.sleep(1)
    Canvas.Tap(self,1475,664)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Canvas.Tap(self,564,311)
    time.sleep(1)
    Canvas.Tap(self,1597,300)
    time.sleep(1)
    Canvas.Tap(self,1110,687)
    time.sleep(2)
    PageManagement.NextPage(self)
    time.sleep(1)
    Canvas.Tap(self,303,472)
    time.sleep(1)
    Canvas.Tap(self,707,465)
    time.sleep(1)
    Canvas.Tap(self,1083,476)
    time.sleep(1)
    Canvas.Tap(self,1482,472)
    time.sleep(2)

def Case2to2(self):
    OpenOLF(self)
    Eraser.OpenEraserMenu(self)
    Eraser.ChooseCircleEraser(self)
    for page in circle_eraser_2to2:
        Canvas.Swipe(self, circle_eraser_2to2[page])
        PageManagement.NextPage(self)
        time.sleep(1)

def Case2to3(self):
    OpenOLF(self)
    Eraser.OpenEraserMenu(self)
    Eraser.ChooseCircleEraser(self)
    for i in range(8):
        Canvas.Swipe(self, circle_eraser_2to3)
        PageManagement.NextPage(self)
        time.sleep(1)
    Canvas.Swipe(self, circle_eraser_2to3)

def Case3(self):
    OpenOLF(self)
    for i in range(8):
        Eraser.OpenEraserMenu(self)
        Eraser.ClearCanvas(self)
        PageManagement.NextPage(self)
    Eraser.OpenEraserMenu(self)
    Eraser.ClearCanvas(self)