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
    lines = int(input())

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

            # 한 줄짜리 테이블 XPath
            # //*[@id="tab-npcs"]/div[2]/div/table
            # row XPath
            # //*[@id="tab-npcs"]/div[2]/div/table/tbody/tr/td[1]/a

            # 세 줄짜리 테이블 XPath
            # //*[@id="tab-npcs"]/div[2]/div/table
            # row XPath
            # //*[@id="tab-npcs"]/div[2]/div/table/tbody/tr[1]/td[1]/a

            print("LOG-03\tsearching table")
            list = driver.find_elements(By.XPATH, "//*[@id='tab-npcs']/div[2]/div/table/tbody/tr");

            print("LOG-03-1\tlen(list) : " + str(len(list)))

            '''
            War Ohuna
            LOG-03-1	len(list) : 0
            ----------------------------------
            error :
            Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tab-npcs']/div[2]/div/table/tbody/tr[1]/td[1]/a"}
              (Session info: chrome=110.0.5481.104)
            '''

            if len(list) == 0:
                #todo
                print("ERROR AT " + engList[i])
                continue
            elif len(list) == 1:
                driver.find_element(By.XPATH, "//*[@id='tab-npcs']/div[2]/div/table/tbody/tr/td[1]/a").click()
            else:
                driver.find_element(By.XPATH, "//*[@id='tab-npcs']/div[2]/div/table/tbody/tr[1]/td[1]/a").click()

            time.sleep(5)

            try :
                print("LOG-04-01\tswap language")
                driver.find_element(By.XPATH, "/html/body/div[4]/div/div[4]/a[8]").click()

                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[10]/div/div/div[2]/a[1]"))).click()

                time.sleep(1)

                name = driver.find_element(By.XPATH, "//*[@id='main-contents']/div[3]/h1").text

                korList[i] = name
                print(engList[i] + " : " + korList[i])

                print("LOG-04-02\tswap language")
                driver.find_element(By.XPATH, "/html/body/div[4]/div/div[4]/a[8]").click()

                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[10]/div/div/div[5]/a[1]"))).click()

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
    engList = ["War Ohuna"]
    korLIst = [""]
    outputList = [""]
    '''

    crawler()

    for i in range(0, len(engList)):
        outputList[i] = "L[\"" + engList[i] + "\"] = \"" + korList[i] + "\""

    for i in range(0, len(outputList)):
        print(outputList[i])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''
log
D:\mdtTextConverter\venv\Scripts\python.exe D:\mdtTextConverter\main.py 
searchListGenerator CALL
10
L["War Ohuna"] = "War Ohuna"
L["Nokhud Neophyte"] = "Nokhud Neophyte"
L["Desecrated Bakar"] = "Desecrated Bakar"
L["Soulharvester Mandakh"] = "Soulharvester Mandakh"
L["Risen Mystic"] = "Risen Mystic"
L["Granyth"] = "Granyth"
L["Nokhud Warhound"] = "Nokhud Warhound"
L["Nokhud Plainstomper"] = "Nokhud Plainstomper"
L["Primalist Thunderbeast"] = "Primalist Thunderbeast"
L["Balakar Khan"] = "Balakar Khan"
crawler CALL
D:\mdtTextConverter\main.py:35: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
  driver = webdriver.Chrome('C:\ChromeDriver\chromedriver')
LOG-01	click pop-ups
LOG-02	start search
LOG-03	searching table
LOG-03-1	len(list) : 0
ERROR AT War Ohuna
LOG-02	start search
LOG-03	searching table
LOG-03-1	len(list) : 1
LOG-04-01	swap language
----------------------------------
error at Nokhud Neophyte
Message: 
Stacktrace:
Backtrace:
	(No symbol) [0x00E137D3]
	(No symbol) [0x00DA8B81]
	(No symbol) [0x00CAB36D]
	(No symbol) [0x00CDD382]
	(No symbol) [0x00CDD4BB]
	(No symbol) [0x00D13302]
	(No symbol) [0x00CFB464]
	(No symbol) [0x00D11215]
	(No symbol) [0x00CFB216]
	(No symbol) [0x00CD0D97]
	(No symbol) [0x00CD253D]
	GetHandleVerifier [0x0108ABF2+2510930]
	GetHandleVerifier [0x010B8EC1+2700065]
	GetHandleVerifier [0x010BC86C+2714828]
	GetHandleVerifier [0x00EC3480+645344]
	(No symbol) [0x00DB0FD2]
	(No symbol) [0x00DB6C68]
	(No symbol) [0x00DB6D4B]
	(No symbol) [0x00DC0D6B]
	BaseThreadInitThunk [0x759400F9+25]
	RtlGetAppContainerNamedObjectPath [0x774D7BBE+286]
	RtlGetAppContainerNamedObjectPath [0x774D7B8E+238]

----------------------------------
LOG-02	start search
LOG-03	searching table
LOG-03-1	len(list) : 2
LOG-04-01	swap language
Desecrated Bakar : 더럽혀진 바카르
LOG-04-02	swap language
LOG-02	start search
LOG-03	searching table
LOG-03-1	len(list) : 1
LOG-04-01	swap language
Soulharvester Mandakh : 영혼수확자 만다크
LOG-04-02	swap language
LOG-02	start search
LOG-03	searching table
LOG-03-1	len(list) : 1
LOG-04-01	swap language
Risen Mystic : 되살아난 비술사
LOG-04-02	swap language
----------------------------------
error at Risen Mystic
Message: 
Stacktrace:
Backtrace:
	(No symbol) [0x00E137D3]
	(No symbol) [0x00DA8B81]
	(No symbol) [0x00CAB36D]
	(No symbol) [0x00CDD382]
	(No symbol) [0x00CDD4BB]
	(No symbol) [0x00D13302]
	(No symbol) [0x00CFB464]
	(No symbol) [0x00D11215]
	(No symbol) [0x00CFB216]
	(No symbol) [0x00CD0D97]
	(No symbol) [0x00CD253D]
	GetHandleVerifier [0x0108ABF2+2510930]
	GetHandleVerifier [0x010B8EC1+2700065]
	GetHandleVerifier [0x010BC86C+2714828]
	GetHandleVerifier [0x00EC3480+645344]
	(No symbol) [0x00DB0FD2]
	(No symbol) [0x00DB6C68]
	(No symbol) [0x00DB6D4B]
	(No symbol) [0x00DC0D6B]
	BaseThreadInitThunk [0x759400F9+25]
	RtlGetAppContainerNamedObjectPath [0x774D7BBE+286]
	RtlGetAppContainerNamedObjectPath [0x774D7B8E+238]

----------------------------------
LOG-02	start search
LOG-03	searching table
LOG-03-1	len(list) : 0
ERROR AT Granyth
LOG-02	start search
LOG-03	searching table
LOG-03-1	len(list) : 3
LOG-04-01	swap language
Nokhud Warhound : [Nokhud Warhound] <[Tier 1 Beast]>
LOG-04-02	swap language
LOG-02	start search
LOG-03	searching table
LOG-03-1	len(list) : 1
LOG-04-01	swap language
Nokhud Plainstomper : 노쿠드 평야활보자
LOG-04-02	swap language
LOG-02	start search
LOG-03	searching table
LOG-03-1	len(list) : 1
LOG-04-01	swap language
Primalist Thunderbeast : 원시술사 천둥야수
LOG-04-02	swap language
LOG-02	start search
LOG-03	searching table
LOG-03-1	len(list) : 3
LOG-04-01	swap language
Balakar Khan : 발라카르 칸
LOG-04-02	swap language
----------------------------------
error at Balakar Khan
Message: 
Stacktrace:
Backtrace:
	(No symbol) [0x00E137D3]
	(No symbol) [0x00DA8B81]
	(No symbol) [0x00CAB36D]
	(No symbol) [0x00CDD382]
	(No symbol) [0x00CDD4BB]
	(No symbol) [0x00D13302]
	(No symbol) [0x00CFB464]
	(No symbol) [0x00D11215]
	(No symbol) [0x00CFB216]
	(No symbol) [0x00CD0D97]
	(No symbol) [0x00CD253D]
	GetHandleVerifier [0x0108ABF2+2510930]
	GetHandleVerifier [0x010B8EC1+2700065]
	GetHandleVerifier [0x010BC86C+2714828]
	GetHandleVerifier [0x00EC3480+645344]
	(No symbol) [0x00DB0FD2]
	(No symbol) [0x00DB6C68]
	(No symbol) [0x00DB6D4B]
	(No symbol) [0x00DC0D6B]
	BaseThreadInitThunk [0x759400F9+25]
	RtlGetAppContainerNamedObjectPath [0x774D7BBE+286]
	RtlGetAppContainerNamedObjectPath [0x774D7B8E+238]

----------------------------------
2023-02-18 13:50:42.754299
quit driver
L["War Ohuna"] = ""
L["Nokhud Neophyte"] = ""
L["Desecrated Bakar"] = "더럽혀진 바카르"
L["Soulharvester Mandakh"] = "영혼수확자 만다크"
L["Risen Mystic"] = "되살아난 비술사"
L["Granyth"] = ""
L["Nokhud Warhound"] = "[Nokhud Warhound] <[Tier 1 Beast]>"
L["Nokhud Plainstomper"] = "노쿠드 평야활보자"
L["Primalist Thunderbeast"] = "원시술사 천둥야수"
L["Balakar Khan"] = "발라카르 칸"

Process finished with exit code 0

'''