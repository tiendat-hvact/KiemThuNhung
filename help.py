import time

# lay tag co id duoc truyen vao
def getById(driver,id):
    return driver.find_element_by_id(id)
    
# nhap vao o input co id va data truyen vao
def inputById(driver,id,data):
    driver.find_element_by_id(id).send_keys(data)

# lay tag co class duoc truyen vao
def getByClass(driver,classname):
    return driver.find_element_by_class_name(classname)

def getsByClass(driver,classname):
    return driver.find_elements_by_class_name(classname)

# find Nane
def getByName(driver,name):
    return driver.find_element_by_name(name)

#find Names
def getBysName(driver,name):
    return driver.find_elements_by_name(name)

# get link
def getLink(driver,Link):
    return driver.get(Link)

# lay url hien
def getCurrentURL(driver):
    return driver.current_url

# check nextpage
def isNextPage():
    # handle ...
    return true

# Lưu file
def create_file_result(filename,data):
    src = 'src/result/'
    file = 'src/result/' + filename + ".txt"
    with open(file,'a',encoding = 'utf-8') as f:
        f.write(data)
        f.write("\n")
        f.close()

#===========================================================================
# data = {"ID":"BTN_XEMCHITIET","page":"https://banhang.upgo.vn/#/dashboard","nextpage":"https://banhang.upgo.vn/#/revenue"}
class check_btn_nextpage():
    class meta:
        " Chứa tất cả các cách test button"
        ''' data = {"page":"https://banhang.upgo.vn/#/dashboard","nextpage":"https://banhang.upgo.vn/#/revenue",} '''
        pass
        
    # by class name
    def check_btn_class_name(driver,data,class_name):
        page = data['page']
        nextpage = data['nextpage']
        # driver.get(page)
        time.sleep(2)
        print(class_name)
        getByClass(driver,class_name).click()
        time.sleep(2)
        Url_Page = getCurrentURL(driver)
        print(Url_Page)
        result = False
        if Url_Page == nextpage :
            result =True
        return  result

    def check_btn_class_names(driver,data,class_name,i):
        page = data['page']
        nextpage = data['nextpage']
        # driver.get(page)
        time.sleep(2)
        print(class_name)
        getsByClass(driver,class_name)[i].click()
        time.sleep(2)
        Url_Page = getCurrentURL(driver)
        print(Url_Page)
        result = False
        if Url_Page == nextpage :
            result =True
        return  result

    def check_btn_class_name2(driver,data,class_name):
        page = data['page']
        nextpage = data['nextpage']
        # driver.get(page)
        time.sleep(2)
        print(class_name)
        getsByClass(driver,class_name)[0].click()
        time.sleep(3)
        Url_Page = getCurrentURL(driver)
        print(Url_Page)
        result = False
        if Url_Page == nextpage :
            result =True
        return  result
    
    def check_btn_class_name3(driver,data,class_name):
        page = data['page']
        nextpage = data['nextpage']
        # driver.get(page)
        time.sleep(2)
        print(class_name)
        getsByClass(driver,class_name)[3].click()
        time.sleep(3)
        Url_Page = getCurrentURL(driver)
        print(Url_Page)
        result = False
        if Url_Page == nextpage :
            result =True
        return  result

# tao khoang trắng sau text khi ghi file
def createLine():
    text ="┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈"
    create_file_result('sanpham',text)
def createLine2():
    text ="-----------------------------------------------------------------------------------------------"
    create_file_result('kq_addCoso',text)

def createLineEdit():
    text ="-----------------------------------------------------------------------------------------------"
    create_file_result('kq_editCoso',text)

def createLineNewKhuVuc():
    text ="-----------------------------------------------------------------------------------------------"
    create_file_result('kq_addKhuVuc',text)

def createLineNewFastKhuVuc():
    text ="-----------------------------------------------------------------------------------------------"
    create_file_result('kq_addFastKhuVuc',text)

def createLineEditKV():
    text ="-----------------------------------------------------------------------------------------------"
    create_file_result('kq_editKhuVuc',text)
