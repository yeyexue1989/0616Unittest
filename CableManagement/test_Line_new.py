# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,datetime

cur = datetime.datetime.now()
a = ("%s%s%s%s"%(cur.month,cur.day,cur.minute,cur.second))

class LineNewAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_line_new_add(self):
        driver = self.driver
        driver.get("http://192.168.0.3:8081/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"杨斌")
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")

        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[2]/div/div/ul/li[2]").click()


        driver.find_element_by_id("a-login").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[2]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[2]/ul/li[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/span[2]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/span[2]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys(u"测试新增线路资产单位%s"%a)
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[15]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[15]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[15]").send_keys("assetcode")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[16]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[16]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[16]").send_keys("projectCode")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[17]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[17]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[17]").send_keys(u"a测试新增线路工程名称%s"%a)
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[20]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[20]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[20]").send_keys("EntityAssetID")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[21]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[21]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[21]").send_keys(u"a测试新增线路%s"%a)
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[22]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[22]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[22]").send_keys("RunningCode")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[27]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[4]/div/div/ul/li[14]/span").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[29]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[29]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[29]").send_keys("PMcode")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[44]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[44]").clear()
        # time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[44]").send_keys(u"测试新增线路起点位置")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[46]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[46]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[46]").send_keys(u"测试起点电站")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[47]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[47]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[47]").send_keys("startSwitchCode")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[48]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[48]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[48]").send_keys(u"测试新增线路终点位置")
        driver.find_element_by_xpath("(//input[@type='text'])[50]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[50]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[50]").send_keys(u"测试终点电站")
        driver.find_element_by_xpath("(//input[@type='text'])[51]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[51]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[51]").send_keys("EndSwitchCode")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[52]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[52]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[52]").send_keys("1000")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[53]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[53]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[53]").send_keys("20000")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[54]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[54]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[54]").send_keys("18000")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[55]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[55]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[55]").send_keys(u"测试新增线路设计单位")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[56]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[56]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[56]").send_keys(u"测试新增线路建设单位")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[57]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[57]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[57]").send_keys(u"测试新增施工单位")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[58]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[58]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[58]").send_keys(u"测试新增线路监理单位")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[59]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[59]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[59]").send_keys(u"测试新增线路功能位置")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[60]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[60]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[60]").send_keys(u"测试新增线路设备主人")
        time.sleep(0.5)
        #是否已测绘
        driver.find_element_by_xpath("(//input[@type='text'])[62]").click()
        driver.find_element_by_xpath("//div[5]/div[1]/div[1]/ul/li[1]/span").click()
        #重要程度
        driver.find_element_by_xpath("(//input[@type='text'])[63]").click()
        driver.find_element_by_xpath("//div[6]/div[1]/div[1]/ul/li[1]/span").click()
        time.sleep(1)

        driver.find_element_by_xpath("(//input[@type='text'])[68]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[68]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[68]").send_keys("facilityCode")
        time.sleep(0.1)
        driver.find_element_by_xpath("(//input[@name=''])[4]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//tr[6]/td[6]/div/span").click()
        time.sleep(0.5)
        # driver.find_element_by_xpath("//div[4]/div[2]/div[2]/div[2]/div").click()
        driver.find_element_by_xpath("(//input[@type='text'])[71]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[71]").send_keys("3")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[72]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[72]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[72]").send_keys(u"测试新增线路备注")
        driver.find_element_by_xpath("//span/button[2]/span").click()
        time.sleep(3)
        print("线路新增成功!!!")


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
