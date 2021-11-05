import time
import Canvas
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def SelectTextBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/btnTypingText"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/btnTypingText").click()

def TypeText(self, string:str): #string can accept lower case a~z only
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/editText"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/editText").click()
    for char in string:
        if char>='a' and char<='z':
            keycode = str(29 + (ord(char)-ord('a')))
            self.driver.press_keycode(keycode)

def ChangeFont(self, index:int):    #index of font is 1~9
    font_selector_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[9]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Spinner[1]/android.view.ViewGroup"
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, font_selector_xpath))
    )
    self.driver.find_element_by_xpath(font_selector_xpath).click()
    time.sleep(1)
    font_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[" + str(index) + "]"
    self.driver.find_element_by_xpath(font_xpath).click()

def ChangeSize(self, index:int):    #index of size is 1~
    size_selector_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[9]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Spinner[2]/android.view.ViewGroup"
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, size_selector_xpath))
    )
    self.driver.find_element_by_xpath(size_selector_xpath).click()
    time.sleep(1)
    size_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[" + str(index) + "]"
    self.driver.find_element_by_xpath(size_xpath).click()

def Bold(self): #粗體
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkBold"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkBold").click()

def Italic(self):   #斜體
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkItalic"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkItalic").click()

def UnderLine(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkUnderline"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkUnderline").click()

def edittextclear(self,text):
    self.driver.press_keycode('123')
    for i in range(0,len(text)):
        self.driver.press_keycode('67')

def ChangeColor(self,type:str="Standard",ColorNum:int=1,R=255,G=255,B=255,A=255): #type is "Standard" or "Advanced", Color num(1~17) for Standard and RGBA(0~255) for Advanced
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonColor"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonColor").click()
    if type == "Standard":
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonStandard"))
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/buttonStandard").click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.GridView/android.view.View['+str(ColorNum)+']').click()
    elif type == "Advanced":
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonAdvanced"))
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/buttonAdvanced").click()
        for i in range(4):
            pattern_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup" + "[" + str(i+1) + "]" + "/android.view.ViewGroup/android.widget.EditText"
            pattern = self.driver.find_element_by_xpath(pattern_xpath)
            if str(i+1) == "1":
                pattern.click()
                context1 = pattern.get_attribute('text')
                edittextclear(self,context1)
                pattern.send_keys(R)
                self.driver.press_keycode('66')

            elif str(i+1) == "2":
                pattern.click()
                context2 = pattern.get_attribute('text')
                edittextclear(self,context2)
                pattern.send_keys(G)
                self.driver.press_keycode('66')
            elif str(i+1) == "3":
                pattern.click()
                context3 = pattern.get_attribute('text')
                edittextclear(self,context3)
                pattern.send_keys(B)
                self.driver.press_keycode('66')
            else:
                pattern.click()
                context4 = pattern.get_attribute('text')
                edittextclear(self,context4)
                pattern.send_keys(A)
                self.driver.press_keycode('66')
        Canvas.Tap(self, 1900, 500)

def ChangeColorBg(self,type:str="Standard",ColorNum:int=1,R=255,G=255,B=255,A=255): #type is "Standard" or "Advanced", Color num(1~17) for Standard and RGBA(0~255) for Advanced
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonColorBg"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonColorBg").click()
    if type == "Standard":
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonStandard"))
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/buttonStandard").click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.GridView/android.view.View['+str(ColorNum)+']').click()
    elif type == "Advanced":
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonAdvanced"))
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/buttonAdvanced").click()
        for i in range(4):
            pattern_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup" + "[" + str(i+1) + "]" + "/android.view.ViewGroup/android.widget.EditText"
            pattern = self.driver.find_element_by_xpath(pattern_xpath)
            if str(i+1) == "1":
                pattern.click()
                context1 = pattern.get_attribute('text')
                edittextclear(self,context1)
                pattern.send_keys(R)
                self.driver.press_keycode('66')

            elif str(i+1) == "2":
                pattern.click()
                context2 = pattern.get_attribute('text')
                edittextclear(self,context2)
                pattern.send_keys(G)
                self.driver.press_keycode('66')
            elif str(i+1) == "3":
                pattern.click()
                context3 = pattern.get_attribute('text')
                edittextclear(self,context3)
                pattern.send_keys(B)
                self.driver.press_keycode('66')
            else:
                pattern.click()
                context4 = pattern.get_attribute('text')
                edittextclear(self,context4)
                pattern.send_keys(A)
                self.driver.press_keycode('66')
        Canvas.Tap(self, 1900, 500)

def Superscript(self):  #上標
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkUpscript"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkUpscript").click()

def Subscript(self):    #下標
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkDownscript"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkDownscript").click()

def AlignLeft(self):    #靠左對齊
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkAlignLeft"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkAlignLeft").click()

def AlignRight(self):   #靠右對齊
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkAlignRight"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkAlignRight").click()

def Center(self):   #置中
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkAlignCenter"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkAlignCenter").click()

def List(self):     #條列項目
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkBulleted"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkBulleted").click()

def AddIdent(self): #縮排
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonIncIndent"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonIncIndent").click()

def ReduceIdent(self):  #減少縮排
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonDecIndent"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonDecIndent").click()

def CloseEditor(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonMenuClose"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonMenuClose").click()