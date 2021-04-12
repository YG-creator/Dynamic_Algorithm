A = '0'+input()
B = '0'+input()
LCS = [[-1]*(len(A)) for _ in range(len(B))]
for i in range(len(A)) :
    for j in range(len(B)) :
        if i == 0 and j>0 :
            LCS[i][j] = LCS[i][j-1] + 1
        elif j == 0 and i>0 :
            LCS[i][j] = LCS[i-1][j] + 1
        elif A[i] == B[j] and i>0 and j>0  :
            LCS[i][j] = LCS[i-1][j-1]
        else :
            LCS[i][j] = min(LCS[i-1][j], LCS[i][j-1])+1
print(LCS[len(A)-1][len(B)-1])

