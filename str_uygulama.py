website ="www.abdulkadir.com.tr"
course = "Sıfırdan İleri Seviye Python Programlama"

#1. soru  = course dizisinde kaç kkaraektert vardır?
uzunkuk = len(course)
print(uzunkuk)
#2. soru = wesite içinden www alın
www = website[:3]
print(www)
#3. soru = websşte içinden com alın
com = website[-6:-3]
print(com)
#4.soru = course içinden ilk 10 ve son 7 karakteri alın
kelime1 = course[:10]
kelime2 = course[-7:]
print(kelime1)
print(kelime2)
#5.soru = course ifadesini tersten yazdırın
ters= course[::-1]
print(ters)

print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")

# 6. SORU = değişkenler ile "benim adım abdulkadşr taştemel yaşım 39 mesleğim mühendislik " yazdırınız

name , surname ,job,  age ="abdulkadir", "taştemel","yazılım",39

#name = input("isminizi  giriniz = ")
#surname = input("soyadınızı giriniz = ")
#age = input("yaşınızı giriniz = ")
#job = input("mesleğinizi giriniz = ")
print(f"benim adım {name} {surname} yaşım {age} mesleğim {job} ")
#print("benim adım {} {} yaşım {} mesleğim {} ".format(name , surname , age , job))

print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")


#7. SORU = 'hello world ifadesindeki w harfiniz W yapınız '
yazı = "hello world"
yazı = yazı[0:4] +" W" + yazı[-4:]
print(yazı)

#8.SORU = abc ifadesini 4 kez yazdırın
sayı = "abc" * 4
print(sayı)