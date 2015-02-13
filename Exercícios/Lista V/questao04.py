# coding=utf-8
k = 0
i = 18644
while i <= 33087:
    if '2' in str(i) and '7' not in str(i):
        k += 1
    i += 1
print("%d números sortudos" % k)
