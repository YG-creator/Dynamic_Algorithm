n = int(input())                        #사과 갯수
apple = list(map(int,input().split()))  #원하는 사과나무 높이
apple_sum = sum(apple)                  #사과나무 높이 합
turn = apple_sum // 3                   
if apple_sum % 3 != 0:
    print('NO')
else:
    for a in apple:
        turn -= (a//2)
    if turn > 0:
        print('NO')
    else:
        print('YES')
