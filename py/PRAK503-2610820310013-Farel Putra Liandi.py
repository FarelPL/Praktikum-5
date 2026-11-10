def maksimal(a, b):
    if a > b:
        return a
    return b

def minimal(a, b):
    if a < b:
        return a
    return b

bilangan = int(input())

angka_list = list(map(int, input().split()))
    
maks = angka_list[0]
minim = angka_list[0]
    
batas = 1
while batas < bilangan:
    nilai = angka_list[batas]
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)
    batas += 1
        
print(f"{maks} {minim}")