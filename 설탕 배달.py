N = int(input())
dp = [-1,-1,1,-1,1]
for j in range( N-3) :
    if dp[j] >0 :
        dp.append(dp[j]+1)
    else :
        if dp[j+2] > 0 :
            dp.append(dp[j+2]+1)
        else :
            dp.append(-1)
print(dp[N-1])
            
    
