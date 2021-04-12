n = int(input())    #숫자 갯수
a = list(map(int, input().split())) #수열
dp = [0 for i in range(n)]  #0x숫자갯수 리스트
for i in range(n):  #dp
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:   #증가하고 dp가 작을때에만 +1
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
