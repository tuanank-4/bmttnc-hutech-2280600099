# Tạo một danh sách rỗng để lưu kết quả
j=[]
3 # Duyệt qua tất cả các số trong đoạn từ 2000 đến 3200, kiểm tra xem số 1 có chia hết cho 7 và không phải là bội số của 5 không
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print (','.join(j))