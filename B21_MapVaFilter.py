# map : map(function,list1,list2,...) : các list cũng có thể là direc


def hamMu(x):
    return x * x


list1 = [1, 3, 2, 8]

func = map(hamMu, list1)
print(list(func))


# c2 viết gọn
list2 = [2, 6, 4, 7, 7]
list3 = [4, 3, 1, 9, 7]
f = map(lambda x, y: x+y, list2, list3)
print(list(f))


# filter: duyệt qua các phần tử trả về phần tử đúng đk nếu True

def chiaHai(x):
    if(x % 2 == 0):
        return x


ff = filter(chiaHai, [2, 3, 1, 6, 7])
print(list(ff))

fff = filter(lambda x: x % 2 == 0, [2, 1, 4, 5, 6, 3, 4, 8, 2])
print(list(fff))
