

DP = []
def solution(S,a,b,c) :
    #모든 곡 다 불렀으면
    if S == 0 :
	#각자 불러야 하는 곡 다 불렀으면
	if a == 0 && b == 0 && c == 0 :
	    return 1
		
	else :
	    return 0
    
    res = DP[S][a][b][c]
    #이미 구해 놓은 경우면
    if res != -1 :
	return res
    res = 0
    res += solution(S - 1, a - 1, b, c)#a만 부를 경우
    res += solution(S - 1, a, b - 1, c)#b만 부를 경우
    res += solution(S - 1, a, b, c - 1)#c만 부를 경우
    res += solution(S - 1, a - 1, b - 1, c)#a,b가 부를 경우
    res += solution(S - 1, a - 1, b, c - 1)#a,c가 부를 경우
    res += solution(S - 1, a, b - 1, c - 1)#b,c가 부를 경우
    res += solution(S - 1, a - 1, b - 1, c - 1)#a,b,c가 부를 경우

    return res

S,a,b,c = map(int,input().split())
print(solution(S, a, b, c))

