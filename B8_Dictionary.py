me = {
    'Name': 'Doan Quang Song',
    'Age': 24,
    'Male': True
}
print(me)
print(me['Age'])

# Thay đổi giá trị

me['Age'] = 25
print(me)

#Xoá phần tử

del me['Age']
print(me)

#xoá hết phẩn tử
me.clear()
print(me)

# xoá dictionary
del me

