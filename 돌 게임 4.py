n = int(input())
dp = [0]*n
dp[0] = dp[2] = 0
dp[1] = dp[3] = 1
for i in range(4,n) :
    if dp[i-1] and dp[i-3] and dp[i-4] :
        dp[i] = 0
    else :
        dp[i] = 1
if dp[n-1] == 1 :
    print('SK')
else :
    print('CY')
    
