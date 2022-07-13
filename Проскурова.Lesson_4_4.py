a = [5, 5, 65, 85, 65, 15, 9, 9]
a1 = []
for x in a:
    if a.count(x) > 1:
        a1.append(x)
        a.remove(x)
print(a, a1)







