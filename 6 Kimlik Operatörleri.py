# Görev 1: Aşağıdaki kodları çalıştırın ve sonuçlarını yorumlayın.
# is operatörü, nesnelerin kimliklerini (id) karşılaştırır, yani bellek adreslerinin aynı olup olmadığını kontrol eder.

a = 256
b = 256
print(a is b)  # Sonuç True, çünkü aynı değeri taşıyan a ve b değişkenleri aslında aynı nesneyi (256 sayısını) işaret ederler.

c = 257
d = 257
print(c is d)  # Sonuç True, aynı değeri taşıyan a ve b değişkenleri aslında aynı nesneyi (257 sayısını) işaret ederler.