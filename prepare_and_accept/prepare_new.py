# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,datetime


cur = datetime.datetime.now()
a = ("%s%s%s"%(cur.month,cur.day,cur.minute))

class prepareNewClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_prepare_new(self):
        driver = self.driver
        driver.get("http://192.168.0.3:8081/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"刘佳")
        # time.sleep(2)
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")
        #选择数据库
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="logindiag"]/div[3]/div/div/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span').click()
        time.sleep(1)
        driver.find_element_by_id("input-password").send_keys(Keys.ENTER)
        # time.sleep(3)

        #
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[3]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[3]/ul/li[2]").click()
        #点击新建工程按钮
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/section/div/div/div/div[1]/div/div/div[1]/div[3]/div[1]/button[1]/span').click()
        # time.sleep(2)
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(u"测试工程名称新增%s"%a)
        time.sleep(1)
        #选择电压等级
        # driver.find_element_by_xpath("//div[2]/div/form/div/div[2]").click()
        # driver.find_element_by_xpath("").click()
        # time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[9]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[4]/div/div/ul/li[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[10]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[5]/div/div/ul/li").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[11]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[6]/div/div/ul/li/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[12]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[12]").clear()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[12]").send_keys(u"测试设计单位新增")
        driver.find_element_by_xpath("(//input[@type='text'])[13]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[13]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[13]").send_keys(u"测试施工单位新增")
        driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys(u"测试监理单位新增")
        driver.find_element_by_xpath("//div/span[2]/i").click()
        driver.find_element_by_xpath("//div/span[2]/i").click()
        driver.find_element_by_xpath("//div/span[2]/i").click()
        driver.find_element_by_xpath("//div/span[2]/i").click()
        driver.find_element_by_xpath("//div/span[2]/i").click()
        driver.find_element_by_xpath("//div/span[2]/i").click()
        driver.find_element_by_xpath("//div/span[2]/i").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@name=''])[5]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[6]/div").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@name=''])[6]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("(//button[@type='button'])[28]").click()
        driver.find_element_by_xpath("//div[8]/div/div/div[2]/table/tbody/tr[2]/td[7]/div/span").click()
        driver.find_element_by_xpath("//textarea").click()
        driver.find_element_by_xpath("//textarea").clear()
        driver.find_element_by_xpath("//textarea").send_keys(u"测试工程概况新增")
        driver.find_element_by_xpath("(//input[@type='text'])[18]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[18]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[18]").send_keys(u"测试工程地点新增")
        driver.find_element_by_xpath("//span/button[2]/span").click()
        driver.refresh()
        time.sleep(3)
        print("项目可研新建工程成功!!!")

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
