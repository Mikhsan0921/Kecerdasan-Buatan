import random
from math import pow, sqrt


data_mahasiswa = [
    ("Andi", 80, 90),
    ("Budi", 85, 95),
    ("Cici", 78, 85),
    ("Dedi", 90, 88),
    ("Eka", 76, 80),
    ("Fina", 92, 91),
    ("Gina", 79, 84),
    ("Hadi", 84, 82),
    ("Indah", 80, 89),
    ("Joko", 70, 78),
    ("Kiki", 75, 77),
    ("Lina", 65, 75),
    ("Mila", 72, 70),
    ("Nina", 68, 65),
    ("Oki", 90, 92),
    ("Putri", 82, 81),
    ("Rina", 86, 87),
    ("Sari", 88, 90),
    ("Tini", 78, 77),
    ("Umar", 60, 70)
]


titik = [(mhs[1], mhs[2]) for mhs in data_mahasiswa]


def jarak_euclidean(a, b):
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))


def bagi_titik_ke_centroid(titik, centroids):
    cluster = [[] for _ in centroids]
    for t in titik:
        jarak = [jarak_euclidean(t, centroid) for centroid in centroids]
        indeks_jarak_minimum = jarak.index(min(jarak))
        cluster[indeks_jarak_minimum].append(t)
    return cluster

def hitung_ulang_centroid(cluster):
    centroids = []
    for c in cluster:
        if c:
            koordinat_x = [t[0] for t in c]
            koordinat_y = [t[1] for t in c]
            centroid = (sum(koordinat_x) / len(koordinat_x), sum(koordinat_y) / len(koordinat_y))
            centroids.append(centroid)
    return centroids

def k_means(titik, centroids):
    while True:
        cluster = bagi_titik_ke_centroid(titik, centroids)
        centroids_baru = hitung_ulang_centroid(cluster)
        if centroids_baru == centroids:
            break  
        centroids = centroids_baru
    return cluster, centroids

centroid_awal = [(80, 80), (60, 60), (90, 90)]  
k = len(centroid_awal)

cluster, centroids = k_means(titik, centroid_awal)

print("Cluster:")
for i, c in enumerate(cluster):
    nama_mahasiswa = [data_mahasiswa[titik.index(t)][0] for t in c]
    nilai_uts = [t[0] for t in c]
    nilai_uas = [t[1] for t in c]
    rata_rata_uts = sum(nilai_uts) / len(nilai_uts)
    rata_rata_uas = sum(nilai_uas) / len(nilai_uas)
    print(f"Cluster {i + 1}: {nama_mahasiswa}")
    print(f"Rata-rata UTS: {rata_rata_uts}")
    print(f"Rata-rata UAS: {rata_rata_uas}")
print("Centroid:", centroids)
