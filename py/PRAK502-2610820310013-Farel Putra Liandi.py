def mutlak(angka):
    if angka < 0:
        return -angka
    return angka

def hitung(nilai1, nilai2):
    return mutlak(nilai1 - nilai2)

data = list(map(int, input().split()))
a, c, b, d = data[0], data[1], data[2], data[3]

hasil = hitung(a, b) + hitung(c, d)
print(mutlak(hasil))