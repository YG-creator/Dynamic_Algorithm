D,K = map(int,input().split())
dp = ['a','b']
for i in range(2,D) :
    dp.append(dp[i-2]+dp[i-1])
a = dp[D-1].count('a')
b = dp[D-1].count('b')
for i in range(K//a) :
    if (K - i * a) % b == 0 :
        c = i
        d = (K - i * a) // b
        break
print(c)
print(d)
