# SUMPAH INI COBAEN DULU JAR
import matplotlib.pyplot as plt

def visualize(arraypoint, minPoint1, minPoint2):
# I.S : arraypoint berisi array of point, minPoint1 dan minPoint2 berisi titik terdekat
# F.S : menampilkan plot 3D dari arraypoint dengan titik terdekat ditandai dengan warna merah dan biru
# Proses : mengambil semua titik kecuali titik terdekat, lalu menampilkan plot 3D dari arraypoint dengan titik terdekat ditandai dengan warna merah dan biru
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
    # print(minPoint1)
    # print(minPoint2)
    plt.title("Visualize Points")
    ax.set_xlabel('X-axis', fontweight ='bold')
    ax.set_ylabel('Y-axis', fontweight ='bold')
    ax.set_zlabel('Z-axis', fontweight ='bold')
    
    # show plot
    plt.show()