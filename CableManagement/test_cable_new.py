# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,datetime
from ddt import ddt
from ddt import data


cur = datetime.datetime.now()
a = ("%s%s%s"%(cur.day,cur.minute,cur.second))

@ddt
class CableNewAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True
    # @data("电缆1","电缆2","电缆3")
    # cable = "电缆"
    # def test_cable_new_add(self,cablename):
    def test_cable_new_add(self):

        driver = self.driver
        driver.get("http://192.168.0.3:8081/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"杨斌")
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")

        time.sleep(2)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[2]/div/div/ul/li[2]").click()

        driver.find_element_by_id("a-login").click()
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[2]/div").click()
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[2]/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[3]/section/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[3]/table/tbody/tr/td[13]/div/div/i").click()
        driver.find_element_by_xpath("//div[@id='line-container']/div[3]/div/div/ul/li[2]/p").click()

        #点击添加
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='line-container']/div[3]/div/div/div/div/button/span").click()
        #资产编号
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[65]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[65]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[65]").send_keys("assetCode")
        #电缆名称
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[66]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[66]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[66]").send_keys(cablename)
        driver.find_element_by_xpath("(//input[@type='text'])[66]").send_keys("DL1")
        #起点位置
        driver.find_element_by_xpath("(//input[@type='text'])[74]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[74]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[74]").send_keys(cablename+"起点位置")
        driver.find_element_by_xpath("(//input[@type='text'])[74]").send_keys("起点位置")
        #结束位置
        driver.find_element_by_xpath("(//input[@type='text'])[75]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[75]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[75]").send_keys(cablename+"结束位置")
        driver.find_element_by_xpath("(//input[@type='text'])[75]").send_keys("结束位置")
        #设备主人
        driver.find_element_by_xpath("(//input[@type='text'])[78]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[78]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[78]").send_keys(cablename+"设备主人")
        driver.find_element_by_xpath("(//input[@type='text'])[78]").send_keys("设备主人")
        #电缆类型
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[80]").click()
        driver.find_element_by_xpath("//div[4]/div/div/ul/li[2]").click()
        #起止说明
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[82]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[82]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[82]").send_keys(cablename+"起止说明")
        driver.find_element_by_xpath("(//input[@type='text'])[82]").send_keys("起止说明")
        driver.find_element_by_xpath("(//input[@name=''])[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//tr[2]/td[4]/div/span").click()
        driver.find_element_by_xpath("(//input[@type='text'])[84]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[84]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[84]").send_keys("facilityCode")
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[85]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[85]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[85]").send_keys(cablename+"备注")
        driver.find_element_by_xpath("(//input[@type='text'])[85]").send_keys("备注")
        driver.find_element_by_xpath("(//input[@name=''])[4]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[6]/div/div/div[2]/table/tbody/tr[6]/td[6]/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[73]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[7]/div/div/ul/li").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span/button[2]/span").click()
        time.sleep(4)
        print("电缆新增成功！！！")

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
