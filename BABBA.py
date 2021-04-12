k = int(input())
a = 'A'
for i in range(k) :
    c = ''
    for j in range(len(a)) :
        if a[j] == 'A' :
            c += 'B'
        else :
            c += 'BA'
    a = c
print(a)
print(a.count('A'),a.count('B'),sep=' ')

        
    
        
    
    
