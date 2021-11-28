from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def InputJisseki(df):

    # 定数宣言
    CONST_WEBDRIVER_PATH = r"C:\Users\800240\PycharmProjects\Driver\IEDriverServer.exe"
    CONST_LOGIN_URL = "http://172.16.xxx.xxx:8080/sts/login.jsp"
    CONST_INPUT_URL = "http://172.16.xxx.xxx:8080/sts/Input.jsp?"
    CONST_ID = "userid"
    CONST_PASS = "Password"

    browser = webdriver.Ie(CONST_WEBDRIVER_PATH)

    browser.get(CONST_LOGIN_URL)

    Userid = browser.find_element_by_id('userCd')
    Userid.send_keys(CONST_ID)

    Pass = browser.find_element_by_id('password')
    Pass.send_keys(CONST_PASS)

    browser.find_element_by_id('btnLogin').click()

    browser.get(CONST_INPUT_URL)

    print("ループ開始")

    df = df.sort_values('date')
    print(df)
    # print(browser.execute_script("document.getElementById('divTotal').scrollLeft"))
    # scrollElement = browser.find_element_by_id('divTotal')
    # scrollElement.

    browser.execute_script("document.getElementById('divTotal').scrollLeft = 0")

    for i in range(len(df.index)):
        try:
            print(df.Pkey[i])
            InputElement = browser.find_element_by_id(df.Pkey[i])
            InputElement.send_keys(df.time[i])
            print(df.time[i])
            browser.execute_script("document.getElementById('divTotal').scrollLeft += 12")
        except:
            pass

    # .execute_script
    # var obj = document.getElementById('divTotal').scrollLeft = 0;
    # obj.scrollTop = obj.scrollHeight;

    #id:divTotal
    # actions = new
    # Actions(driver)
    # actions.move_to_element(element)
    # actions.perform()

    browser.find_element_by_id('btnReg').click()
