n = int(input())
a,b = map(int,input().split())
c = [int(input()) for _ in range(n-2)]
cnt = 0
for i in c :
    if abs(a-i) <= abs(b-i) :
        min1 = abs(a-i)
        cnt += min1
        a = i
        print(a)
    else :
        min1 = abs(b-i)
        cnt += min1
        b = i
        print(b)
print(cnt)
