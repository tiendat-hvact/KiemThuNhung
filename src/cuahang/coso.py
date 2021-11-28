import json
import time
import help
from help import check_btn_nextpage
from selenium.webdriver.common.keys import Keys
f = open('C:/Users/ADMIN/Documents/kiemthunhung/testing/src/cuahang/dataH.json', encoding='utf-8')  
list = json.load(f)
newCoso = list['newCoso']
addCosoMPTY = list['addCosoMPTY']
editCoso = list['editCoso']


# newCoso = [
#   {"ID":"CSBH_aFULL","macoso":"YT1","tencoso":"co so AAA1", "sdtcoso":"0934127238", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà", "expected":"nextPage"},

#   {"ID":"CSBH_aMCS01","macoso":"%^@$AAA","tencoso":"co so AAA1", "sdtcoso":"0934127238", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà", "expected":"un_nextPage"},

#   {"ID":"CSBH_aMCS02","macoso":"","tencoso":"co so AAA1", "sdtcoso":"0934127238", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà","expected":"nextPage"},

#   # {"ID":"CSBH_aTCS01","macoso":"Vse1","tencoso":"", "sdtcoso":"0934127238", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà", "expected":"un_nextPage"},

#   {"ID":"CSBH_aTCS02","macoso":"VAA1","tencoso":"%@!#Co so XXY2", "sdtcoso":"0934127238", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà", "expected":"un_nextPage"},

#   {"ID":"CSBH_aSDT01","macoso":"AAA1","tencoso":"%!_$$Co soAAA1", "sdtcoso":"", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà","expected":"un_nextPage"},

#   {"ID":"CSBH_aSDT02","macoso":"AAA1","tencoso":"co so AAA1", "sdtcoso":"%$@0934127238", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà", "expected":"un_nextPage"},

#   # {"ID":"CSBH_aMPTY","macoso":"","tencoso":"", "sdtcoso":"", "tpcoso":"", "huyencoso":"", "xacoso":"", "expected":"un_nextPage"},

#   # {"ID":"CSBH_aDCHI","macoso":"AAA1","tencoso":"co so AAA1", "sdtcoso":"0934127238", "tpcoso":"", "huyencoso":"", "xacoso":"", "expected":"un_nextPage"},

#   ]
# addCosoMPTY = [
#   {"ID":"CSBH_aMPTY","macoso":"","tencoso":"", "sdtcoso":"", "tpcoso":"", "huyencoso":"", "xacoso":"", "expected":"un_nextPage"},

#   {"ID":"CSBH_aDCHI","macoso":"AAA1","tencoso":"co so AAA1", "sdtcoso":"0934127238", "tpcoso":"", "huyencoso":"", "xacoso":"", "expected":"un_nextPage"},
#   ]
# editCoso = [
#   {"ID":"CSBH_eMCS01","macoso":"$@!ATS","tencoso":"co so AAA1", "sdtcoso":"", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà","expected":"un_nextPage"},

#   {"ID":"CSBH_eMCS02","macoso":"","tencoso":"co so AAA1", "sdtcoso":"%$#0934127238", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà", "expected":"nextPage"},

#   {"ID":"CSBH_eTCS01","macoso":"AAA1","tencoso":"!$!CosoAAA1", "sdtcoso":"0934127238", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà", "expected":"un_nextPage"},

#   {"ID":"CSBH_eTCS02","macoso":"AAA1","tencoso":"", "sdtcoso":"0934127238", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà", "expected":"un_nextPage"},

#   {"ID":"CSBH_eSDT01","macoso":"AAA1","tencoso":"Coso AAA1", "sdtcoso":"!#@$0934127238", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà", "expected":"un_nextPage"},

#   {"ID":"CSBH_eSDT02","macoso":"AAA1","tencoso":"Coso AAA1", "sdtcoso":"", "tpcoso":"Hà Nội", "huyencoso":"Thạch Thất", "xacoso":"Thạch Hoà", "expected":"un_nextPage"},]
# ++++++++++++++++++++ THÊM +++++++++++++++++++++++++++
def addCoSo(driver):
  print('<+++ Adding newCoso +++>')
  driver.get("https://banhang.upgo.vn/#/workstation/collection")
  time.sleep(3)
  textResult = "%15s" %('ID') +"\t|"+ "%15s" %('MACOSO') +"\t|"+ "%15s" %('TENCOSO') +"\t|"+ "%15s" %('SDTCOSO')  +"\t|"+ "%15s" %('EXPECTED') +"\t|"+"STATUS"
  help.create_file_result('kq_addCoso',textResult)
  help.createLine2()
  # newCoSo = '{"ma":"X", "ten":"co so xxx", "tinh":"Hà Nội", "huyen":"Thạch Thất",
  #  "xa":"Tiến Xuân", "diachi":"Tiến Xuân, Thạch Thất, Hà Nôi"}'
  ROUND = 0
  roundMPTY = 0 
  for cs in newCoso:
    #nhan them
    ROUND +=1
    print('---> looping CS <---' , ROUND)
    help.getByClass(driver,"p-button-label").click()
    time.sleep(1) 
    isNextPage = insertData(driver,cs)
    print(isNextPage)
    if(isNextPage==True and cs['expected']=='nextPage'):
      print('========1=========')
      textResult1 = "%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso'] +"\t|"+  "%15s" %cs['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_addCoso',textResult1)
      help.createLine2()

    elif(isNextPage==False and cs['expected']=='un_nextPage'):
      print('========22=========')
      textResult2 ="%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso'] +"\t|"+ "%15s" %cs['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_addCoso',textResult2)
      help.createLine2()
      driver.get ("https://banhang.upgo.vn/#/workstation/collection")
      time.sleep(3)

    elif(isNextPage==True and cs['expected']=='un_nextPage'):
      print('========333=========')
      textResult3 ="%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso'] +"\t|"+ "%15s" %cs['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_addCoso',textResult3)
      help.createLine2()

    elif(isNextPage==False and cs['expected']=='nextPage'):
      print('========444=========')
      textResult4 ="%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso']  +"\t|"+ "%15s" %cs['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_addCoso',textResult4)
      help.createLine2()
      driver.get ("https://banhang.upgo.vn/#/workstation/collection")
      time.sleep(3)
    time.sleep(1)

  for cs in addCosoMPTY:
    #nhan them
    roundMPTY +=1
    print('-> empty CS <-' , roundMPTY)
    help.getByClass(driver,"p-button-label").click()
    time.sleep(1) 
    isNextPage2 =  insertDataMPTY(driver, cs)
    print(isNextPage2)
    if(isNextPage2==True and cs['expected']=='nextPage'):
      print('========1=========')
      textResult1 = "%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso'] +"\t|"+  "%15s" %cs['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_addCoso',textResult1)
      help.createLine2()

    elif(isNextPage2==False and cs['expected']=='un_nextPage'):
      print('========22=========')
      textResult2 ="%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso'] +"\t|"+ "%15s" %cs['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_addCoso',textResult2)
      help.createLine2()
      driver.get ("https://banhang.upgo.vn/#/workstation/collection")
      time.sleep(3)

    elif(isNextPage2==True and cs['expected']=='un_nextPage'):
      print('========333=========')
      textResult3 ="%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso'] +"\t|"+ "%15s" %cs['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_addCoso',textResult3)
      help.createLine2()

    elif(isNextPage2==False and cs['expected']=='nextPage'):
      print('========444=========')
      textResult4 ="%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso']  +"\t|"+ "%15s" %cs['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_addCoso',textResult4)
      help.createLine2()
      driver.get ("https://banhang.upgo.vn/#/workstation/collection")
      time.sleep(3)
    time.sleep(1)
  
# ========================= SỬA =============================
def editCoSo(driver):
  print('<--- Editing --->')
  driver.get ("https://banhang.upgo.vn/#/workstation/collection")
  time.sleep(3)
  textResult = "%15s" %('ID') +"\t|"+ "%15s" %('MACOSO') +"\t|"+ "%15s" %('TENCOSO') +"\t|"+ "%15s" %('SDTCOSO')  +"\t|"+ "%15s" %('EXPECTED') +"\t|"+"STATUS"
  help.create_file_result('kq_editCoso',textResult)
  help.createLineEdit()
  # newCoSo = '{"ma":"X", "ten":"co so xxx", "tinh":"Hà Nội", "huyen":"Thạch Thất",
  #  "xa":"Tiến Xuân", "diachi":"Tiến Xuân, Thạch Thất, Hà Nôi"}'
  roundEdit = 0
  for cs in editCoso:
    #nhan them
    roundEdit +=1
    print('---> editing CS <---' , roundEdit)
    help.getsByClass(driver,"fa-edit")[0].click()
    time.sleep(1) 
    isNextPage = editData(driver,cs)
    print('--chuyen trang edit--',isNextPage)
    if(isNextPage==True and cs['expected']=='nextPage'):
      print('========1=========')
      textResult1 = "%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso'] +"\t|"+  "%15s" %cs['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_editCoso',textResult1)
      help.createLineEdit()

    elif(isNextPage==False and cs['expected']=='un_nextPage'):
      print('========22=========')
      textResult2 ="%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso'] +"\t|"+ "%15s" %cs['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_editCoso',textResult2)
      help.createLineEdit()
      driver.get ("https://banhang.upgo.vn/#/workstation/collection")
      time.sleep(3)

    elif(isNextPage==True and cs['expected']=='un_nextPage'):
      print('========333=========')
      textResult3 ="%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso'] +"\t|"+ "%15s" %cs['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_editCoso',textResult3)
      help.createLineEdit()

    elif(isNextPage==False and cs['expected']=='nextPage'):
      print('========444=========')
      textResult4 ="%15s" %cs['ID'] +"\t|"+ "%15s" %cs['macoso'] +"\t|"+ "%15s" %cs['tencoso'] +"\t|"+ "%15s" %cs['sdtcoso']  +"\t|"+ "%15s" %cs['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_editCoso',textResult4)
      help.createLineEdit()
      driver.get ("https://banhang.upgo.vn/#/workstation/collection")
      time.sleep(3)
    time.sleep(1)
  changeSTT(driver)
  
# ====== Xoa =============>>>>
def xoaCoso(driver):
  print('<<< Deleting >>>')
  driver.get ("https://banhang.upgo.vn/#/workstation/collection")
  time.sleep(3)
  help.getsByClass(driver, 'fa-trash')[0].click()
  textResult2 ="%15s" %'dELETE' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+"FAIL"
  help.create_file_result('kq_editCoso',textResult2)
  help.createLineEdit()
# ===== TIM KIEM =============
def timCoso(driver):
  print('<<< Findingggg >>>')
  driver.get ("https://banhang.upgo.vn/#/workstation/collection")
  time.sleep(3)
  help.getByName(driver, 'area_name').send_keys("CS1"+ Keys.ENTER)
  del1 ="%15s" %'CSBH_fCSBH' +"\t|"+ "%15s" %'CS1' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+"FAIL"
  help.create_file_result('kq_editCoso',del1)
  help.createLineEdit()
  time.sleep(3)
  help.getByName(driver, 'area_name').clear()
  help.getByName(driver, 'area_name').send_keys(""+ Keys.ENTER)
  del2 ="%15s" %'CSBH_fMPTY' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+"PASS"
  help.create_file_result('kq_editCoso',del2)
  help.createLineEdit()
  time.sleep(3)
  help.getByName(driver, 'area_name').clear()
  help.getByName(driver, 'area_name').send_keys("&%*#CS1"+ Keys.ENTER)
  del3 ="%15s" %'CSBH_fSPEC' +"\t|"+ "%15s" %'&%*#CS1' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+"PASS"
  help.create_file_result('kq_editCoso',del3)
  help.createLineEdit()
  time.sleep(2)



def insertData(driver, cs):
  time.sleep(2)
  help.getByName(driver, 'workstation_no').send_keys(cs['macoso'])
  time.sleep(2)
  help.getByName(driver, 'workstation_name').send_keys(cs['tencoso'])
  time.sleep(2)
  help.getsByClass(driver, 'ng-valid')[2].send_keys(cs['sdtcoso'])
  time.sleep(2)
  help.getsByClass(driver, 'p-autocomplete-input')[0].send_keys(cs['tpcoso'])
  time.sleep(6)
  # help.getById(driver, 'pr_id_4_list').click()
  help.getsByClass(driver, 'p-autocomplete-items')[0].click()
  time.sleep(2)
  help.getsByClass(driver, 'p-autocomplete-input')[1].send_keys(cs['huyencoso'])
  time.sleep(6)
  help.getsByClass(driver, 'p-autocomplete-item')[0].click()
  time.sleep(2)
  help.getsByClass(driver, 'p-autocomplete-input')[2].send_keys(cs['xacoso'])
  time.sleep(6)
  help.getsByClass(driver, 'p-autocomplete-item')[0].click()
  time.sleep(2)
  #nhanluu
  data ={"page":"https://banhang.upgo.vn/#/workstation/create","nextpage":"https://banhang.upgo.vn/#/workstation/collection"}
  check = check_btn_nextpage.check_btn_class_name(driver, data, 'p-button-success')
  return check

def insertDataMPTY(driver, cs):
  time.sleep(2)
  help.getByName(driver, 'workstation_no').send_keys(cs['macoso'])
  time.sleep(2)
  help.getByName(driver, 'workstation_name').send_keys(cs['tencoso'])
  time.sleep(2)
  help.getsByClass(driver, 'ng-valid')[2].send_keys(cs['sdtcoso'])
  time.sleep(2)
  help.getsByClass(driver, 'p-autocomplete-input')[0].send_keys(cs['tpcoso'])
  time.sleep(4)
  # help.getsByClass(driver, 'p-autocomplete-items')[0].click()
  # time.sleep(2)
  help.getsByClass(driver, 'p-autocomplete-input')[1].send_keys(cs['huyencoso'])
  time.sleep(4)
  # help.getsByClass(driver, 'p-autocomplete-item')[0].click()
  # time.sleep(2)
  help.getsByClass(driver, 'p-autocomplete-input')[2].send_keys(cs['xacoso'])
  time.sleep(4)
  # help.getsByClass(driver, 'p-autocomplete-item')[0].click()
  # time.sleep(2)
  #nhanluu
  data ={"page":"https://banhang.upgo.vn/#/workstation/create","nextpage":"https://banhang.upgo.vn/#/workstation/collection"}
  check = check_btn_nextpage.check_btn_class_name(driver, data, 'p-button-success')
  return check

def editData(driver, cs):
  time.sleep(2)
  help.getByName(driver, 'workstation_no').clear()
  help.getByName(driver, 'workstation_no').send_keys(cs['macoso'])
  time.sleep(2)
  help.getByName(driver, 'workstation_name').clear()
  help.getByName(driver, 'workstation_name').send_keys(cs['tencoso'])
  time.sleep(2)
  help.getsByClass(driver, 'ng-valid')[2].clear()
  help.getsByClass(driver, 'ng-valid')[2].send_keys(cs['sdtcoso'])
  time.sleep(2)
  #nhanluu
  data ={"page":"https://banhang.upgo.vn/#/workstation/create","nextpage":"https://banhang.upgo.vn/#/workstation/collection"}
  check = check_btn_nextpage.check_btn_class_name(driver, data, 'p-button-success')
  return check

def changeSTT(driver):
    print('--Change STT--' )
    help.getsByClass(driver,"fa-edit")[0].click()
    time.sleep(2) 
    help.getsByClass(driver, 'p-inputswitch-slider')[0].click()
    data ={"page":"https://banhang.upgo.vn/#/workstation/create","nextpage":"https://banhang.upgo.vn/#/workstation/collection"}
    check = check_btn_nextpage.check_btn_class_name(driver, data, 'p-button-success')
    isNextPage = check
    print('--chuyen trang edit--',isNextPage)
    if(isNextPage==True ):
      print('========1=========')
      textResult1 = "%15s" %'CSBH_eTTCS' +"\t|"+ "%15s" %"" +"\t|"+ "%15s" %"" +"\t|"+ "%15s" %"" +"\t|"+  "%15s" %'nextPage' +"\t|"+"PASS"
      help.create_file_result('kq_editCoso',textResult1)
      help.createLineEdit()

    elif(isNextPage==False ):
      print('========22=========')
      textResult2 ="%15s" %'CSBH_eTTCS' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'un_nextPage' +"\t|"+"FAIL"
      help.create_file_result('kq_editCoso',textResult2)
      help.createLineEdit()
      driver.get ("https://banhang.upgo.vn/#/workstation/collection")
      time.sleep(3)
    time.sleep(2)

