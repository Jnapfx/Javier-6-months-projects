a = [3,1,4,1,5,9,2,6,3,]


for range( len(a) ):
    for j in range(0, len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(a)