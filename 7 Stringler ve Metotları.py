# Görev 1: Kullanıcıdan bir metin girmesini isteyin. Bu metni: Tüm harfleri büyük yapın, Başındaki ve sonundaki boşlukları silin,
# "a" harflerini "e" ile değiştirin, Boşluklara göre split edip kelimeleri liste halinde yazdırın.

metin = input("Bir metin giriniz: ")
metin = metin.replace('a', 'e').replace('A', 'E').upper().strip()
kelimeler = metin.split()
print(kelimeler)

# Görev 2: "Python programlama dili" metnini ters çevirip ekrana yazdırın. 
# Ardından replace() metoduyla "programlama" yerine "kodlama" yazın.

metin = "Python programlama dili"
ters_metin = metin[::-1]
kodlamali_metin = ters_metin.replace("programlama"[::-1], "kodlama"[::-1])
print("Ters çevrilmiş metin:", ters_metin)
print("Replace işlemi sonrası metin:", kodlamali_metin[::-1])