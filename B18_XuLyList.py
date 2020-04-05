myName = "Doan Quang Song"
listTest = ['A', 1, 5, 's']

# List: trả về list của chuỗi
print("list: ", list(myName))

# len: độ dài
print(len(listTest))

# extend : thêm phần tử vào cuối mảng + append() :giống(chỉ thêm được 1 phẩn tử)
listTest.extend(('D', 4))
print(listTest)
print("Độ dài len: ", len(listTest))
listTest.append(("C", 9))
print(listTest)
print("Độ dài len: ", len(listTest))

# count: đếm số lần xuất hiện
print("cout: ", listTest.count('s'))

# index: trả về vị trí đầu tiên, nếu ko tìm thấy thì exception
print("index: ", listTest.index('s'))

# insert : chèn x vào vị trí 5
listTest.insert(5, 'x')
print("Insert: ", listTest)

# reverse : đảo ngược chuỗi
listTest.reverse()
print("reverse: ", listTest)

# remove: xoá các phần tử
listTest.remove('s')
print("Remove phần tử: ",listTest)

# pop : xoá phần tử theo index
listTest.pop(3)
print(listTest)

# clear: xoá all phần tử
listTest.clear()
print(listTest)

# sort : sắp xếp tăng(False), giảm(True): cùng kiểu
listSort = ['d', 'a', 's', 'f']
listSort.sort()
print(listSort)

listSort.sort(reverse=True)
print(listSort)
