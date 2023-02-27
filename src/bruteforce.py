from utility import *

def closestPairBf(arraypoint,npoint,dimensi,count):
# mengembalikan jarak terdekat, titik pertama, dan titik kedua dari arraypoint dengan brute force
    min = euclidean(arraypoint[0], arraypoint[1], dimensi)
    minPoint1 = arraypoint[0]
    minPoint2 = arraypoint[1]

    for i in range(npoint-1):
        for j in range(i+1,npoint):
                distance = euclidean(arraypoint[i], arraypoint[j], dimensi)
                count += 1
                if distance < min :
                    min = distance
                    minPoint1 = arraypoint[i]
                    minPoint2 = arraypoint[j]
    return min,minPoint1,minPoint2,count
