
from types import coroutine


isimler = ["ali","ayşe","fatma","beyza","berke","beyza","beyza"]
years = [1998,1987,1976,2003,2021]

# 1.SORU isimler dizisinin sonuna kadir ismini ekle 

isimler.append("kadir")

# 2. SORU liste başına kadir ismin ekle 
 
isimler.insert(0,'kadir')

# 3. SORU fatma ismini listeden siliniz

isimler.remove("fatma")


# 4.SORU berke liste elmanı mıdır 

contrl = "berke " in isimler

print(contrl)

# 5. SORU liste elmanlarını alfabetik sırlayınız

isimler.sort()

# 6. SORU years elmanlarını alfabeyij sıralayınız 

years.sort()
print(years)

# 7. SORU years kaç tane 2003 ismi vardır

snc = isimler.count(2003)


# 8. SORU isimler ve yearsz elmanarını ters yazdırınız 

isimler.reverse()
years.reverse()


# 8. SORU str="araba", "kamyon" bilgileriniz kullanıcıdan alıp listeye dönüştürünüz

markalar = []
marka = input("marka giriniz = ")

markalar.append(marka)
 
print(markalar)


print(years)
print(isimler)
print(snc)