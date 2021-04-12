a = '0' + input()
b = '0' + input()
dp = [[0]*len(a) for _ in range(len(b))]
c = ''
for i in range(1,len(a)) :
    dp[i][0] = dp[i-1][0] + 1 
for j in range(1,len(b)) :
    dp[0][j] = dp[0][j-1] + 1
for i in range(1,len(b)) :
    for j in range(1,len(a)) :
        if a[j] == b[i] :
            dp[i][j] = dp[i-1][j-1]
        else :
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + 1            
print(dp[len(a)-1][len(b)-1])

n = len(b)-1
m = len(a)-1
for i in range(m,0,-1) :
    for j in range(n,0,-1) :
        if a[j] == b[i] :
            c += a[j]
            n = j-1
            m = i-1
            break
print(c[::-1])
