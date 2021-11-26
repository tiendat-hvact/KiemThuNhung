import seleniumConfig
from src.sanPham import sanpham, nhomsp

def main():
    print("=======Main========")
    # while(1):
        # choose=input('Nhap chuong trinh: ')
        # if(choose=='1'):
    driver= seleniumConfig.login(5)
    sanpham.add(driver)
    nhomsp.add(driver)

main()

