from dividenconquer import *
from bruteforce import *
from visualize import *
from utility import *
import time

n = int(input("Masukkan jumlah titik : "))
dimensi = int(input("Masukkan dimensi titik : "))
if n > 0 and dimensi > 0:
    array = randomPoint(n,dimensi)
    sortbyx(array,0,n-1)
    if dimensi == 3:
        count = 0
        t1 = time.time()
        min,minPoint1,minPoint2,count =closestPairBf(array,n,dimensi,count)
        t2 = time.time()
        print("Jarak terdekat antara 2 titik adalah : ",min)
        print("Titik pertama : ",minPoint1)
        print("Titik kedua : ",minPoint2)
        print("Jumlah perhitungan : ",count)
        print("Waktu eksekusi : ",t2-t1)

        count = 0
        t1 = time.time()
        min,minPoint1,minPoint2,count = closestPairDnC(array,n,dimensi,count)
        t2 = time.time()
        print("Jarak terdekat antara 2 titik adalah : ",min)
        print("Titik pertama : ",minPoint1)
        print("Titik kedua : ",minPoint2)
        print("Jumlah perhitungan : ",count)
        print("Waktu eksekusi : ",t2-t1)

        visualize(array,minPoint1,minPoint2)
    elif dimensi>0 and dimensi != 3:
        count = 0
        t1 = time.time()
        min,minPoint1,minPoint2,count =closestPairBf(array,n,dimensi,count)
        t2 = time.time()
        print("Jarak terdekat antara 2 titik adalah : ",min)
        print("Titik pertama : ",minPoint1)
        print("Titik kedua : ",minPoint2)
        print("Jumlah perhitungan : ",count)
        print("Waktu eksekusi : ",t2-t1)

        count = 0
        t1 = time.time()
        min,minPoint1,minPoint2,count = closestPairDnC(array,n,dimensi,count)
        t2 = time.time()
        print("Jarak terdekat antara 2 titik adalah : ",min)
        print("Titik pertama : ",minPoint1)
        print("Titik kedua : ",minPoint2)
        print("Jumlah perhitungan : ",count)
        print("Waktu eksekusi : ",t2-t1)
    else: 
        print("Dimensi tidak valid")
else:
    print("Jumlah titik atau dimensi tidak valid")