import time
import seleniumConfig
from src.sanPham import sanpham, nhomsp
from src.tongQuan import btn_XemChiTiet,btn_XemMXH
from src.donHang import TK_HoaDon
from src.CaLamViec import calamviec
from src.cuahang import cuahang

def main():
    print("=======Main========")
    driver = seleniumConfig.login(5)
    time.sleep(1)
    print(driver)
    ''' Tổng quan '''
    btn_XemChiTiet.btn_XemChiTiet(driver)
    # time.sleep(2)
    # btn_XemMXH.btn_XemMXH(driver)
    ''' Đơn Hàng '''
    TK_HoaDon.Hoa_Don(driver)
    ''' Ca làm việc '''
    calamviec.CaLamViec(driver)
    ''' Sản phẩm '''
    sanpham.add(driver)
    ''' Nhóm sản phẩm '''
    nhomsp.add(driver)
    ''' Cửa hàng'''
    cuahang.cuahang(driver)




if __name__ == "__main__":
    main()

