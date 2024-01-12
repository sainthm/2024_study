# readline.py

try:
    f = open('./newfile.txt', 'r')
    line = f.readline()
    print(line)
    f.close()
except AttributeError:
    pass