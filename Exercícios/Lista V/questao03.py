# coding=utf-8
k = 0
i = 1067
while i <= 3627:
    if i % 2 == 0 and i % 7 == 0:
        k += 1
    i += 1
print("%d números pares e divisíveis por 7" % k)
