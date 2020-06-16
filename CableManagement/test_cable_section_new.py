# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from ddt import ddt,data
# @classmethod
# @ddt
class CableSection(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True
    # @data("电缆段1","电缆段2","电缆段3","电缆段4","电缆段5","电缆段6","电缆段7")
    def test_cable_section(self):
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
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[2]/div").click()
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[2]/ul/li[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/section/div[2]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[13]/div/div/i').click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='line-container']/div[3]/div/div/ul/li[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='line-container']/div[4]/div[2]/div/div/div/div[3]/table/tbody/tr/td[10]/div/label/i").click()
        driver.find_element_by_xpath("//div[@id='cable-total']/div[2]/div/div/ul/li[2]/p").click()
        driver.find_element_by_xpath("//div[@id='cable-total']/div[2]/div/div/div/div/button/span").click()
        time.sleep(4)
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys("assetUnit")
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("CableSectionAssetCode")
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("DLD1")
        driver.find_element_by_xpath("(//input[@type='text'])[13]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[13]").clear()
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[13]").send_keys(u"起点位置")
        driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").clear()
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys(u"终点位置")
        driver.find_element_by_xpath("(//input[@type='text'])[15]").click()
        driver.find_element_by_xpath("//div[4]/div/div/ul/li").click()
        driver.find_element_by_xpath("(//input[@type='text'])[16]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[16]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[16]").send_keys("1000")
        driver.find_element_by_xpath("//input[@name='']").click()
        driver.find_element_by_xpath("(//button[@type='button'])[18]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[18]").click()
        driver.find_element_by_xpath("//td[6]/div/span").click()
        driver.find_element_by_xpath("(//input[@type='text'])[19]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[19]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[19]").send_keys(u"施工单位")
        driver.find_element_by_xpath("(//input[@type='text'])[21]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[21]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[21]").send_keys("TYPEA")
        driver.find_element_by_xpath("(//input[@type='text'])[22]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[22]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[22]").send_keys(u"生产厂家")
        driver.find_element_by_xpath("(//input[@type='text'])[24]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[24]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[24]").send_keys("220")
        driver.find_element_by_xpath("(//input[@type='text'])[27]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[27]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[27]").send_keys("1000")
        driver.find_element_by_xpath("(//input[@type='text'])[28]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[28]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[28]").send_keys("1200")
        driver.find_element_by_xpath("(//input[@type='text'])[48]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[48]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[48]").send_keys("facilityCode")
        driver.find_element_by_xpath("(//input[@name=''])[5]").send_keys("2020-06-10")
        time.sleep(2)
        # driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[5]/div/span").click()
        # /html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[5]/div/span
        #重要程度
        driver.find_element_by_xpath("//div[2]/div/div[2]/div/div[1]/div/form/table/tbody/tr[16]/td[2]/div/div/div/div[1]/input").click()
        driver.find_element_by_xpath("//div[7]/div[1]/div[1]/ul/li[1]").click()

        driver.find_element_by_xpath("(//input[@type='text'])[51]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[51]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[51]").send_keys("220kV")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[52]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[52]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[52]").send_keys("3")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[53]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[53]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[53]").send_keys(u"线路详情")
        driver.find_element_by_xpath("(//input[@type='text'])[54]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[54]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[54]").send_keys(u"唯一标识")
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[56]").click()
        driver.find_element_by_xpath("//div[8]/div[1]/div[1]/ul/li[1]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[57]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[9]/div[1]/div[1]/ul/li[1]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[58]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[58]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[58]").send_keys("10000")
        time.sleep(0.5)
        driver.find_element_by_xpath("(//input[@type='text'])[59]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[59]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[59]").send_keys(u"备注")
        driver.find_element_by_xpath("//div[2]/div/div[3]/div/div/button/span").click()
        print("电缆段创建成功！！！")
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
