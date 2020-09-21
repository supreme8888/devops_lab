a = input("Input first numbers sequence divided by spaces:").split()
for i in range(len(a)):
    a[i] = int(a[i])
b = input("Input second numbers sequence divided by spaces:").split()
for i in range(len(b)):
    b[i] = int(b[i])

print(sorted(list(set(a) & set(b))))
