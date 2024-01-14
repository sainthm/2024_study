# xx_times.py

## two_times
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

## 3
def three_times(x): 
    return x * 3

print(list(map(three_times, [1, 2, 3, 4])))
# print(map(three_times, [1, 2, 3, 4]))


## 4
print(list(map(lambda a: a*4, [1, 2, 3, 4])))