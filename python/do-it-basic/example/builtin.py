# builtin.py

print("dir")
dir([1, 2, 3])
print(dir([1, 2, 3]))

print("*" * 10)

dir({"1": "a"})
print(dir({"1": "a"}))

print("*" * 10)

print("enumerate")
for i, name in enumerate(["body", "foo", "bar"]):
    print(i, name)