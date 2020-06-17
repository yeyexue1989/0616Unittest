from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://192.168.0.3:8081/#/login")
driver.find_element_by_id("input-username").click()
driver.find_element_by_id("input-username").clear()
driver.find_element_by_id("input-username").send_keys(u"杨斌")
driver.find_element_by_id("input-password").clear()
driver.find_element_by_id("input-password").send_keys("admin123")
driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
time.sleep(1)
driver.find_element_by_xpath("//li[2]/span").click()
time.sleep(1)
driver.find_element_by_id("a-login").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[12]/div").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[12]/ul/li").click()
time.sleep(1)

name = driver.find_element_by_xpath('//table/tbody/tr[1]/td[3]/div').text
# name = name_element.text

print(name)
#勾选记录