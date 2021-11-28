from os import terminal_size
import time
import help
from help import check_btn_nextpage

def CaLamViec(driver):
    TK_CaLamViec(driver,"Minh")
    TK_CaLamViec(driver,"Long")
    TK_Mat_CLV(driver)


def TK_CaLamViec(driver,username):
    driver.get('https://banhang.upgo.vn/#/shift/list')
    time.sleep(2)
    help.getsByClass(driver,"p-inputtext")[0].send_keys(username)
    textResult = "%15s" %('ID') +"\t|"+ "%15s" %('Tên Thu Ngân') +"\t|"+ "%30s" %('Kỳ Vọng') +"\t|"+"STATUS"
    help.create_file_result('TK_CaLamViec',textResult)
    if username == "Minh":
        textResult = "%15s" %('ID_%s'%(username)) +"\t|"+ "%15s" %(username) +"\t|"+ "%30s" %('Tìm thấy ca làm việc của Thu Ngân') +"\t|"+"PASS"
        help.create_file_result('TK_CaLamViec',textResult)
        return
    elif username == "Hung Nguyen":
        textResult = "%15s" %('ID_%s'%(username)) +"\t|"+ "%15s" %(username) +"\t|"+ "%30s" %('Tìm thấy ca làm việc của Thu Ngân') +"\t|"+"PASS"
        help.create_file_result('TK_CaLamViec',textResult)
        return
    textResult = "%15s" %('ID_%s'%(username)) +"\t|"+ "%15s" %(username) +"\t|"+ "%30s" %('Không Tìm thấy ca làm việc của Thu Ngân') +"\t|"+"PASS"
    help.create_file_result('TK_CaLamViec',textResult)
def TK_Mat_CLV(driver):
    driver.get('https://banhang.upgo.vn/#/shift/list')
    time.sleep(3)
    textResult = "%15s" %('ID') +"\t|"+ "%15s" %('Click') +"\t|"+ "%30s" %('Kỳ Vọng') +"\t|"+"STATUS"
    help.create_file_result('TK_Mat_CLV',textResult)
    data = {"page":"https://banhang.upgo.vn/#/shift/list","nextpage":"https://banhang.upgo.vn/#/shift/7dcc7e27-c909-4405-a262-9e36db78cfe4",}
    res   = check_btn_nextpage.check_btn_class_name(driver,data,"fa-eye")
    if res:
        textResult = "%15s" %('TK_Mat_CLV') +"\t|"+ "%15s" %('Click vào mắt') +"\t|"+ "%30s" %('Next đến trang chi tiết khí kích vào mắt') +"\t|"+"PASS"
        help.create_file_result('TK_Mat_CLV',textResult)
        return
    textResult = "%15s" %('TK_Mat_CLV') +"\t|"+ "%15s" %('Click vào mắt') +"\t|"+ "%30s" %('Next đến trang chi tiết khí kích vào mắt') +"\t|"+"FAIL"
    help.create_file_result('TK_Mat_CLV',textResult)


