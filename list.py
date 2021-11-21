
liste = ["bmw","mercedes","audi","mazda","bugatti","ferrari"]

# 1.SORU mazda ismini toyota ile değiştir

liste[-1] = "toyota"
sonuc = liste

# 2.SORU audi dizinin bir elamnımıdır?

sonuc = 'audi' in liste

# 3.SORU listenin -2. elmanı kimdir?

sonuc = liste[-2]

#4. SORU listenin ilk 3 elmanını alın

sonuc = liste[0:3]

#5. SORU son 2 elamanı toyota ve tesla yapınz

liste[-2:]= ['Toyota','Tesla']
sonuc= liste

# 6. SORU listeye 2 tane araba ekle 

sonuc = liste + ["hundai","Nissan"]

#7. SORU son 2 elamnı siliniz

del liste[-2:]
sonuc= liste

# 8. SORU liste elamanlarını tersten yazdırınız 

sonuc = liste[::-1]

print(sonuc)

# 9. SORU öğrencinin ismini yaşını ve not ortalamsını yazdırm

student = ['abdulkadir','taştemel',2003,[51,85,83]]
ortalama = (student[3][0] + student[3][1] + student[3][2])/3

sonuc2 = f"{2020-student[2]} yaşındaki {student[0]} {student[1]}  isimli öğrencisini not ortalamsı = {ortalama}"

print(sonuc2)