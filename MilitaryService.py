## Import Package
from selenium import webdriver
import time
## Enabled Chrome function 打開模擬瀏覽器
chrome_browser = webdriver.Chrome()
## go to the website
chrome_browser.get('https://www.ris.gov.tw/aw_pub_rsc/mc/physicalexam/')
time.sleep(2)
personid = chrome_browser.find_element_by_xpath('//*[@id="personId"]')
personid.send_keys('B123456789')

#https://matters.news/@CHWang/coding%E8%B5%B7%E4%BE%86-python%E8%87%AA%E5%8B%95%E5%8C%96%E7%88%AC%E8%9F%B2-selenium%E5%A5%97%E4%BB%B6-%E6%96%B9%E6%B3%95%E6%95%99%E5%AD%B8-bafyreieq5sbozlrboqb42eg2yu3q6vrtqshjbuztq6xiy4tiz3d4sxydzm