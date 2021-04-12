N = int(input())        #행 갯수
num = [list(map(int,input().split())) for _ in range(N)]    #숫자 입력
for i in range(N-1) :   
    for j in range(len(num[i+1])) :
        if j == 0 : #첫번째거는 전행 첫번째거에 더함
            num[i+1][j] += num[i][0]
        elif j == len(num[i+1])-1 : #마지막거는 전행 마지막거에 더함
            num[i+1][j] += num[i][len(num[i])-1]
        else :  #나머지는 왼쪽/오른쪽 대각선중에 최대값에 더함
            num[i+1][j] += max(num[i][j-1],num[i][j])
print(max(num[N-1]))

