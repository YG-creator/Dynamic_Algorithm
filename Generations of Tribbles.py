t = int(input())
a = [int(input()) for _ in range(t)]
s = [1, 1, 2, 4]
for j in range(4, max(a) + 1):
    s.append(s[j - 1] + s[j - 2] + s[j - 3] + s[j - 4])
for i in a :
    print(s[i])
