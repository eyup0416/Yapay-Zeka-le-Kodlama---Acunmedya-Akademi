# Görev 1: meyveler = ["elma", "armut", "çilek", "kiraz"] listesi veriliyor. 
# Kullanıcıdan bir meyve ismi alıp listede olup olmadığını in operatörüyle kontrol edin.

meyveler = ["elma", "armut", "çilek", "kiraz"]
kullanici_meyve = input("Bir meyve ismi giriniz: ").strip().lower()
print("Meyve listede var mı?:", kullanici_meyve in meyveler)

# Görev 2: parola = "PyThOn123" değişkeni oluşturun. Kullanıcıdan bir karakter girmesini isteyin. 
# Bu karakter parolada yoksa (not in) "Parolada bu karakter yok" yazdırın.

parola = "PyThOn123"
kullanici_karakter = input("Bir karakter giriniz: ")
if kullanici_karakter not in parola:
    print("Parolada bu karakter yok")
