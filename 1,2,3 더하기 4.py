n = int(input())
for _ in range(n):
    dp = [[1,0,0],[1,1,0],[1,1,1]]
    a = int(input())
    if a<=3:
        print(sum(dp[a-1]))
        continue
    for i in range(3, a+1):
        tmp = []
        tmp.append(dp[i-1][0])
        tmp.append(dp[i-2][0]+dp[i-2][1])
        tmp.append(dp[i-3][2]+dp[i-3][1]+dp[i-3][0])
        dp.append(tmp)
    print(sum(dp[a-1]))
