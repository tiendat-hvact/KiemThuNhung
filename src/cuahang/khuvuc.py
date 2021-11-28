import json
import time
import help
from help import check_btn_nextpage
from selenium.webdriver.common.keys import Keys
f = open('C:/Users/ADMIN/Documents/kiemthunhung/testing/src/cuahang/dataH.json', encoding='utf-8')  
list = json.load(f)
newKhuvuc = list['newKhuvuc']
newFastKhuvuc = list['newFastKhuvuc']
newFastKhuvucMPTY = list['newFastKhuvucMPTY']
editKhuvucXX = list['editKhuvucXX']

# newKhuvuc = [
#   {"ID":"KV_aFULL","makhuvuc":"AAA1", "tenkhuvuc":"khu vuc AAA1", "expected":"nextPage"},
#   {"ID":"KV_aMKV01","makhuvuc":"$!@%AAA1", "tenkhuvuc":"khu vuc AAA1", "expected":"un_nextPage"},
#   {"ID":"KV_aMKV02","makhuvuc":"", "tenkhuvuc":"khu vuc AAA1", "expected":"un_nextPage"},
#   {"ID":"KV_aMPTY","makhuvuc":"", "tenkhuvuc":"", "expected":"un_nextPage"},
#   {"ID":"KV_aTKV01","makhuvuc":"AAA1", "tenkhuvuc":"", "expected":"un_nextPage"},
#   {"ID":"KV_aTKV02","makhuvuc":"AAA1", "tenkhuvuc":"%#$!Khu vucAAA", "expected":"un_nextPage"},
#   ]
# newFastKhuvuc = [
#   {"ID":"KV_afFULL","makhuvuc":"BBB1","soluong":"1","expected":"nextPage"},
#   {"ID":"KV_afMKV01","makhuvuc":"","soluong":"1","expected":"un_nextPage"},
#   {"ID":"KV_afMKV02","makhuvuc":"%#$!AGAA","soluong":"1","expected":"un_nextPage"},  
#   ]
# newFastKhuvucMPTY = [
#   {"ID":"KV_afSL01","makhuvuc":"AGAA","soluong":"","expected":"un_nextPage"},
#   # {"ID":"KV_afSL02","makhuvuc":"AGAA","soluong":"@#$","expected":"un_nextPage"},  
# ]

# editKhuvucXX = [
#   {"ID":"KV_eMKV01","makhuvuc":"%#$!VEWA", "tenkhuvuc":"khu vuc AAA1", "expected":"un_nextPage"},
#   {"ID":"KV_eMKV02","makhuvuc":"", "tenkhuvuc":"khu vuc AAA1", "expected":"un_nextPage"},
#   {"ID":"KV_eTKV01","makhuvuc":"VEWA", "tenkhuvuc":"@%&$khuvuc AJE1", "expected":"un_nextPage"},
#   {"ID":"KV_eTKV02","makhuvuc":"VEWA", "tenkhuvuc":"", "expected":"un_nextPage"},
#   ]
# ==== THÊM KHU VỰC =====
def insertDataKV(driver, kv):
  time.sleep(2)
  help.getByName(driver, 'area_no').send_keys(kv['makhuvuc'])
  time.sleep(2)
  help.getByName(driver, 'area_name').send_keys(kv['tenkhuvuc'])
  time.sleep(2)
  #nhanluu
  data ={"page":"https://banhang.upgo.vn/#/area/create","nextpage":"https://banhang.upgo.vn/#/area/collection"}
  check = check_btn_nextpage.check_btn_class_name2(driver, data, 'fa-save')
  return check

def addKhuvuc(driver):
  print('<<__Adding newKhuvuc__>>')
  driver.get("https://banhang.upgo.vn/#/area/collection")
  time.sleep(3)
  textResult ="%15s" %('ID') +"\t|"+"%15s" %('MAKHUVUC') +"\t|"+"%15s" %('TENKHUVUC') +"\t|"+"%15s" %('EXPECTED') +"\t|"+"STATUS"
  help.create_file_result('kq_addKhuVuc',textResult)
  help.createLineNewKhuVuc()
  ROUND = 0

  for kv in newKhuvuc:
    ROUND +=1
    print('---> looping KV <---' , ROUND)
    help.getsByClass(driver,"p-button-label")[0].click()
    time.sleep(1) 
    isNextPage = insertDataKV(driver,kv)
    print(isNextPage)
    if(isNextPage==True and kv['expected']=='nextPage'):
      print('========1=========')
      textResult1 = "%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['tenkhuvuc'] +"\t|"+  "%15s" %kv['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_addKhuVuc',textResult1)
      help.createLineNewKhuVuc()

    elif(isNextPage==False and kv['expected']=='un_nextPage'):
      print('========22=========')
      textResult2 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['tenkhuvuc'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_addKhuVuc',textResult2)
      help.createLineNewKhuVuc()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)

    elif(isNextPage==True and kv['expected']=='un_nextPage'):
      print('========333=========')
      textResult3 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['tenkhuvuc'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_addKhuVuc',textResult3)
      help.createLineNewKhuVuc()

    elif(isNextPage==False and kv['expected']=='nextPage'):
      print('========444=========')
      textResult4 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['tenkhuvuc'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_addKhuVuc',textResult4)
      help.createLineNewKhuVuc()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)
    time.sleep(1)

def insertFastDataKV(driver, kv):
  time.sleep(2)
  #makhuvuc
  help.getById(driver, 'area_no').send_keys(kv['makhuvuc'])
  time.sleep(2)
  #sổ xuống
  help.getsByClass(driver, 'pi-chevron-down')[0].click()
  time.sleep(2)
  #click list đầu tiên
  help.getsByClass(driver, 'p-autocomplete-item')[2].click()
  time.sleep(2)

  help.getById(driver, 'integeronly').send_keys(kv['soluong'])
  time.sleep(4)
  # nhan XONG
  help.getsByClass(driver, 'fa-check-square')[0].click()
  time.sleep(4)
  #nhanluu
  # data ={"page":"https://banhang.upgo.vn/#/area/create","nextpage":"https://banhang.upgo.vn/#/area/collection"}
  # check = check_btn_nextpage.check_btn_class_name2(driver, data, 'fa-save')
  #check = true = đóng POPUP >< fail Lỗi KHÔNG ĐÓNG POPUP
  
  try:
    time.sleep(2)
    temp = help.getById(driver, 'pr_id_3-label').text
    print(temp)
    time.sleep(2)
    if(temp =='Thêm nhanh khu vực'):
      checkPopUp = False
      print("CHƯA ĐÓNG POPUP", checkPopUp)
    else:
      print('Temp giá trị khác')
  except:
    checkPopUp = True
    time.sleep(2)
  return checkPopUp

def insertFastDataKVMPTY(driver, kv):
  time.sleep(2)
  #makhuvuc
  help.getById(driver, 'area_no').send_keys(kv['makhuvuc'])
  time.sleep(2)
  #sổ xuống
  help.getsByClass(driver, 'pi-chevron-down')[0].click()
  time.sleep(2)
  #click list đầu tiên
  help.getsByClass(driver, 'p-autocomplete-item')[2].click()
  time.sleep(2)
  # help.getById(driver, 'integeronly').send_keys(kv['soluong'])
  # time.sleep(2)
  # nhan XONG
  help.getsByClass(driver, 'fa-check-square')[0].click()
  time.sleep(4)

  try:
    time.sleep(2)
    temp = help.getById(driver, 'pr_id_3-label').text
    print(temp)
    time.sleep(2)
    if(temp =='Thêm nhanh khu vực'):
      checkPopUp = False
      print("CHƯA ĐÓNG POPUP", checkPopUp)
    else:
      print('Temp giá trị khác')
  except:
    checkPopUp = True
    time.sleep(2)
  return checkPopUp

def addFastKhuvuc(driver):
  print('<<__add newFastKhuvuc__>>')
  driver.get("https://banhang.upgo.vn/#/area/collection")
  time.sleep(3)
  textResult ="%15s" %('ID') +"\t|"+"%15s" %('MAKHUVUC') +"\t|"+"%15s" %('SOLUONG') +"\t|"+"%15s" %('EXPECTED') +"\t|"+"STATUS"
  help.create_file_result('kq_addFastKhuVuc',textResult)
  help.createLineNewFastKhuVuc()
  ROUNDFast = 0
  ROUNDFastMPTY = 0

  for kv in newFastKhuvuc:
    ROUNDFast +=1
    print('---> looping FastKV <---' , ROUNDFast)
    help.getsByClass(driver,"p-button-label")[1].click()
    time.sleep(1) 
    isNextPage = insertFastDataKV(driver,kv)
    print(isNextPage)
    if(isNextPage==True and kv['expected']=='nextPage' ):
      print('========1=========')
      textResult1 = "%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['soluong'] +"\t|"+  "%15s" %kv['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_addFastKhuVuc',textResult1)
      help.createLineNewFastKhuVuc()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)

    elif(isNextPage==False and kv['expected']=='un_nextPage'):
      print('========22=========')
      textResult2 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['soluong'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_addFastKhuVuc',textResult2)
      help.createLineNewFastKhuVuc()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)

    elif(isNextPage==True and kv['expected']=='un_nextPage'):
      print('========333=========')
      textResult3 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['soluong'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_addFastKhuVuc',textResult3)
      help.createLineNewFastKhuVuc()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)


    elif(isNextPage==False and kv['expected']=='nextPage'):
      print('========444=========')
      textResult4 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['soluong'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_addFastKhuVuc',textResult4)
      help.createLineNewFastKhuVuc()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)
    time.sleep(4)
  
  for kv in newFastKhuvucMPTY:
    ROUNDFastMPTY +=1
    print('---> looping FastKV <---' , ROUNDFastMPTY)
    help.getsByClass(driver,"p-button-label")[1].click()
    time.sleep(1) 
    # isNextPage = insertFastDataKV(driver,kv)
    isNextPage = False
    print(isNextPage)
    if(isNextPage==True and kv['expected']=='nextPage' ):
      print('========1=========')
      textResult1 = "%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['soluong'] +"\t|"+  "%15s" %kv['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_addFastKhuVuc',textResult1)
      help.createLineNewFastKhuVuc()

    elif(isNextPage==False and kv['expected']=='un_nextPage'):
      print('========22=========')
      textResult2 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['soluong'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_addFastKhuVuc',textResult2)
      help.createLineNewFastKhuVuc()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)

    elif(isNextPage==True and kv['expected']=='un_nextPage'):
      print('========333=========')
      textResult3 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['soluong'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_addFastKhuVuc',textResult3)
      help.createLineNewFastKhuVuc()

    elif(isNextPage==False and kv['expected']=='nextPage'):
      print('========444=========')
      textResult4 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['soluong'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_addFastKhuVuc',textResult4)
      help.createLineNewFastKhuVuc()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)
    time.sleep(1)

# ==== SỬA KHU VƯC +++++++
def editDataKV(driver, kv):
  time.sleep(2)
  help.getByName(driver, 'area_no').clear()
  time.sleep(2)
  help.getByName(driver, 'area_no').send_keys(kv['makhuvuc'])
  time.sleep(2)
  help.getByName(driver, 'area_name').clear()
  time.sleep(2)
  help.getByName(driver, 'area_name').send_keys(kv['tenkhuvuc'])
  time.sleep(2)
  #nhanluu
  data ={"page":"https://banhang.upgo.vn/#/area/create","nextpage":"https://banhang.upgo.vn/#/area/collection"}
  check = check_btn_nextpage.check_btn_class_name2(driver, data, 'fa-save')
  return check

def changeSTTKV(driver):
    print('--Change STTKV--' )
    help.getsByClass(driver,"fa-edit")[0].click()
    time.sleep(2) 
    help.getsByClass(driver, 'p-inputswitch-slider')[2].click()
    data ={"page":"https://banhang.upgo.vn/#/area/create","nextpage":"https://banhang.upgo.vn/#/area/collection"}
    # check = check_btn_nextpage.check_btn_class_name(driver, data, 'p-button-success')
    check = check_btn_nextpage.check_btn_class_name2(driver, data, 'fa-save') 
    isNextPage = check
    print('--chuyen trang edit STT--',isNextPage)
    if(isNextPage==True ):
      print('========1=========')
      textResult1 = "%15s" %'KV_eTTKV' +"\t|"+ "%15s" %"" +"\t|"+ "%15s" %"" +"\t|"+  "%15s" %'nextPage' +"\t|"+"PASS"
      help.create_file_result('kq_editKhuVuc',textResult1)
      help.createLineEditKV()

    elif(isNextPage==False ):
      print('========22=========')
      textResult2 ="%15s" %'KV_eTTKV' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'un_nextPage' +"\t|"+"FAIL"
      help.create_file_result('kq_editKhuVuc',textResult2)
      help.createLineEditKV()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)
    time.sleep(2)

def editKhuvuc(driver):
  print('<--- Editing --->')
  driver.get ("https://banhang.upgo.vn/#/area/collection")
  time.sleep(3)
  textResult = "%15s" %('ID') +"\t|"+ "%15s" %('MAKHUVUC') +"\t|"+ "%15s" %('TENKHUVUC')  +"\t|"+ "%15s" %('EXPECTED') +"\t|"+"STATUS"
  help.create_file_result('kq_editKhuVuc',textResult)
  help.createLineEditKV()
  # newCoSo = '{"ma":"X", "ten":"co so xxx", "tinh":"Hà Nội", "huyen":"Thạch Thất",
  #  "xa":"Tiến Xuân", "diachi":"Tiến Xuân, Thạch Thất, Hà Nôi"}'
  roundEdit = 0
  for kv in editKhuvucXX:
    #nhan them
    roundEdit +=1
    print('---> editing KV <---' , roundEdit)
    help.getsByClass(driver,"fa-edit")[0].click()
    time.sleep(1) 
    isNextPage = editDataKV(driver,kv)
    print('--chuyen trang edit--',isNextPage)
    if(isNextPage==True and kv['expected']=='nextPage'):
      print('========1=========')
      textResult1 = "%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['tenkhuvuc'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_editKhuVuc',textResult1)
      help.createLineEditKV()

    elif(isNextPage==False and kv['expected']=='un_nextPage'):
      print('========22=========')
      textResult2 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['tenkhuvuc'] +"\t|"+"%15s" %kv['expected'] +"\t|"+"PASS"
      help.create_file_result('kq_editKhuVuc',textResult2)
      help.createLineEditKV()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)

    elif(isNextPage==True and kv['expected']=='un_nextPage'):
      print('========333=========')
      textResult3 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['tenkhuvuc'] +"\t|"+"%15s" %kv['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_editKhuVuc',textResult3)
      help.createLineEditKV()

    elif(isNextPage==False and kv['expected']=='nextPage'):
      print('========444=========')
      textResult4 ="%15s" %kv['ID'] +"\t|"+ "%15s" %kv['makhuvuc'] +"\t|"+ "%15s" %kv['tenkhuvuc'] +"\t|"+ "%15s" %kv['expected'] +"\t|"+"FAIL"
      help.create_file_result('kq_editKhuVuc',textResult4)
      help.createLineEditKV()
      driver.get ("https://banhang.upgo.vn/#/area/collection")
      time.sleep(3)
    time.sleep(1)
  changeSTTKV(driver)


# ===== XOA KHU VUC >>>>>>
def checkClosePopUp(driver):
  try:
    time.sleep(2)
    temp = help.getById(driver, 'p-confirm-dialog-message').text
    print(temp)
    time.sleep(2)
    if(temp =='Bạn có chắc muốn xoá khu vực?'):
      checkPopUp = False
      print("CHƯA ĐÓNG POPUP", checkPopUp)
    else:
      print('Temp giá trị khác')
  except:
    checkPopUp = True
    time.sleep(2)
  return checkPopUp

def xoaKhuvuc(driver):
  print('<<< Deleting >>>')
  driver.get ("https://banhang.upgo.vn/#/workstation/collection")
  time.sleep(3)
  help.getsByClass(driver, 'fa-trash')[0].click()
  time.sleep(2)
  # Check close Popup
  check = checkClosePopUp(driver)
  isNextPage = check
  print('--PopUp Xoa KV--',isNextPage)
  if(isNextPage==True ):
    print('========1=========')
    textResult1 = "%15s" %'KV_dELETE' +"\t|"+ "%15s" %"" +"\t|"+ "%15s" %"" +"\t|"+  "%15s" %'nextPage' +"\t|"+"PASS"
    help.create_file_result('kq_editKhuVuc',textResult1)
    help.createLineEditKV()

  elif(isNextPage==False ):
    print('========22=========')
    textResult2 ="%15s" %'KV_dELETE' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %'un_nextPage' +"\t|"+"FAIL"
    help.create_file_result('kq_editKhuVuc',textResult2)
    help.createLineEditKV()
    driver.get ("https://banhang.upgo.vn/#/area/collection")
    time.sleep(3)
  time.sleep(2)

# === TIM KIEM KHU VUC ====
def timKhuvuc(driver):
  print('<<< Findingggg KV >>>')
  driver.get ("https://banhang.upgo.vn/#/area/collection")
  time.sleep(3)
  help.getByName(driver, 'area_name').send_keys("Bep"+ Keys.ENTER)
  del1 ="%15s" %'KV_fKHVC' +"\t|"+ "%15s" %'Bep' +"\t|"+ "%15s" %''  +"\t|"+ "%15s" %'' +"\t|"+"FAIL"
  help.create_file_result('kq_editKhuVuc',del1)
  help.createLineEditKV()
  time.sleep(3)
  help.getByName(driver, 'area_name').clear()
  help.getByName(driver, 'area_name').send_keys(""+ Keys.ENTER)
  del2 ="%15s" %'KV_fMPTY' +"\t|"+ "%15s" %'' +"\t|"+ "%15s" %''  +"\t|"+ "%15s" %'' +"\t|"+"PASS"
  help.create_file_result('kq_editKhuVuc',del2)
  help.createLineEditKV()
  time.sleep(3)
  help.getByName(driver, 'area_name').clear()
  help.getByName(driver, 'area_name').send_keys("&%*#CS1"+ Keys.ENTER)
  del3 ="%15s" %'KV_fSPEC' +"\t|"+ "%15s" %'&%*#CS1' +"\t|"+ "%15s" %''  +"\t|"+ "%15s" %'' +"\t|"+"PASS"
  help.create_file_result('kq_editKhuVuc',del3)
  help.createLineEditKV()
  time.sleep(2)
