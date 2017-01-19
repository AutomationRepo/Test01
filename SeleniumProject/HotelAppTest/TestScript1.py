'''
Created on Jan 17, 2017

@author: shweta
'''
import unittest
from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.support import expected_conditions 

class Test(unittest.TestCase):

    def setUp(self):
        #webdriver.DesiredCapabilities.CHROME["unexpectedAlertBehaviour"]="ignore"
        self.driver = webdriver.Chrome()
        self.driver.get("http://adactin.com/HotelApp/")
        self.driver.maximize_window()
        assert "Hotel" in self.driver.title

    def tearDown(self):
        self.driver.quit()

    def test_Login(self):
        edtUserName = self.driver.find_element_by_id("username")
        edtUserName.send_keys("foouser02")
        edtPassword = self.driver.find_element_by_id("password")
        edtPassword.send_keys("test")
        btnLogin = self.driver.find_element_by_id("login")
        btnLogin.click()  
        txtLogin = self.driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]")
        assert "Welcome to AdactIn Group of Hotels" in txtLogin.text    

    def test_verifyCheckOutDate(self):
        self.test_Login()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()