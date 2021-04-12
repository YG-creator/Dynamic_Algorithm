N = int(input())                          #사람 수
a = [0] + list(map(int,input().split()))  #잃는 체력
b = [0] + list(map(int,input().split()))  #얻는 기쁨
dp = [[0]*100 for _ in range(N+1)]
for i in range(1,N+1) :
    for j in range(100) :
        if j+a[i] < 100 :
            dp[i][j+a[i]] = dp[i-1][j] + b[i]
        if dp[i][j] < dp[i-1][j] :
            dp[i][j] = dp[i-1][j]
print(dp[N][99])
