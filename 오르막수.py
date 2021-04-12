n = int(input())
s = [[0] * 10 for i in range(1001)]
for i in range(10):
    s[1][i] = 1
for i in range(2, 1001):
    for j in range(10):
        for k in range(j + 1):
            s[i][j] += s[i - 1][k]
print(sum(s[n]) % 10007)

'''
a
   0  1  2  3  4  5  6  7  8  9
1  1  1  1  1  1  1  1  1  1  1
n  1


a[n][i] = a[n][i-1]+a[n-1][i]
'''
