import help
import time
from help import check_btn_nextpage
def btn_XemMXH(driver):
    ''' 
         Kiểm tra nút Xem tất cả : Kỳ vọng là vào được trang ( https://banhang.upgo.vn/#/settings ) 
    
    '''
    print("Thực hiện kiểm tra Nút Xem tất cả ")
    driver.get('https://banhang.upgo.vn/#/dashboard')
    time.sleep(2)
    data = {"page":"https://banhang.upgo.vn/#/dashboard","nextpage":"https://banhang.upgo.vn/#/settings"}
    result = check_btn_nextpage.check_btn_class_names(driver,data,"btn-primary",1)
    print(result)
    if result:
        # textResult = "%15s" %('ID') +"\t|"+ "%15s" %('MACOSO') +"\t|"+ "%15s" %('TENCOSO') +"\t|"+ "%15s" %('SDTCOSO')  +"\t|"+ "%15s" %('EXPECTED') +"\t|"+"STATUS"
        text = "btn_XemMXH" + "=== Yêu cầu bấm nút button Xem tất cả ở === " +  data["page"] + " sẽ được chuyển đến  === " + data["nextpage"] + " ===  PASS"
        help.create_file_result("btn_XemMXH",text)
    else:
        text ="btn_XemMXH" + "=== Yêu cầu bấm nút button Xem tất cả ở === " +  data["page"] + " sẽ được chuyển đến  === " + data["nextpage"] + " ===  FAIL"
        help.create_file_result("btn_XemMXH",text)
    