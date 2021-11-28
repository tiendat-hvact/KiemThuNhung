from src.cuahang import coso
from src.cuahang import khuvuc
def cuahang(driver):
        coso.addCoSo(driver)
        coso.editCoSo(driver)
        coso.xoaCoso(driver)
        coso.timCoso(driver)
        # test.testFC(driver)
        # test.testJson(driver)
        khuvuc.addKhuvuc(driver)
        khuvuc.addFastKhuvuc(driver)
        khuvuc.editKhuvuc(driver)
        khuvuc.xoaKhuvuc(driver)
        khuvuc.timKhuvuc(driver)