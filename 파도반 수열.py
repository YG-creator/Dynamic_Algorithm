T = int(input())
N = [int(input()) for _ in range(T)]
a = [1,1,1]
for i in range(3,max(N)) :   
    a.append(a[i-3]+a[i-2])
for j in N :
    print(a[j-1])

        
