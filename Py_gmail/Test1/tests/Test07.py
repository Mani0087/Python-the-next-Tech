from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
import unittest
from selenium import webdriver

class Login (unittest.TestCase):

    def setUp(self):
    
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://mail.google.com/")
        self.driver.find_element_by_css_selector("input[type='email']").send_keys('tset0087@gmail.com')
        self.driver.find_element_by_css_selector("#identifierNext").click()
        #ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        #your_element = WebDriverWait(self.driver, 20,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        time.sleep(10)
        self.driver.find_element_by_css_selector("input[type='password']").send_keys('Test123!@#')
        self.driver.find_element_by_css_selector("#passwordNext").click()
    
    # def test_search_using_subject(self):
        
    #     self.driver.find_element_by_css_selector("input[name='q']").send_keys('test002'+Keys.ENTER)
    #     #input()

    def test_sending_mail(self):


        self.driver.find_element_by_xpath(("//div[contains(text(), 'Compose')]")).click()
        
        self.driver.find_element_by_xpath("//textarea").click()
        time.sleep(10)
        self.driver.switch_to_active_element().send_keys("tset0087@gmail.com")
        self.driver.find_element_by_css_selector("input[name='subjectbox']").send_keys("Test03")
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@role='textbox']").send_keys("Hello")
        time.sleep(10)
        #self.driver.find_element_by_xpath(("//div[contains(text(), 'Send')]")).click()
        self.driver.find_element_by_xpath("//div[text()='Send']").click()
        time.sleep(5)
        #self.driver.find_element_by_xpath("//span[text()='Message sent']")
        #input()
        
    def test_recivie_mail(self):
        
        
        self.driver.find_element_by_xpath("//span[@class='bqe']").click()
        #input.get_attribute self.driver.find_element_by_xpath("//div[@role='textbox']").click()
        #input.get_attribute('Hello')
        textbox_input = driver.find_element_by_xpath("//div[@role='textbox']").click()
        print(textbox_input.get_attribute('value'))
        
     

    def tearDown(self):
        self.driver.quit()
        pass

if __name__ == "__main__":
    unittest.main()
		





