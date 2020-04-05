# input
age = input("Nhap tuoi cua ban: ")
print("Tuoi cua ban la: ", age)

# File
# open file : open(filePath, mode, buffer)
print('=========Open File =========')
openFile = open("test.txt")
readFile = openFile.read()
openFile.close()
print("Tuoi cua ban la: ", readFile)


print('=========write File =========')


wFile = open("test.txt", 'w+')
wFile.write('45')
wFile.close()

print(wFile.name)
print(wFile.close)
print(wFile.mode)
