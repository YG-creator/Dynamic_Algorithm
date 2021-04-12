N = int(input())    #집 갯수
cost = [list(map(int,input().split()))for _ in range(N)]        #n번째 페인트칠 가격
for i in range(N-1) :      
    for j in range(3) : #전행의 다른열의  최솟값을 더함
        if j == 0 :     
            cost[i+1][j] = min(cost[i][1],cost[i][2])+cost[i+1][j]
        elif j == 1 :
            cost[i+1][j] = min(cost[i][0],cost[i][2])+cost[i+1][j]
        else :
           cost[i+1][j] = min(cost[i][0],cost[i][1])+cost[i+1][j]
print(min(cost[N-1])    #최솟값 출력
