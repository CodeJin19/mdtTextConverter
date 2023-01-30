from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def document_initialised(driver):
    return driver.execute_script("return initialised")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver')

    try:
        driver.get('https://www.wowhead.com/') #driver 버전은 최신이어야 함
        time.sleep(5)

        wait = WebDriverWait(driver, 30)

        print("------------- starting click -------------")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))).click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "notifications-dialog-buttons-decline"))).click() #class 이름으로 검색할 때는 중간에 공백 불가


        print("------------- search -------------")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[1]/form/input").send_keys("Stormcaller Boroo")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[1]/a").click()

        time.sleep(5)

        #/html/body/div[4]/div/div[4]/a[8]
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div[4]/a[8]").click()




    except BaseException as e:
            print("----------------------------------")
            print("error :")
            print(e)
            print("----------------------------------")
    finally:
            driver.quit()
            print(datetime.datetime.now())
            print("quit driver")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''
    lines = int(input())
    beforeConvertArr = []
    afterConvertArr = []

    for i in range(0, lines):
        line = input()
        beforeConvertArr.append(line.split('"')[1])

    print(beforeConvertArr)
'''
