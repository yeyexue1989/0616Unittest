from selenium import webdriver
import requests,time

def getRowNo(url):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)

        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"杨斌")
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[2]/span").click()
        driver.find_element_by_id("a-login").click()
        time.sleep(4)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[12]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div[2]/ul/li[12]/ul/li[2]").click()
        time.sleep(1)
        elements = driver.find_elements_by_xpath("(//table[1])[2]/tbody/tr")
        print(type(elements))
        print(len(elements))
        for element in elements:
            print(element.text)
        return elements

if __name__ == '__main__':
    url = "http://192.168.0.3:8081/#/login"
    getRowNo(url)