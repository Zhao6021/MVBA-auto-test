from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def NewPage(self):
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnPageAdd').click() 

def NextPage(self):
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnPageNext').click()

def LastPage(self):
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnPagePrev').click()