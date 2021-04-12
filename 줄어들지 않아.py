T = int(input())        #케이스 수
n = [int(input()) for _ in range(T)]    #숫자 자리수
dp = [[1]*10 for _ in range(max(n))]    #가능한 숫자 개수
for i in range(1,10) :
    for j in range(1,max(n)) :
        dp[j][i] = dp[j-1][i] + dp[j][i-1]
for i in n :
    print(sum(dp[i-1]))

