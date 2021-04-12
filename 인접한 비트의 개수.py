s = [[[0 for i in range(2)] for j in range(100)] for k in range(101)]
s[1][0][0] = 1
s[1][0][1] = 1
for n in range(2, 101):
    for k in range(n):
        s[n][k][0] = s[n - 1][k][0] + s[n - 1][k][1]
        s[n][k][1] = s[n - 1][k][0] + s[n - 1][k - 1][1]
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(sum(s[n][k]))
