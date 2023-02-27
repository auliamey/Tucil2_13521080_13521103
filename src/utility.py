import random
import math

def color_text(code):
        return "\33[{code}m".format(code=code)

def randomPoint(npoint,dimensi):
# mengembalikan array of point dengan jumlah npoint dan dimensi yang sudah ditentukan dan memiliki posisi yang random
    arraypoint = []
    for i in range(npoint):
        point = []
        for j in range(dimensi):
            # random sebanyak dimensi, misal 2 (x,y) misal 3 (x,y,z)
            titik = random.randint(-1000,1000)
            point.append(titik)
        arraypoint.append(point)
    return arraypoint

def euclidean(a,b,n):
# mengembalikan jarak euclidean antara a dan b dengan dimensi R^n
    if n == 1:
        return (a[0]-b[0])
    else:
        return math.sqrt(euclidean(a,b,n-1)**2 + (a[n-1]-b[n-1])**2)

def euclideanCounter(a,b,n,ctr) :
    # mengembalikan jarak euclidean dan counter yang menghitung banyaknya perhitungan euclidean yang dilakukan
    ctr += 1
    return euclidean(a,b,n), ctr