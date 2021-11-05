from unittest.case import TestCase
from appium import webdriver
import unittest
import time
import TextTestCase
import StickyNoteTestCase
import LoginAndActive

email = "aiden.test2222@gmail.com"
password = "$Cd069798"

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # super().setUp()
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = '172.21.10.103:5555'
        desired_caps['appPackage'] = 'com.viewsonic.droid'
        desired_caps["noReset"]=True
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    def test_Text(self):
        TextTestCase.testCase1(self)
        TextTestCase.testCase2(self)
        TextTestCase.testCase3(self)

    def test_StickyNote(self):
        LoginAndActive.NormalLogin(self, email, password)
        time.sleep(20)
        StickyNoteTestCase.TestStickyNote_Pen(self)
        StickyNoteTestCase.TestStickyNote_Text(self)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    suite1 = unittest.TestSuite()
    suite1.addTest(MyTestCase("test_StickyNote"))
    suite1.addTest(MyTestCase("test_Text"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite1)