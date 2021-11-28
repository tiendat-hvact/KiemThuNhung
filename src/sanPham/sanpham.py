import time
import json
import help
from help import check_btn_nextpage
f = open('C:/Users/ADMIN/Documents/kiemthunhung/testing/src/sanPham/data.json', encoding='utf-8')
list = json.load(f)
list = list['sanpham']

def add(driver):
    print('========= Đang Thêm sản phẩm=============')
    driver.get ("https://banhang.upgo.vn/#/item/list")
    time.sleep(3)
    text="\n\n========================================THÊM SẢN PHẨN ===================================================\n\n"
    help.create_file_result('sanpham',text)
    text =("%12s" %('MÃ PHÂN NHÓM') +'\t┊'+
    "%15s" %('TÊN PHÂN NHÓM') +'\t┊'+ 
    "%12s" %('L.THỰC ĐƠN') +'\t┊'+
    "%12s" %('NHÀ HÀNG') +'\t┊'+
    "%12s" %('Đ.VỊ TÍNH') +'\t┊'+
    "%12s" %('IN.CB') +'\t┊'+
    "%12s" %('TRENDING') +'\t┊'+
    "%12s" %('MANG ĐI') +'\t┊'+
    "%12s" %('LOẠI') +'\t┊'+
    "%12s" %('BẢNG GIÁ') +'\t┊'+
    "%12s" %('GIÁ BÁN') +'\t┊'+
    "%12s" %('KỲ VỌNG') +'\t┊'+
    "\tKẾT QUẢ")
    help.create_file_result('sanpham',text)
    help.createLine()
    for sp in list:
        # nhấn thêm
        help.getByClass(driver,"p-button-label").click()
        isNextPage = enterData(driver,sp)
        time.sleep(1)   
        if(isNextPage==True and sp['ky_vong']=='next_page'):
            dataText(sp, "PASS")
        elif(isNextPage==False and sp['ky_vong']=='un_next_page'):
            dataText(sp, "PASS")
            driver.get ("https://banhang.upgo.vn/#/item/list")
            time.sleep(3)
        elif(isNextPage==True and sp['ky_vong']=='un_next_page'):
            dataText(sp, "FAIL")
        elif(isNextPage==False and sp['ky_vong']=='next_page'):
            dataText(sp, "FAIL")
            driver.get ("https://banhang.upgo.vn/#/item/list")
            time.sleep(3)

        time.sleep(1)

# nhập dữ liệu vào các ô input trong phần thêm sản phẩm
def enterData(driver,sp):
    
    # value
    help.inputById(driver, 'item_no', sp['masp'])
    help.inputById(driver, 'item_name', sp['tensp'] )

    # select
    if(sp['loai_thuc_don']=='select'):
        time.sleep(2)
        help.getsByClass(driver,'p-dropdown-trigger')[0].click()
        time.sleep(3)
        help.getsByClass(driver,'p-dropdown-item')[1].click()

    if(sp['nhom_hang']=='select'):
        time.sleep(2)
        help.getsByClass(driver, 'p-autocomplete-dropdown')[0].click()
        time.sleep(2)
        help.getByClass(driver, 'p-autocomplete-item').click()

    if(sp['don_vi_tinh']=='select'):
        time.sleep(2)
        help.getsByClass(driver, 'p-autocomplete-dropdown')[1].click()
        time.sleep(2)
        help.getByClass(driver, 'p-autocomplete-item').click()

    if(sp['in_che_bien']=='select'):
        time.sleep(2)
        help.getsByClass(driver, 'p-autocomplete-dropdown')[2].click()
        time.sleep(2)
        help.getByClass(driver, 'p-autocomplete-item').click()
    

    # check box
    if(sp['trending']=='check'):
        help.getsByClass(driver,'p-checkbox-box')[0].click()

    if(sp['ban_mang_di']=='check'):
        help.getsByClass(driver,'p-checkbox-box')[1].click()
   
    if(sp['loaisp']=='check'):
        help.getsByClass(driver,'p-checkbox-box')[6].click()

    # select
    if(sp['bang_gia']=='select'):
        help.getsByClass(driver,'p-dropdown-trigger')[1].click()
        time.sleep(1)
        help.getsByClass(driver,'p-dropdown-item')[1].click()

    # value
    if(sp['gia']!='0'):
        help.getByClass(driver, 'p-inputnumber-input').send_keys(sp['gia'])

       # nhấn lưu
    data ={"page":"https://banhang.upgo.vn/#/item/create","nextpage":"https://banhang.upgo.vn/#/item/list"}
    check = check_btn_nextpage.check_btn_class_name(driver, data, 'p-button-success')
    return check

def dataText(sp, status):
    text =("%12s" %(sp['masp'])+'\t┊'+
    "%15s" %(sp['tensp'])+'\t┊'+ 
    "%12s" %(sp['loai_thuc_don'])+'\t┊'+
    "%12s" %(sp['nhom_hang']) +'\t┊'+
    "%12s" %(sp['don_vi_tinh']) +'\t┊'+
    "%12s" %(sp['in_che_bien']) +'\t┊'+
    "%12s" %(sp['trending']) +'\t┊'+ 
    "%12s" %(sp['ban_mang_di']) +'\t┊'+ 
    "%12s" %(sp['loaisp']) +'\t┊'+ 
    "%12s" %(sp['bang_gia']) +'\t┊'+ 
    "%12s" %(sp['gia'])+ '\t┊'+ 
    "%12s" %(sp['ky_vong'])+ '\t┊'+ 
    "%12s" %(status) )
    help.create_file_result('sanpham',text)
    help.createLine()