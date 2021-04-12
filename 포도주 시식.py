N = int(input())                            #잔 갯수
vol = [int(input()) for _ in range(N)]      #각 잔마다 포도주 양
dp = [0 for _ in range(N)]                  #dp 리스트 생성
dp[0] = vol[0]                              #첫번째 dp
dp[1] = vol[0] + vol[1]                     #두번째 dp
dp[2] = max(vol[1]+vol[2],vol[0]+vol[2])    #세번째 dp
for i in range(3,len(vol)):                 #4~N번째 dp
    dp[i] = max(dp[i-1],dp[i-2]+vol[i],dp[i-3]+vol[i-1]+vol[i])
print(max(dp))                              #최대 dp
    


