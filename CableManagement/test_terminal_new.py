# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Terminalnew(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_terminalnew(self):
        driver = self.driver
        driver.get("http://192.168.0.3:8081/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"杨斌")
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[2]/div/div/ul/li[2]").click()
        driver.find_element_by_id("a-login").click()
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[2]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[2]/ul/li[2]").click()

        # driver.find_element_by_xpath("//div[@id='app']/div/div/div[3]/section/div[2]/div/div/div[2]/div/div/div/div[4]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[3]/section/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[3]/table/tbody/tr/td[13]/div/div/i").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='line-container']/div[3]/div/div/ul/li[2]/p").click()
        driver.find_element_by_xpath("//div[@id='line-container']/div[4]/div[2]/div/div/div/div[3]/table/tbody/tr/td[10]/div/label/i").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='cable-total']/div[2]/div/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='cable-total']/div[4]/div/div/div[3]/table/tbody/tr/td[12]/div/div/i").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='cable-detail']/div[2]/div/div/ul/li[4]/p").click()
        driver.find_element_by_xpath("//div[@id='cable-detail']/div[2]/div/div/div/div/button/span").click()
        driver.find_element_by_xpath("(//input[@type='text'])[60]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[60]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[60]").send_keys("terminalassetcode")
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[61]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[61]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[61]").send_keys(u"终端1")
        driver.find_element_by_xpath("(//input[@type='text'])[82]").click()
        driver.find_element_by_xpath("//div[4]/div/div/ul/li[3]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[15]").click()
        time.sleep(2)
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
