# positive.py

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

####################
# filter(name_of_function, iterable_data_type)
####################
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))