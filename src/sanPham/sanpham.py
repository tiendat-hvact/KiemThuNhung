

def gotoSanPham(timeout):
    time.sleep(timeout)
    driver.get("https://banhang.upgo.vn/#/item/list")
    driver.find_elements_by_class_name("p-button-label")[0].click()
