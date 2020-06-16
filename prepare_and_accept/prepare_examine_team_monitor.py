# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class prepareExamine(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_prepare_examine(self):
        driver = self.driver
        driver.get("http://192.168.0.3:8081/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"陈阳")
        # driver.find_element_by_xpath("//div[@id='logindiag']/div[2]/label").click()
        driver.find_element_by_id("input-password").click()
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")

        #选择数据库
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="logindiag"]/div[3]/div/div/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span').click()

        driver.find_element_by_id("input-password").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[3]/div").click()
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[3]/ul/li[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//div[@id='tab-2'])").click()
        driver.find_element_by_xpath("//table/tbody/tr[1]/td[1]/div/label/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//textarea").click()
        driver.find_element_by_xpath("//textarea").clear()
        driver.find_element_by_xpath("//textarea").send_keys(u"测试审核意见")
        time.sleep(1)
        driver.find_element_by_xpath("//span/button[2]/span").click()
        driver.find_element_by_xpath("(//div[@id='tab-4'])").click()
        time.sleep(3)
        print("生产准备及验收班长审核成功！！！")


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
