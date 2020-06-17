# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class EmergencyManageEdit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_emergency_manage_edit(self):
        '''应急预案编辑成功'''
        driver = self.driver
        driver.get("http://192.168.0.3:8081/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"杨斌")
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[2]/span").click()

        driver.find_element_by_id("a-login").click()
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[12]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[12]/ul/li").click()
        time.sleep(1)
        name = driver.find_element_by_xpath('//table/tbody/tr[1]/td[3]/div').text
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[3]/section/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td/div/label/span/span").click()

        #点击编辑
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        #编辑预案名称
        driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(name+'编辑')
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[4]/div/div/ul/li[4]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[9]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[5]/div/div/ul/li[4]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[10]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[6]/div/div/ul/li[2]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[11]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[7]/div/div/ul/li[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[12]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[8]/div/div/ul/li[4]/span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[15]").click()
        time.sleep(2)
        print("应急预案编辑成功！！！")

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
