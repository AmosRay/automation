from selenium import webdriver
wd = webdriver.Chrome('chromedriver.exe')
wd.implicitly_wait(5)
wd.get('https://www.baidu.com')
element = wd.find_element_by_id('kw').send_keys('shenwu\n')
print(element.text)
wd.quit()