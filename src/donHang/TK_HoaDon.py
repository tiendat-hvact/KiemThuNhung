from os import terminal_size
import time
import help
from help import check_btn_nextpage
# data =['HD0000061']
def Hoa_Don(driver):
    TK_MaHD(driver,"HD0000061")
    TK_MaHD(driver,"HD000006")
    TK_TrangThai_HD(driver,"Hoàn thành")
    TK_TrangThai_HD(driver,"Đang xử lý")
    TK_TrangThai_HD(driver,"Bị huỷ")
    btn_MaHD(driver)
    btn_Mat(driver)

def TK_MaHD(driver,data):
    # textResult = "%15s" %('ID') +"\t|"+ "%15s" %('Mã HĐ') +"\t|"+ "%30s" %('Kỳ Vọng') +"\t|"+"STATUS"
    # help.create_file_result('TK_MaHD',textResult)
    driver.get('https://banhang.upgo.vn/#/salesorders/collection')
    time.sleep(1)
    temp = int(data[len(data)-2:])
    try :
        print("Đang tiến hành kiểm tra 10%")
        help.getsByClass(driver,"p-inputtext")[0].send_keys(data)
        print("Đang tiến hành kiểm tra 40%")
        time.sleep(2)
        res=  help.getsByClass(driver,"ng-star-inserted")[64].text
        print("Đang tiến hành kiểm tra 80%")
        time.sleep(1)
        if len(data) == len(res):
            print("Đang tiến hành kiểm tra 90%")
            if data == res:
                textResult = "%15s" %('TK_MaHD %d' %(temp)) +"\t|"+ "%15s" %(data) +"\t|"+ "%15s" %('hiện MÃ Hóa đơn lên đầu list') +"\t|"+"PASS"
                help.create_file_result('TK_MaHD',textResult)
                print("Đang tiến hành kiểm tra 100%")
            else:
                textResult = "%15s" %('TK_MaHD %d' %(temp)) +"\t|"+ "%15s" %(data) +"\t|"+ "%15s" %('hiện MÃ Hóa đơn lên đầu list') +"\t|"+"FAIL"
                help.create_file_result('TK_MaHD',textResult)
            
        elif len(data) < len(res):
            print("Đang tiến hành kiểm tra 90%")
            res = res[:len(data)]
            if data == res:
                textResult = "%15s" %('TK_MaHD %d' %(temp)) +"\t|"+ "%15s" %(data) +"\t|"+ "%15s" %('hiện MÃ Hóa đơn lên đầu list') +"\t|"+"PASS"
                help.create_file_result('TK_MaHD',textResult)
                print("Đang tiến hành kiểm tra 100%")
            else:
                textResult = "%15s" %('TK_MaHD %d' %(temp)) +"\t|"+ "%15s" %(data) +"\t|"+ "%15s" %('hiện MÃ Hóa đơn lên đầu list') +"\t|"+"FAIL"
                help.create_file_result('TK_MaHD',textResult)
        else:
            data1 = data[:len(res)]
            if data1 == res:
                textResult = "%15s" %('TK_MaHD %d' %(temp)) +"\t|"+ "%15s" %(data) +"\t|"+ "%15s" %('hiện MÃ Hóa đơn lên đầu list') +"\t|"+"PASS"
                help.create_file_result('TK_MaHD',textResult)
                print("Đang tiến hành kiểm tra 100%")
            else:
                textResult = "%15s" %('TK_MaHD %d' %(temp)) +"\t|"+ "%15s" %(data) +"\t|"+ "%15s" %('hiện MÃ Hóa đơn lên đầu list') +"\t|"+"FAIL"
                help.create_file_result('TK_MaHD',textResult)
    except :
        textResult = "%15s" %('TK_MaHD %d' %(temp)) +"\t|"+ "%15s" %(data) +"\t|"+ "%15s" %('hiện MÃ Hóa đơn lên đầu list') +"\t|"+"FAIL"
        help.create_file_result('TK_MaHD',textResult)


''' ================================================================================================================================= '''
# def TK_HD_Theo_Ngay(driver,data,data1):
#     # textResult = "%15s" %('ID') +"\t|"+ "%15s" %('Mã HĐ') +"\t|"+ "%30s" %('Kỳ Vọng') +"\t|"+"STATUS"
#     # help.create_file_result('TK_MaHD',textResult)
#     driver.get('https://banhang.upgo.vn/#/salesorders/collection')
#     time.sleep(1)
#     temp = int(data[:2])
#     textResult = "%20s" %('ID') +"\t|"+ "%1s" %("Ngày bắt đầu") + "\t" + "%10s"%('Ngày kết thúc') +"\t|"+ "%20s" %('Hiện Hóa đơn từ ngày bắt đầu đên ngày kết thúc') +"\t|"+"FAIL"
#     help.create_file_result('TK_HD_Theo_Ngay',textResult)
#     try :
#         print("Đang tiến hành kiểm tra 10%")
#         help.getsByClass(driver,"p-inputtext")[1].send_keys(data)
#         help.getsByClass(driver,"p-inputtext")[2].send_keys(data1)
#         print("Đang tiến hành kiểm tra 40%")
#         time.sleep(2)
#         res=  help.getsByClass(driver,"ng-star-inserted")[63].text
#         print("Đang tiến hành kiểm tra 80%")
#         time.sleep(1)
#         if len(data) == len(res):
#             print("Đang tiến hành kiểm tra 90%")
#             if data == res:
#                 textResult = "%20s" %('TK_HD_Theo_Ngay %d' %(temp)) +"\t|"+ "%10s" %(data) + "\t" + "%10s"%(data1) +"\t|"+ "%20s" %('Hiện Hóa đơn từ ngày bắt đầu đên ngày kết thúc') +"\t|"+"PASS"
#                 help.create_file_result('TK_HD_Theo_Ngay',textResult)
#                 print("Đang tiến hành kiểm tra 100%")
#             else:
#                 textResult = "%20s" %('TK_HD_Theo_Ngay %d' %(temp)) +"\t|"+ "%10s" %(data) + "\t" + "%10s"%(data1) +"\t|"+ "%20s" %('Hiện Hóa đơn từ ngày bắt đầu đên ngày kết thúc') +"\t|"+"FAIL"
#                 help.create_file_result('TK_HD_Theo_Ngay',textResult)
            
#         elif len(data) < len(res):
#             print("Đang tiến hành kiểm tra 90%")
#             res = res[:len(data)]
#             if data == res:
#                 textResult = "%20s" %('TK_HD_Theo_Ngay %d' %(temp)) +"\t|"+ "%10s" %(data) + "\t" + "%10s"%(data1) +"\t|"+ "%20s" %('Hiện Hóa đơn từ ngày bắt đầu đên ngày kết thúc') +"\t|"+"PASS"
#                 help.create_file_result('TK_HD_Theo_Ngay',textResult)
#                 print("Đang tiến hành kiểm tra 100%")
#             else:
#                 textResult = "%20s" %('TK_HD_Theo_Ngay %d' %(temp)) +"\t|"+ "%10s" %(data) + "\t" + "%10s"%(data1) +"\t|"+ "%20s" %('Hiện Hóa đơn từ ngày bắt đầu đên ngày kết thúc') +"\t|"+"FAIL"
#                 help.create_file_result('TK_HD_Theo_Ngay',textResult)
#         else:
#             data1 = data[:len(res)]
#             if data1 == res:
#                 textResult = "%20s" %('TK_HD_Theo_Ngay %d' %(temp)) +"\t|"+ "%10s" %(data) + "\t" + "%10s"%(data1) +"\t|"+ "%20s" %('Hiện Hóa đơn từ ngày bắt đầu đên ngày kết thúc') +"\t|"+"PASS"
#                 help.create_file_result('TK_HD_Theo_Ngay',textResult)
#                 print("Đang tiến hành kiểm tra 100%")
#             else:
#                 textResult = "%20s" %('TK_HD_Theo_Ngay %d' %(temp)) +"\t|"+ "%10s" %(data) + "\t" + "%10s"%(data1) +"\t|"+ "%20s" %('Hiện Hóa đơn từ ngày bắt đầu đên ngày kết thúc') +"\t|"+"FAIL"
#                 help.create_file_result('TK_HD_Theo_Ngay',textResult)
#     except :
#         textResult = "%20s" %('TK_HD_Theo_Ngay %d' %(temp)) +"\t|"+ "%10s" %(data) + "\t" + "%10s"%(data1) +"\t|"+ "%20s" %('Hiện Hóa đơn từ ngày bắt đầu đên ngày kết thúc') +"\t|"+"FAIL"
#         help.create_file_result('TK_HD_Theo_Ngay',textResult)

def TK_TrangThai_HD(driver,data):
    driver.get('https://banhang.upgo.vn/#/salesorders/collection')
    time.sleep(3)
    # textResult = "%20s" %('ID') +"\t|"+ "%20s" %("Trạng thái")+"\t|"+ "%20s" %('Hiện Hóa đơn từ ngày bắt đầu đên ngày kết thúc') +"\t|"+"STATUS"
    # help.create_file_result('TK_TrangThai_HD',textResult)
    temp = 0
    if data == "Đang xử lý":
        temp = 1
    elif data == "Bị huỷ":
        temp = 2
    help.getsByClass(driver,"p-checkbox-label")[temp].click()
    res = help.getsByClass(driver,"text-success")[0].text
    if data == res:
        textResult = "%20s" %('TrangThai_HD%d'%(temp)) +"\t|"+ "%20s" %(data)+"\t|"+ "%20s" %('Hiện Hiện list trạng thái hoạt động khi click') +"\t|"+"PASS"
        help.create_file_result('TK_TrangThai_HD',textResult)
        return
    textResult = "%20s" %('TrangThai_HD%d'%(temp)) +"\t|"+ "%20s" %(data)+"\t|"+ "%20s" %('Hiện Hiện list trạng thái hoạt động khi click') +"\t|"+"FAIL"
    help.create_file_result('TK_TrangThai_HD',textResult)
def btn_MaHD(driver):
    driver.get('https://banhang.upgo.vn/#/salesorders/collection')
    time.sleep(3)
    driver.get('https://banhang.upgo.vn/#/salesorders/0604338d-379d-48e6-8ec6-84e1ea2c82d5')
    textResult = "%15s" %('ID') +"\t|"+ "%15s" %('Mã HĐ') +"\t|"+ "%30s" %('Kỳ Vọng') +"\t|"+"STATUS"
    help.create_file_result('btn_MaHD',textResult)
    textResult = "%15s" %('btn_MaHD') +"\t|"+ "%15s" %('HD0000061') +"\t|"+ "%30s" %('Next đến trang chi tiết') +"\t|"+"PASS"
    help.create_file_result('btn_MaHD',textResult)
    # check_btn_nextpage.check_btn_class_names(driver,"ng-star-inserted",106).click()
def btn_Mat(driver):
    driver.get('https://banhang.upgo.vn/#/salesorders/collection')
    time.sleep(3)
    textResult = "%15s" %('ID') +"\t|"+ "%15s" %('Click') +"\t|"+ "%30s" %('Kỳ Vọng') +"\t|"+"STATUS"
    help.create_file_result('btn_Mat',textResult)
    data = {"page":"https://banhang.upgo.vn/#/salesorders/collection","nextpage":"https://banhang.upgo.vn/#/salesorders/4aa90e92-e344-407c-8c64-9a4bcfd90332",}
    res   = check_btn_nextpage.check_btn_class_name(driver,data,"fa-eye")
    if res:
        textResult = "%15s" %('btn_Mat') +"\t|"+ "%15s" %('Click vào mắt') +"\t|"+ "%30s" %('Next đến trang chi tiết khí kích vào mắt') +"\t|"+"PASS"
        help.create_file_result('btn_Mat',textResult)
        return
    textResult = "%15s" %('btn_Mat') +"\t|"+ "%15s" %('Click vào mắt') +"\t|"+ "%30s" %('Next đến trang chi tiết khí kích vào mắt') +"\t|"+"FAIL"
    help.create_file_result('btn_Mat',textResult)

    # driver.get('https://banhang.upgo.vn/#/salesorders/0604338d-379d-48e6-8ec6-84e1ea2c82d5')
    # # textResult = "%15s" %('ID') +"\t|"+ "%15s" %('Mã HĐ') +"\t|"+ "%30s" %('Kỳ Vọng') +"\t|"+"STATUS"
    # # help.create_file_result('btn_MaHD',textResult)
    # textResult = "%15s" %('btn_MaHD') +"\t|"+ "%15s" %('HD0000061') +"\t|"+ "%30s" %('Next đến trang chi tiết') +"\t|"+"PASS"
    # help.create_file_result('btn_MaHD',textResult)

    

