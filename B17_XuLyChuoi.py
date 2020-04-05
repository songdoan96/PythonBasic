str = "esanIsi iSRure eSsie ad ut"
str2 = "Dolore cons\tequat nisi voluptate aliqua anim."


print("\nChuỗi của tui: ", str)

print("\nIn hoa ký tự đầu: ", str.capitalize())
print("\nIn hoa ALL ký tự: ", str.upper())
print("\nViết thường ALL ký tự: ", str.lower())
# Tìm chuỗi nếu ko tìm thấy trả về -1
print("\nTìm kiếm chuỗi,vị trí bắt đầu chuỗi: ",str.find('iS')) 
# Tìm chuỗi giống find nếu ko tìm thấy trả về exception
print("Index: ",str.index("iS"))


print("\nChuỗi nằm giữa, ký tự * 2 đầu, all chiếm 50 ký tự: ", str.center(50, "*"))
print("\nĐếm số ký tự i,từ vị trí 5, độ dài 10 ký tự: ", str.count("i", 5, 10))
print("\nKtra ký tự cuối cùng của chuỗi có phải 'i' từ vtri 5, độ dài 4 ký tự: ", str.endswith("i", 5, 4))
print("\nThay \\t bằng tab- (8 space): ",str2.expandtabs())