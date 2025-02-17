# Görev 1: Aşağıdaki koşulları kontrol eden mantıksal ifadeler yazın ve sonuçlarını ekrana yazdırın.

yas = int(input("Yaşınızı giriniz: "))
print("18 ile 65 arasında mı?:", yas > 18 and yas < 65)
print("18'den küçük veya 65'ten büyük mü?:", yas < 18 or yas > 65)
print("Yaş 25 değil mi?:", not (yas == 25))

# Görev 2: Kullanıcıdan bir sayı alın. Bu sayının çift olup olmadığını ve pozitif olup olmadığını kontrol eden bir koşul yazın. 
# Eğer sayı çiftse ekrana True, değilse False yazdırın.

sayi = int(input("Bir sayı giriniz: "))
cift_mi = sayi % 2 == 0
pozitif_mi = sayi > 0
print("Sayı çift mi?:", cift_mi)
print("Sayı pozitif mi?:", pozitif_mi)

# Görev 3: Kullanıcıdan bir yaş bilgisi alın. 
# Yaş 18'den büyük ve ehliyet bilgisi True ise "Araba kullanabilirsiniz" değilse "Araba kullanamazsınız" yazdırın.

yas = int(input("Yaşınızı girin: "))
ehliyet = input("Ehliyetiniz var mı? (True/False): ").strip().lower() == "true"
if yas > 18 and ehliyet:
    print("Araba kullanabilirsiniz")
else:
    print("Araba kullanamazsınız")