from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#-----------------------------------期末評量問卷--------------------------------------------

PATH = "C:/Users/User/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://sso.nutc.edu.tw/eportal/")

account = driver.find_element_by_id("ContentPlaceHolder1_Account")
account.send_keys("account")
password = driver.find_element_by_id("ContentPlaceHolder1_Password")
password.send_keys("password")

time.sleep(5)                     # wait five mins 
password.send_keys(Keys.RETURN)   # press enter
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_MyArea1_A7"))
)
link = driver.find_element_by_link_text("學生管理系統")
link.click()   # Enter student manage system
driver.switch_to.window(driver.window_handles[1])   # 切換到新分頁

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "DivLogo"))
)
driver.find_element_by_class_name('MainMenuBigIcon').click()
time.sleep(1)
driver.find_element_by_class_name('MainMenuStyle01').click()
time.sleep(1)
driver.find_element_by_class_name('ares-icon-search-teacher').click()
time.sleep(1)
for i in range(2):
    btn = driver.find_element_by_class_name('btn-default')
    btn.click()
    time.sleep(1)
    rads = driver.find_elements_by_css_selector('input[value="2"]')
    for rad in rads:
        rad.click()
    driver.find_element_by_xpath('//*[@id="ui_form"]/table[2]/tbody/tr[1]/td/a[1]').click()
    time.sleep(1)
    driver.switch_to.alert.accept()    # switch to  alert then click accept 
    time.sleep(1)
   

