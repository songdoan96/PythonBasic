print("=========== Hàm =========")


def sayHello(a):
    print(a)


sayHello("doan quang song")

print("=========== Hàm có trả về =========")


def sum(a, b):
    return a + b


x = sum(2, 3)
print(x)

print("=========== 7. Biến global =========")

str1 = "Ten cua tui"


def getName(str1):
    str1 = "Doan quang song"
    print(str1)
def getNameGlobal():
    global str1
    str1 = "Bien Global"
    print(str1)

getName(str1)
print(str1)

print("=========== 9. Truyền vô số tham số =========")


def getSum(*n):
    t = 0
    for i in n:
        t += i
    return t


print(getSum(1, 2, 4))

