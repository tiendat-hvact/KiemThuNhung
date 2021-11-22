import seleniumConfig
from src.sanPham import sanpham

def main():
    print("=======Main========")
    while(1):
        choose=input('Nhap chuong trinh: ')
        seleniumConfig.login(5)
        if(choose=='1'):
            print("1111")

main()

