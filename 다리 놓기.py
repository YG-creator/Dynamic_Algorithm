def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

t = int(input())
n_m = [list(map(int,input().split()))for _ in range(t)]
for i in range(t) :
    print(factorial(n_m[i][1])/factorial(n_m[i][0])/factorial(n_m[i][1]-n_m[i][0]))
