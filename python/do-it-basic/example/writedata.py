# wirtedata.py

f = open('./newfile.txt', 'w')
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

# for i in range(1, 11):
#     data = f"{i} 번째 줄입니다."
#     print(data)