# two_times.py

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def three_times(x): 
    return x * 3

print(list(map(three_times, [1, 2, 3, 4])))