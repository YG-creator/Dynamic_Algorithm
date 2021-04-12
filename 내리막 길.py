import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
m,n = map(int,input().split())
MAP = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dp[m-1][n-1] = 1

def dfs(x,y):

 if dp[x][y] == -1: #방문하지않음
 dp[x][y] = 0 #방문으로표시
 for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
 if 0<=x+dx<m and 0<=y+dy<n and MAP[x][y]>MAP[x+dx][y+dy]:
 dp[x][y] += dfs(x+dx,y+dy)
 return dp[x][y]

print(dfs(0,0))
