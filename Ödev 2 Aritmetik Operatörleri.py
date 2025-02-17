# Görev 1: Kullanıcıdan iki sayı alın. Bu sayılar üzerinde toplama (+), çıkarma (-), çarpma (*), bölme (/), 
# tam bölme (//), mod alma (%), ve üs alma (**) işlemlerini yapıp sonuçları ekrana yazdırın.

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

print("Toplama:", sayi1 + sayi2)
print("Çıkarma:", sayi1 - sayi2)
print("Çarpma:", sayi1 * sayi2)
print("Bölme:", sayi1 / sayi2)
print("Tam Bölme:", sayi1 // sayi2)
print("Mod Alma:", sayi1 % sayi2)
print("Üs Alma:", sayi1 ** sayi2)

# Görev 2: Bir dairenin alanını hesaplayın. Kullanıcıdan yarıçapı alın ve formülü π * r² kullanarak sonucu yazdırın (π = 3.14).

pi = 3.14
yaricap = float(input("Dairenin yarıçapını girin: "))
alan = pi * yaricap ** 2
print("Dairenin alanı:", alan)
