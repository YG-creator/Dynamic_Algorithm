st = input()
a = input()
b = input()
c = [[],[],[]]
d = [[],[],[]]
cnt = 0
for i in range(len(st)) :
    for j in range(len(a)) :
        if i%2 == 0 :
            if a[j] == st[i] :
                c[i].append(j)
        else :
            if b[j] == st[i] :
                c[i].append(j)
            
for i in range(len(st)) :
    for j in range(len(b)) :
        if i%2 == 0 :
            if b[j] == st[i] :
                d[i].append(j)
        else :
            if a[j] == st[i] :
                d[i].append(j)

for j in c[0] :
    for k in c[1] :
        for l in c[2]:
            if j < k < l :
                cnt +=1
for j in d[0] :
    for k in d[1] :
        for l in d[2]:
            if j < k < l :
                cnt +=1
print(cnt)
