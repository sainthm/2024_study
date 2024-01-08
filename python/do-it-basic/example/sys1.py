# sys1.py
# python3 sys1.py aaa bbb ccc
import sys

args = sys.argv[1:]
for i in args:
    print(i)