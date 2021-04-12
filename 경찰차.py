n = int(input())    #도로 크기
w = int(input())    #사건 수
cop1 = [1,1]        #경찰1 위치
cop2 = [n,n]        #경찰2 위치
location = [list(map(int,input().split())) for _ in range(w)]   #사건 위치
who = []    #사건 담당 경찰
sum = 0     #총 거리
for i in range(3) : #총거리 최솟값, 사건 담당 경찰
    cop1_length = abs(cop1[0]-location[i][0]) + abs(cop1[1]-location[i][1])
    cop2_length = abs(cop2[0]-location[i][0]) + abs(cop2[1]-location[i][1])
    if cop1_length <= cop2_length :
        cop1 = location[i]
        who.append(1)
        sum += cop1_length
    else :
        cop2 = location[i]
        who.append(2)
        sum += cop2_length
print(sum)
for i in range(w) :
    print(who[i])

