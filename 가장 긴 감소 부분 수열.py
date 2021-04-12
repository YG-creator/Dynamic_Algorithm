N = int(input())
A = list(map(int,input().split()))
dp = [1]*len(A)
for i in range(1,N) :
    for j in range(i-1,-1,-1) :
        if A[i]<A[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
print(max(dp))
