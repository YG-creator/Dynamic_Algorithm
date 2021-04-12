N = int(input())
cnt = 0
for i in range(1,400) :
    if N >= i**2 :
        a = i
    else :
        break
for i in range(a,0,-1) :
    cnt += N//(i**2)
    N %= i**2
print(cnt)

