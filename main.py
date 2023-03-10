from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

engList = []
korList = []
outputList = []


def document_initialised(driver):
    return driver.execute_script("return initialised")

def searchListGenerator():
    print("searchListGenerator CALL")
    print("enter the number of lines to convert")
    lines = int(input())

    if lines == 1:
        print("enter " + lines + " line to convert")
    else:
        print("enter " + lines + " lines to convert")

    for i in range(0, lines):
        line = input()
        engList.append(line.split('"')[1])
        korList.append("")
        outputList.append("")

def crawler():
    print("crawler CALL")
    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver')

    try:
        driver.get('https://www.wowhead.com/')  # driver 버전은 최신이어야 함
        time.sleep(5)

        wait = WebDriverWait(driver, 30)

        print("LOG-01\tclick pop-ups")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "notifications-dialog-buttons-decline"))).click()  # class 이름으로 검색할 때는 중간에 공백 불가

        for i in range(len(engList)):
            print("LOG-02\tstart search")
            # 1줄짜리 데이터 "Stormcaller Boroo"
            # 3줄짜리 데이터 "Nokhud Saboteur"
            driver.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[1]/form/input").clear()
            driver.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[1]/form/input").send_keys(engList[i])
            driver.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[1]/a").click()

            time.sleep(5)

            '''
            #stackoverflow
            #이렇게 하면 th/tr과 /tbody/tr을 모두 찾아서 오차가 1 생긴다
            table = driver.find_element(By.XPATH, "//*[@id='tab-npcs']/div[2]/div/table");
    
            cnt = 0
            for tr in table.find_elements(By.TAG_NAME, "tr"):
                cnt += 1
    
            print(cnt)
            '''

            print("LOG-03\tsearching table")
            list = driver.find_elements(By.XPATH, "//*[@id='tab-npcs']/div[2]/div/table/tbody/tr")

            print("LOG-03-1\tlen(list) : " + str(len(list)))

            if len(list) == 0:
                try:
                    driver.find_element(By.XPATH, "//*[@id='search-tabs']/div/ul/li[5]/a").click()
                    list = driver.find_elements(By.XPATH, "//*[@id='tab-npcs']/div[2]/div/table/tbody/tr")

                    print("LOG-03-2\tlen(list) : " + str(len(list)))
                except BaseException as e3:
                    print("----------------------------------")
                    print("error at " + engList[i] + " E3")
                    print(e3)
                    print("----------------------------------")


            if len(list) == 1:
                driver.find_element(By.XPATH, "//*[@id='tab-npcs']/div[2]/div/table/tbody/tr/td[1]/a").click()
            else:
                driver.find_element(By.XPATH, "//*[@id='tab-npcs']/div[2]/div/table/tbody/tr[1]/td[1]/a").click()

            time.sleep(5)

            try :
                print("LOG-04-01\tswap language")
                driver.find_element(By.XPATH, "/html/body/div[4]/div/div[4]/a[8]").click()

                #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[10]/div/div/div[2]/a[1]"))).click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '한국어')]"))).click()

                time.sleep(1)

                name = driver.find_element(By.XPATH, "//*[@id='main-contents']/div[3]/h1").text

                korList[i] = name
                print(engList[i] + " : " + korList[i])

                print("LOG-04-02\tswap language")
                driver.find_element(By.XPATH, "/html/body/div[4]/div/div[4]/a[8]").click()

                #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[10]/div/div/div[5]/a[1]"))).click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "menu-inner")))
                menu = driver.find_element(By.CLASS_NAME, "menu-inner")
                menu.find_element(By.XPATH, "//*[contains(text(), 'English')]").click()

                time.sleep(1)
            except BaseException as e2:
                print("----------------------------------")
                print("error at " + engList[i])
                print(e2)
                print("----------------------------------")
            finally:
                continue

    except BaseException as e:
        print("----------------------------------")
        print("error :")
        print(e)
        print("----------------------------------")
    finally:
        driver.quit()
        print(datetime.datetime.now())
        print("quit driver")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    searchListGenerator()

    '''
    engList = ["Maruuk"]
    korList = [""]
    outputList = [""]
    '''

    crawler()

    for i in range(0, len(engList)):
        outputList[i] = "L[\"" + engList[i] + "\"] = \"" + korList[i] + "\""

    for i in range(0, len(outputList)):
        print(outputList[i])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/