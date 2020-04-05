# Import module
import math

i = 3.6
j = 3.4
print("Lam tron len:", math.ceil(i))
print("Lam tron xuong:", math.floor(i))

print("===========")
# import các gói của module
# from math import ceil : from Module import gói


# tạo module
import myModule
print(myModule.tinhTong(3,4))

# from myModule import tinhTong
# print(tinhTong(3,4))


# Đặt tên cho module: import Module as TênĐặtLại

import myModule as abc
print(abc.tinhTich(2,7))


# import module trong thư mục
import os, sys
path = os.path.abspath(os.path.join('module'))
sys.path.append(path)
import MyModule
# print(MyModule.Hieu(3,5))