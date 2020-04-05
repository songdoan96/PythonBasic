def chia(x, y):
    return x/y

# Try 
try:
    print(chia(6, 0))
except Exception as e:
    print(e)

# Finally
print("======= Finally ======")
try:
    print(chia(7,0))
except Exception as e1:
    print(e1)
finally:
    print("Đoạn này luôn được thực thi")