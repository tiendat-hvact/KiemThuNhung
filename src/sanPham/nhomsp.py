import time
import help
from help import check_btn_nextpage
list = [
    {
        "ma_phan_nhom": 'pn1',
        "ten_phan_nhom": 'phan nhom 1',
        "thu_tu": '',
        "ky_vong": 'next_page'
    },
  
    {
        "ma_phan_nhom": '',
        "ten_phan_nhom": '',
        "thu_tu": '',
        "ky_vong": 'un_next_page'
    },
  
    {
        "ma_phan_nhom": '',
        "ten_phan_nhom": 'phân nhóm 3',
        "thu_tu": '3',
        "ky_vong": 'un_next_page'
    },
    
    {
        "ma_phan_nhom": 'pn4',
        "ten_phan_nhom": '',
        "thu_tu": '4',
        "ky_vong": 'un_next_page'
    },
    
    {
        "ma_phan_nhom": '%$#@!$@!$@#$',
        "ten_phan_nhom": 'phan nhom 5',
        "thu_tu": '',
        "ky_vong": 'un_next_page'
    },
    
    {
        "ma_phan_nhom": 'pn6',
        "ten_phan_nhom": '%$#@!$@!$@#$',
        "thu_tu": '',
        "ky_vong": 'un_next_page'
    },
    
    {
        "ma_phan_nhom": 'pn7',
        "ten_phan_nhom": 'phan nhom 7',
        "thu_tu": '-1',
        "ky_vong": 'un_next_page'
    },

]

def add(driver):
   
    print('========= Đang thêm SP =============')
    driver.get ("https://banhang.upgo.vn/#/category/collection")
    time.sleep(3)
    text ="%15s" %('MÃ PHÂN NHÓM') +'\t|'+ "%15s" %('TÊN PHÂN NHÓM') +'\t|'+ "%15s" %('THỨ TỰ') +'\t|'+"PASS"
    help.create_file_result('kq_nhom_sp',text)
    help.createLine()
    for sp in list:
        # nhấn thêm
        help.getByClass(driver,"p-button-label").click()
        time.sleep(1)   
        isNextPage = enterData(driver,sp)
        if(isNextPage==True and sp['ky_vong']=='next_page'):
            text ="%15s" %(sp['ma_phan_nhom']) +'\t|'+ "%15s" %(sp['ten_phan_nhom']) +'\t|'+ "%15s" %(sp['thu_tu']) +'\t|'+"PASS"
            help.create_file_result('kq_nhom_sp',text)
            help.createLine()
        elif(isNextPage==False and sp['ky_vong']=='un_next_page'):
            text ="%15s" %(sp['ma_phan_nhom']) +'\t|'+ "%15s" %(sp['ten_phan_nhom']) +'\t|'+ "%15s" %(sp['thu_tu']) +'\t|'+"PASS"
            help.create_file_result('kq_nhom_sp',text)
            help.createLine()
            driver.get ("https://banhang.upgo.vn/#/category/collection")
            time.sleep(3)
        elif(isNextPage==True and sp['ky_vong']=='un_next_page'):
            text ="%15s" %(sp['ma_phan_nhom']) +'\t|'+ "%15s" %(sp['ten_phan_nhom']) +'\t|'+ "%15s" %(sp['thu_tu']) +'\t|'+"FAIL"
            help.create_file_result('kq_nhom_sp',text)
            help.createLine()
        elif(isNextPage==False and sp['ky_vong']=='next_page'):
            text ="%15s" %(sp['ma_phan_nhom']) +'\t|'+ "%15s" %(sp['ten_phan_nhom']) +'\t|'+ "%15s" %(sp['thu_tu']) +'\t|'+"FAIL"
            help.create_file_result('kq_nhom_sp',text)
            help.createLine()
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