N,k = map(int,input().split())
pi = list(map(int,input().split()))
a = ''
for i in range(N-1) :
    if pi[i] > pi[i+1] :    #감소
        a += '0'
    elif pi[i] < pi[i+1] :  #증가
        a += '1'
if '0'*k in a :
    print('NO')
else :
    print('YES')
