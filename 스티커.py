T = int(input())
for _ in range(T) :
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dp_0 = [a[0],a[0]+b[1]]
    dp_1 = [b[0],b[0]+a[1]]
    for i in range(2,n) :
        dp_0.append(max(dp_0[i-1],dp_1[i-2])+a[i])
        dp_1.append(max(dp_1[i-1],dp_0[i-2])+b[i])
    print(max(dp_0[n-1],dp_1[n-1]))
                    
