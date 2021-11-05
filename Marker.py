from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ChangeColor(self,ColorNum):  ## " Open Advanced Adjustment" (8+16=24 "+"icon) => ColorNum = 8  ##
    Num = ColorNum + 16     ## Red = 17,Orange = 18, Yellow = 19 ......) ##
    self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[9]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']').click()

def AdvancedColor(self,ColorNum): ## 1~17 ##
    self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.GridView/android.view.View['+str(ColorNum)+']').click()

def click_Adorner_colorMenu(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonColor"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonColor").click()

def edittextclear(self,text):
    self.driver.press_keycode('123')
    for i in range(0,len(text)):
        self.driver.press_keycode('67')

def change_color(self,R,G,B,A):
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

def AdjustThickness(self,Num):     ## 0~32 ##
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/seekBarWidth"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/seekBarWidth").send_keys(str(Num))

def AdjustTransParency(self,Num):    ## 0~229 ##
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/seekBarAlpha"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/seekBarAlpha").send_keys(str(Num))