from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://m.facebook.com")

time.sleep(1)
#
# idvar = driver.find_element_by_id('m_login_email')
# idvar.send_keys('')
print('페이스북에 로그인해주세요. 30초 후에 시작됩니다.')
time.sleep(30)
button_login = driver.find_element(By.XPATH, "//button[@value='로그인']")
button_login.click()
time.sleep(2)


while True:
    driver.get("https://m.facebook.com/friends/center/requests/outgoing")
    time.sleep(1)
    # driver.find_elements(By.XPATH("//button[@value='취소']"))
    button_cancel = driver.find_elements(By.XPATH, "//button[@value='취소']")
    if not button_cancel:
        break
    for button in button_cancel:
        try:
            button.click()
        except:
            continue
    time.sleep(2)

