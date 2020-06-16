# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class prepareReport2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_prepare_report2(self):
        driver = self.driver
        driver.get("http://192.168.0.3:8081/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"刘佳")
        driver.find_element_by_id("input-password").click()
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")
        #
        # ##########
        # #选择数据库
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="logindiag"]/div[3]/div/div/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span').click()

        # #########
        driver.find_element_by_id("input-password").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[3]/div").click()
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[3]/ul/li[3]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[3]/section/div/div/div/div/div/div/div/div[3]/div[2]/div/div[3]/table/tbody/tr/td/div/label/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[3]/section/div/div/div/div/div/div/div/div[3]/div/button[2]/span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
        time.sleep(1)
        driver.refresh()
        driver.find_element_by_id("tab-2").click()
        time.sleep(3)
        print("工程初设上传成功！！！")

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
