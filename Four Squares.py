n = int(input())                #숫자 입력
a = 223                         #제곱할 숫자 범위 제한
cnt = 0                         #제곱할 숫자 갯수
while(1) :
    if n == 0 :
        break
    for i in range(a,0,-1) :    
        if n >= i**2 :
            n %= i**2
            a = i
            cnt += 1
            break
print(cnt)
