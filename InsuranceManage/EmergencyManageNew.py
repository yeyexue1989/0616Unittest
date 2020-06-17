# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,datetime


cur = datetime.datetime.now()
a = "%s%s"%(cur.day,cur.minute)

class EmergencyManageNew(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_emergency_manage_new(self):
        driver = self.driver
        driver.get("http://192.168.0.3:8081/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"杨斌")
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")
        # time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[2]/span").click()
        driver.find_element_by_id("a-login").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[12]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[12]/ul/li").click()
        time.sleep(2)
        driver.find_element_by_xpath("//section/div[2]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/button[1]/span").click()
        # time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(u"测试新增预案%s"%a)
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[4]/div/div/ul/li[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[9]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[5]/div/div/ul/li[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[10]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[6]/div/div/ul/li[3]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[11]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[7]/div/div/ul/li[3]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[12]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[8]/div/div/ul/li[3]/span").click()
        # time.sleep(1)
        driver.find_element_by_xpath("//span/button[2]/span").click()
        time.sleep(2)
        print("应急预案创建成功！！！")

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
