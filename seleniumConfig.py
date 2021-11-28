import time
from selenium import webdriver

def login(timeout):
    driver = webdriver.Chrome(executable_path="C:/Users/ADMIN/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get ("https://banhang.upgo.vn")
    print (driver.title  )
    time.sleep(timeout)
    print("========= LOGIN=================")
    username = '0328716036'
    password = 'minh123456'
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id ("password").send_keys(password)
    driver.find_element_by_class_name("my-4").click()
    time.sleep(2)
    driver.get ("https://banhang.upgo.vn/#/item/list")
    time.sleep(2)
    try:
        res=  driver.find_elements_by_class_name("p-button-label")[0].text
        print('========================================')
        if(res=='Thêm'):
            print ("LOGIN THÀNH CÔNG !")
        else:
            print("LOGIN KHÔNG THÀNH CÔNG !")
    except:
        print("LOGIN KHÔNG THÀNH CÔNG !")
    return driver