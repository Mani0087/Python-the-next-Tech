import unittest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium import webdriver

class Eyelove(unittest.TestCase): 
      
    def setUp(self): 
        pass

    def test_create_an_appointment(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://eyelove.bot.qa.dialogflows.com/s/eyelove")
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[2]/button/span').click()
        self.driver.find_element_by_id("input-message").send_keys("hi")
        self.driver.find_element_by_xpath('//*[@id="btn-send"]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@name='fullname']").send_keys('Manikanta')
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys('vegimani87@gmail.com')
        #self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div[3]/div/div').send_keys     
        self.driver.find_element_by_xpath("//input[@name='phone']").send_keys('+919945997123')
        self.driver.find_element_by_xpath("//input[@name='zipCode']").send_keys('M4B 1B3')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div[6]/div/button/span').click()
        self.driver.find_element('//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/button[1]').click()
        self.driver.find_element("//*[text()='Continue with my previous details']").click()



    def tearDown(self):
        pass
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

