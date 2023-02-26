import random
import matplotlib.pyplot as plt
import mpl_toolkits
from dividenconquer import *

# semi main tapi blom control kalo input salah
npoint = int(input("Masukkan banyak point : "))
dimensi = int(input("Masukkan dimensi yang diinginkan : "))
arraypoint = []
count = 0

for i in range(npoint):
    point = []
    for j in range(dimensi):
        # random sebanyak dimensi, misal 2 (x,y) misal 3 (x,y,z)
        titik = random.randint(-1000,1000)
        point.append(titik)
    arraypoint.append(point)
    
# cek isi titiknya aja si buat liat
for i in range(len(arraypoint)):
    print(arraypoint[i])

min = euclidean(arraypoint[0], arraypoint[1], dimensi)
minPoint1 = arraypoint[0]
minPoint2 = arraypoint[1]

for i in range(npoint):
    for j in range(npoint):
        if (i != j) :
            distance, count = euclideanCounter(arraypoint[i], arraypoint[j], dimensi, count)
            if distance < min :
                min = distance
                minPoint1 = arraypoint[i]
                minPoint2 = arraypoint[j]


print("Jarak terdekat " + str(min) + " dengan titik pertama " + str(minPoint1) + " dan titik kedua " + str(minPoint2)) 
print("Banyaknya perhitungan euclidean yang terjadi adalah " + str(count))          

# SUMPAH INI COBAEN DULU JAR
arrayX = []
arrayY = []
arrayZ = []

for i in range(len(arraypoint)):
    if(arraypoint[i] != minPoint1 and arraypoint[i] != minPoint2):
        arrayX.append(arraypoint[i][0])
        arrayY.append(arraypoint[i][1])
        arrayZ.append(arraypoint[i][2])

fig = plt.figure(figsize=(6,6))
# ax = fig.add_subplot(projection ='3d')
ax = plt.axes(projection ="3d")

# ax.plot_surface(arrayX, arrayY, arrayZ, cmap='3D', edgecolor='green')
ax.scatter3D(arrayX, arrayY, arrayZ, color = "green")
ax.scatter3D(minPoint1[0], minPoint1[1], minPoint1[2], color = "red")
ax.scatter3D(minPoint2[0], minPoint2[1], minPoint2[2], color = "blue")
print(minPoint1)
print(minPoint2)
plt.title("Visualize Points")
ax.set_xlabel('X-axis', fontweight ='bold')
ax.set_ylabel('Y-axis', fontweight ='bold')
ax.set_zlabel('Z-axis', fontweight ='bold')
 
# show plot
plt.show()