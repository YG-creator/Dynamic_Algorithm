N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
for i in range(N) :
    for j in range(M) :
        if i == 0 and j>0 :
            A[i][j] += A[i][j-1]
        elif j ==0 and i>0 :
            A[i][j] += A[i-1][j]
        elif i>0 and j>0 :
            A[i][j] += max(A[i][j-1],A[i-1][j],A[i-1][j-1])
print(A[N-1][M-1])

