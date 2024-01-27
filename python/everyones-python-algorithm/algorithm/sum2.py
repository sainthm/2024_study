# sum2.py
# 문제: 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘

def sum_n(n):
    return n * (n+1) // 2

print(sum_n(10))
print(sum_n(100))
print(sum_n(1000))