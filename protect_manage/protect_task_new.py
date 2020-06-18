# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,datetime


cur = datetime.datetime.now()
a = ("%s%s"%(cur.day,cur.minute))

class ProtectTaskNew(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_protect_task_new(self):
        """保电任务新建"""
        driver = self.driver
        driver.get("http://192.168.0.3:8081/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"杨斌")
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")
        driver.find_element_by_id("logindiag").click()
        #选择数据库
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[2]/span").click()
        #点击登录
        driver.find_element_by_id("a-login").click()
        time.sleep(1)

        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/p/i").click()
        #保电管理
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[12]/div").click()
        #保电任务管理
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[12]/ul/li").click()
        #下发通知
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[3]/section/div[2]/div/div/div/div/div/div/div[2]/div/button/span").click()
        #保电名称
        driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys(u"测试新增保电名称%s"%a)
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[4]/div/div/ul/li[2]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
        driver.find_element_by_xpath("//div[5]/div/div/ul/li").click()
        #选择线路
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        driver.find_element_by_xpath("//div[2]/div[2]/div/div/div[3]/table/tbody/tr/td/div/label/span/span").click()
        #保电范围
        time.sleep(1)
        driver.find_element_by_xpath("//div[5]/div/div[3]/span/button[2]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[3]/div[2]/div/div/div/div/span/span/i").click()

        driver.find_element_by_xpath("(//input[@type='text'])[15]").click()
        driver.find_element_by_xpath("//div[7]/div/div/ul/li").click()
        #起始位置
        driver.find_element_by_xpath("(//input[@type='text'])[16]").click()
        driver.find_element_by_xpath("//div[8]/div/div/ul/li[2]").click()
        #结束位置
        driver.find_element_by_xpath("(//input[@type='text'])[17]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[9]/div/div/ul/li[2]/span").click()
        #导入按钮
        driver.find_element_by_xpath("//div[2]/div/div/div/i").click()
        #勾选记录
        driver.find_element_by_xpath("//div[4]/div/div/div[3]/table/tbody/tr/td/div").click()
        time.sleep(1)
        # driver.find_element_by_xpath("//div[4]/div/div/div[3]/table/tbody/tr/td/div/label/span/span").click()
        #点击确定
        driver.find_element_by_xpath("//div[6]/div/div[3]/span/button[2]/span").click()
        #开始时间
        driver.find_element_by_xpath("(//input[@name=''])[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//tr[4]/td[5]/div/span").click()
        #结束时间
        driver.find_element_by_xpath("(//input[@name=''])[4]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//button[@type='button'])[40]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[8]/div/div/div[2]/table/tbody/tr[2]/td[4]/div/span").click()
        #保电地址
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[12]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[12]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[12]").send_keys(u"测试保电地址")
        time.sleep(1)
        #风险等级
        driver.find_element_by_xpath("(//input[@type='text'])[13]").click()
        driver.find_element_by_xpath("//div[9]/div/div/ul/li[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys("CODE100010")
        driver.find_element_by_xpath("//textarea").click()
        driver.find_element_by_xpath("//textarea").clear()
        driver.find_element_by_xpath("//textarea").send_keys(u"测试保电内容")
        driver.find_element_by_xpath("//div[8]/div/div/div/div/textarea").clear()
        driver.find_element_by_xpath("//div[8]/div/div/div/div/textarea").send_keys(u"测试保电要求")
        driver.find_element_by_xpath("//div[9]/div/div/div/div/textarea").clear()
        driver.find_element_by_xpath("//div[9]/div/div/div/div/textarea").send_keys(u"测试保电原因")
        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
        time.sleep(2)
        print("保电任务创建成功!!!")

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
    unittest.main(verbosity=2)
