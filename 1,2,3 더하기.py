T = int(input())
n = [int(input()) for _ in range(T)]
dp = [1,2,4]
for i in range(7) :
    dp.append(dp[i]+dp[i+1]+dp[i+2])
for j in n :
    print(dp[j-1])
