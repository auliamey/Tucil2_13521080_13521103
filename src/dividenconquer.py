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
    pivot = a[(i+j)//2]
    p = i
    q = j
    while True:
        while a[p][0] < pivot[0] :
            p += 1
        while a[q][0] > pivot[0] :
            q -= 1
        if p < q :
            temp = a[p]
            a[p] = a[q]
            a[q] = temp
            p += 1
            q -= 1
        else:
            return q


def closestPairDnC(a,n,dimension,count):
    # mengembalikan jarak terdekat antara 2 titik dalam a dengan dimensi R^n dan pasangan titiknya
    if n == 2:
        # print("1")
        count = 1
        return euclidean(a[0],a[1],dimension),a[0],a[1],count
    elif n == 3:
        # print("3")
        count = 3
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
        nilai1,p11,p21,count1= closestPairDnC(left,mid,dimension,0)
        nilai2,p221,p22,count2= closestPairDnC(right,n-mid,dimension,0)
        count = count1 + count2
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
        stripleft = []
        stripright = []
        if n%2 == 0:
            mid = (a[mid-1][0]+a[mid][0])/2
            # print(mid)
        else :
            mid = a[mid][0]
        for i in left:
            if i[0] > mid - nilai:
                stripleft.append(i)
        for i in right:
            if i[0] < mid + nilai:
                stripright.append(i)
        # buat ngedebug
        # for i in strip:
        #     print(i)

        for i in stripleft:
            for j in stripright:
                cek = True
                for k in range(dimension):
                    if abs(i[k]-j[k]) >= nilai:
                        cek = False
                if cek :
                    count += 1
                    x = euclidean(i,j,dimension)
                    if x < nilai:
                        nilai = x
                        p1 = i
                        p2 = j
        return nilai,p1,p2,count


# array1 = randomPoint(10,4)
# points = randomPoint(100,4)
# sortbyx(points,0,len(points)-1)
# print(points)
# sortbyx(array1,0,len(array1)-1)
# array = [[-2],[14],[-5],[-1],[0]]
# sortbyx(array,0,len(array)-1)
# print(array)
# min,p1,p2,count = closestPairDnC(array,len(array),2,0)
# min1,p11,p21,count1 = closestPairDnC(array1,len(array1),4,0)

# print("Jarak terdekat antara 2 titik dalam array adalah",min,"dengan pasangan titik",p1,"dan",p2)
# print("Jumlah perhitungan euclidean yang dilakukan adalah",count)

# print(count1)
