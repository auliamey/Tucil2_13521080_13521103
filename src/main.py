from dividenconquer import *
from bruteforce import *
from visualize import *
from utility import *
import time
def main():
    #I.S : user memasukkan jumlah titik dan dimensi titik
    #F.S : menampilkan jarak terdekat antara 2 titik, titik pertama, titik kedua, jumlah perhitungan, dan waktu eksekusi
    #Proses : main program
    print(color_text(95) + "=============================================================")
    print(color_text(96) + "               CLOSEST PAIR OF POINTS PROGRAM")
    print(color_text(96) + "             BY Fajar (13521080)-Joli (13521103)")
    print(color_text(95) + "=============================================================")
    n = int(input(color_text(34)  +"Masukkan jumlah titik                :   " + color_text(93)))
    dimensi = int(input(color_text(34) + "Masukkan dimensi titik               :   " + color_text(93)))
    print()
    print()
    if n > 0 and dimensi > 0:
        array = randomPoint(n,dimensi)
        sortbyx(array,0,n-1)
        if dimensi == 3:
            count = 0
            t1 = time.time()
            min,minPoint1,minPoint2,count =closestPairBf(array,n,dimensi,count)
            t2 = time.time()
            print(color_text(95) + "=============================================================")
            print(color_text(91) + "               PENDEKATAN SECARA BRUTE FORCE")
            print(color_text(95) + "=============================================================")
            print(color_text(34) + "Jarak terdekat antara 2 titik adalah : ",color_text(93),min)
            print(color_text(34) + "Titik pertama                        : ",color_text(93),minPoint1)
            print(color_text(34) + "Titik kedua                          : ",color_text(93),minPoint2)
            print(color_text(34) + "Jumlah perhitungan                   : ",color_text(93),count)
            print(color_text(34) + "Waktu eksekusi                       : ",color_text(93),t2-t1)
            print()
            
            count = 0
            t1 = time.time()
            min,minPoint1,minPoint2,count = closestPairDnC(array,n,dimensi,count)
            t2 = time.time()
            print(color_text(95) + "=============================================================")
            print(color_text(91) + "             PENDEKATAN SECARA DIVIDE CONQUER")
            print(color_text(95) + "=============================================================")
            print(color_text(34) + "Jarak terdekat antara 2 titik adalah : ",color_text(93),min)
            print(color_text(34) + "Titik pertama                        : ",color_text(93),minPoint1)
            print(color_text(34) + "Titik kedua                          : ",color_text(93),minPoint2)
            print(color_text(34) + "Jumlah perhitungan                   : ",color_text(93),count)
            print(color_text(34) + "Waktu eksekusi                       : ",color_text(93),t2-t1)
            

            visualize(array,minPoint1,minPoint2)
        elif dimensi>0 and dimensi != 3:
            count = 0
            t1 = time.time()
            min,minPoint1,minPoint2,count =closestPairBf(array,n,dimensi,count)
            t2 = time.time()
            print(color_text(95) + "=============================================================")
            print(color_text(91) + "               PENDEKATAN SECARA BRUTE FORCE")
            print(color_text(95) + "=============================================================")
            print(color_text(34) + "Jarak terdekat antara 2 titik adalah : ",color_text(93),min)
            print(color_text(34) + "Titik pertama                        : ",color_text(93),minPoint1)
            print(color_text(34) + "Titik kedua                          : ",color_text(93),minPoint2)
            print(color_text(34) + "Jumlah perhitungan                   : ",color_text(93),count)
            print(color_text(34) + "Waktu eksekusi                       : ",color_text(93),t2-t1)
            print()

            count = 0
            t1 = time.time()
            min,minPoint1,minPoint2,count = closestPairDnC(array,n,dimensi,count)
            t2 = time.time()
            print(color_text(95) + "=============================================================")
            print(color_text(91) + "             PENDEKATAN SECARA DIVIDE CONQUER")
            print(color_text(95) + "=============================================================")
            print(color_text(34) + "Jarak terdekat antara 2 titik adalah : ",color_text(93),min)
            print(color_text(34) + "Titik pertama                        : ",color_text(93),minPoint1)
            print(color_text(34) + "Titik kedua                          : ",color_text(93),minPoint2)
            print(color_text(34) + "Jumlah perhitungan                   : ",color_text(93),count)
            print(color_text(34) + "Waktu eksekusi                       : ",color_text(93),t2-t1)
        else: 
            print("Dimensi tidak valid")
    else:
        print("Jumlah titik atau dimensi tidak valid")


# sek ternyata gabisa balik ya
# exit = False
main()

# while not exit :
#     print("Apakah ingin lanjut program?")
#     print("1. Ya")
#     print("2. Tidak")
#     inputuser = int(input("Masukkan angka : "))
#     while (inputuser != 1 or inputuser != 2):
#         print("Masukkan salah! Masukkan input ulang!")
#         print("Apakah ingin lanjut program?")
#         print("1. Ya")
#         print("2. Tidak")
#         inputuser = int(input("Masukkan angka : "))
    
#     if (inputuser == 1):
#         main()
#     else :
#         exit = True
    