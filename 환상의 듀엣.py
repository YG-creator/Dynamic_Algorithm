n = int(input())
a = list(map(int,input().split()))  #입력
b = []  #차이
c = []  #상덕  
d = []  #희원
sum = 0 #힘든정도 최솟값
for i in range(n-1) :   #차이 
    b.append(abs(a[i+1]-a[i]))
b_max = b.index(max(b)) #차이 최댓값 index
for j in range(b_max+1) :   #상덕
    c.append(a[j])
for i in range(b_max+1,n) : #희원
    if i == n-1 :
        d.append(a[i])
        an = 0
    elif (a[i] - a[b_max]) >= b[i-1] :
        d.append(a[i])
        an = 1
    else :
        a_index = i
        an = 1
        break
if an == 1 :
    for j in range(a_index,n) : #상덕
        c.append(a[j])
for i in range(len(c)-1) :  #힘든 정도 최솟값
    sum += abs(c[i+1]-c[i])
for j in range(len(d)-1) :
    sum += abs(d[j+1]-d[j])
print(sum)
