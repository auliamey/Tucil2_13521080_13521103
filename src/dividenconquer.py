import math
def sortbyx(a,i,j):
# I.S : a terdefinisi
# F.S : a terurut berdasarkan x
# Proses : mengurutkan a berdasarkan x dengan menggunakan algoritma quick sort
    if i<j:
        k = partisibyx(a,i,j)
        sortbyx(a,i,k)
        sortbyx(a,k+1,j)

def partisibyx(a,i,j):
# I.S : a terdefinisi
# F.S : a terurut berdasarkan x
# Proses : mengurutkan a berdasarkan x dengan menggunakan algoritma divide and conquer
    x = a[(i+j)//2][0]
    p = i
    q = j
    while True:
        while(a[p][0] < x):
            p = p + 1
        while(a[q][0] > x):
            q = q - 1
        if p < q :
            temp = a[p]
            a[p] = a[q]
            a[q] = temp
            p = p+1
            q = q-1
        if p>=q :
            break
    return q

def euclidean(a,b,n):
# mengembalikan jarak euclidean antara a dan b dengan dimensi R^n
    if n == 1:
        return (a[0]-b[0])
    else:
        return math.sqrt(euclidean(a,b,n-1)**2 + (a[n-1]-b[n-1])**2)

def closestPair(a,n,dimension):
    # mengembalikan jarak terdekat antara 2 titik dalam a dengan dimensi R^n dan pasangan titiknya
    if n == 2:
        return euclidean(a[0],a[1],dimension),a[0],a[1]
    elif n == 3:
        d = min(euclidean(a[0],a[1],dimension),euclidean(a[0],a[2],dimension),euclidean(a[1],a[2],dimension))
        if d == euclidean(a[0],a[1],dimension):
            return d,a[0],a[1]
        elif d == euclidean(a[0],a[2],dimension):
            return d,a[0],a[2]
        else:
            return d,a[1],a[2]
    else :
        mid = n//2
        left = a[:mid]
        right = a[mid:]
        # buat ngedebug
        # print(left)
        # print(right)
        nilai1,p11,p21 = closestPair(left,mid,dimension)
        nilai2,p221,p22 = closestPair(right,n-mid,dimension)
        nilai = 0
        p1 = []
        p2 = []
        if nilai1 < nilai2 :
            nilai = nilai1
            p1 = p11
            p2 = p21
        else :
            nilai = nilai2
            p1 = p221
            p2 = p22
        strip = []
        if n%2 == 0:
            mid = (a[mid-1][0]+a[mid][0])/2
        else :
            mid = a[mid][0]
        for i in left:
            if i[0] >= mid - nilai:
                strip.append(i)
        for i in right:
            if i[0] <= mid + nilai:
                strip.append(i)
        # buat ngedebug
        # for i in strip:
        #     print(i)

        for i in range(len(strip)):
            for j in range(i+1,len(strip)):
                if euclidean(strip[i],strip[j],dimension) < nilai:
                    nilai = euclidean(strip[i],strip[j],dimension)
                    p1 = strip[i]
                    p2 = strip[j]
        return nilai,p1,p2

A = [[2,3],[12,30],[40,50],[5,1],[12,10],[1,1]]
sortbyx(A,0,len(A)-1)
nilai,p,q = closestPair(A,len(A),2)
print(nilai,p,q)



        
