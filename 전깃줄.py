N= int(input())     #빨랫줄 갯수
A = [ list(map(int,input().split())) for _ in range(N) ] #빨랫줄
A.sort()    #오름차순
dp = [1] * len(A)   
for i in range(1,len(A)) :  #dp가 작거나 같고 걸린 빨랫줄 숫자가 클때 dp증가
    for j in range(i) :
        if A[j][1]<A[i][1] and dp[j]>=dp[i] :
            dp[i] = dp[j] + 1
cnt = 0
ma = dp.index(max(dp))  #dp 최댓값 인덱스
for i in range(ma-1,-1,-1) :    #백트랙킹
    if dp[i] == dp[ma] -1 :         
        ma = i
    else :              #백트랭킹 외 것은 cnt+=1
        cnt +=1
print(cnt)
