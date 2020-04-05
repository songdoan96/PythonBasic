name = "YeuToQuocYeuDongBao"
for i in name:
    print(i)

print("==================")

for i in range(0, 10):
    for j in range(i, 10):
        print(j, end=" ")
    print("")

print("======== While ==========")
i = 1
while i < 10:
    j = 1
    while j < (10-i):
        print(j, end=" ")
        j += 1
    print("")
    i += 1


# Break
strName = "DoanQuangSong"
for i in strName:
    if i == 'a':
        break
    print(i, end=" ")

# Continue
print()
for j in strName:
    if j == "a":
        continue
    print(j, end=" ")

