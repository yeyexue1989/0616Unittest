# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class prepareExamineZhuanzhe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_prepare_examine_zhuanzhe(self):
        driver = self.driver
        driver.get("http://192.168.0.3:8081/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"杨斌")
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")
        time.sleep(2)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[2]/div/div/ul/li[2]").click()
        time.sleep(1)
        driver.find_element_by_id("a-login").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[3]/div").click()
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[3]/ul/li[2]").click()
        time.sleep(5)
        # driver.refresh()
        driver.find_element_by_id("tab-4").click()
        time.sleep(1)
        driver.find_element_by_xpath("//table/tbody/tr/td/div/label/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//textarea").click()
        driver.find_element_by_xpath("//textarea").clear()
        driver.find_element_by_xpath("//textarea").send_keys(u"专责审核测试通过")
        time.sleep(1)
        driver.find_element_by_xpath("(//button[@type='button'])[9]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[3]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[3]/ul/li[3]").click()
        time.sleep(5)
        print("生产准备及验收专责审核成功！！！")


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
