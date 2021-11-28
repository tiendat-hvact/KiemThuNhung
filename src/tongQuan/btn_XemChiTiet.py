import help
import time
from help import check_btn_nextpage
def btn_XemChiTiet(driver):
    ''' 
         Kiểm tra nút xem chi tiết : Kỳ vọng là vào được trang ( https://banhang.upgo.vn/#/revenue ) 
    
    '''
    print("Thực hiện kiểm tra Nút xem chi tiết ")
    driver.get('https://banhang.upgo.vn/#/dashboard')
    time.sleep(1)
    data = {"page":"https://banhang.upgo.vn/#/dashboard","nextpage":"https://banhang.upgo.vn/#/revenue"}
    result = check_btn_nextpage.check_btn_class_name(driver,data,"btn-primary")
    if result:
        text = "BTN_XEMCHITIET" + "=== Yêu cầu bấm nút button Xem chi tiết ở === " +  data["page"] + " sẽ được chuyển đến  === " + data["nextpage"] + " ===  PASS"
        help.create_file_result("BTN_XEMCHITIET",text)
        return
    text ="BTN_XEMCHITIET" + "=== Yêu cầu bấm nút button Xem chi tiết ở === " +  data["page"] + " sẽ được chuyển đến  === " + data["nextpage"] + " ===  FAIL"
    help.create_file_result("BTN_XEMCHITIET",text)
    