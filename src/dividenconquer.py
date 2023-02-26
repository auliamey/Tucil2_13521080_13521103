from utility import *

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

def closestPairDnC(a,n,dimension,count):
    # mengembalikan jarak terdekat antara 2 titik dalam a dengan dimensi R^n dan pasangan titiknya
    if n == 2:
        print("1")
        count += 1
        return euclidean(a[0],a[1],dimension),a[0],a[1],count
    elif n == 3:
        print("3")
        count += 3
        nilai1 = euclidean(a[0],a[1],dimension)
        nilai2 = euclidean(a[0],a[2],dimension)
        nilai3 = euclidean(a[1],a[2],dimension)
        if nilai1 < nilai2 and nilai1 < nilai3:
            return nilai1,a[0],a[1],count
        elif nilai2 < nilai1 and nilai2 < nilai3:
            return nilai2,a[0],a[2],count
        else:
            return nilai3,a[1],a[2],count
    else :
        mid = n//2
        left = a[:mid]
        right = a[mid:]
        # buat ngedebug
        # print(left)
        # print(right)
        nilai1,p11,p21,count1= closestPair(left,mid,dimension,0)
        nilai2,p221,p22,count2= closestPair(right,n-mid,dimension,0)
        count += count1 + count2
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
                print("1")
                count += 1
                if euclidean(strip[i],strip[j],dimension) < nilai:
                    nilai = euclidean(strip[i],strip[j],dimension)
                    p1 = strip[i]
                    p2 = strip[j]
        
        return nilai,p1,p2,count


