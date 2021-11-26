import time
import json
import help
from help import check_btn_nextpage
f = open('D:/Nam4 BY Me/testing/auto test/src/sanPham/data.json', encoding='utf-8')
list = json.load(f)
list = list['nhom_sp']

def add(driver):
    print('========= Đang thêm SP =============')

    help.create_file_result('sanpham',"\n=========================== THÊM NHÓM SẢN PHẨM=====================\n")
    driver.get ("https://banhang.upgo.vn/#/category/707416b3-2fc2-477f-aa52-f30c14684d86")

    driver.get ("https://banhang.upgo.vn/#/category/collection")
    time.sleep(3)
    text ="%15s" %('MÃ TESTCASE') +'\t┊'+ "%15s" %('MÃ PHÂN NHÓM')+'\t┊'+ "%15s" %('TÊN PHÂN NHÓM') +'\t┊'+ "%15s" %('THỨ TỰ') +'\t┊'+ "%15s" %('KỲ VỌNG') +'\t┊'+"%12s" %('KẾT QUẢ') 
    help.create_file_result('sanpham',text)
    help.createLine()
    for sp in list:
        # nhấn thêm
        help.getByClass(driver,"p-button-label").click()
        time.sleep(1)   
        isNextPage = enterData(driver,sp)
        if(isNextPage==True and sp['ky_vong']=='next_page'):
            dataText(sp, "PASS")
        elif(isNextPage==False and sp['ky_vong']=='un_next_page'):
            dataText(sp, "PASS")
            driver.get ("https://banhang.upgo.vn/#/category/collection")
            time.sleep(3)
        elif(isNextPage==True and sp['ky_vong']=='un_next_page'):
            dataText(sp, "FAIL")
        elif(isNextPage==False and sp['ky_vong']=='next_page'):
            dataText(sp, "FAIL")
            driver.get ("https://banhang.upgo.vn/#/category/collection")
            time.sleep(3)

        time.sleep(1)
        # help.create_file_result('kq_themsp',sp['name'])

# nhập dữ liệu vào các ô input 
def enterData(driver,sp):
    help.getByName(driver, 'category_no').send_keys(sp['ma_phan_nhom'])
    help.getByName(driver, 'category_name').send_keys(sp['ten_phan_nhom'])
    help.getByName(driver, 'sort_number').send_keys(sp['thu_tu'])
    # nhấn lưu
    data ={"page":"https://banhang.upgo.vn/#/category/create","nextpage":"https://banhang.upgo.vn/#/category/collection"}
    check = check_btn_nextpage.check_btn_class_name(driver, data, 'p-button-success')
    return check

def dataText(sp, status):
    text =(
    "%15s" %(sp['matc']) +'\t┊'+
    "%15s" %(sp['ma_phan_nhom']) +'\t┊'+
    "%15s" %(sp['ten_phan_nhom']) +'\t┊'+
    "%15s" %(sp['thu_tu']) +'\t┊'+
    "%15s" %(sp['ky_vong']) +'\t┊'+
    "%12s" %(status) )
    help.create_file_result('sanpham',text)
    help.createLine()