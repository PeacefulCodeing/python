
orenciler = {}

number = input("öğrenci no = ")
name  = input("öğrenci adı = ")
surname = input("öğrenci soyadı = ")
phone = input("öğrenci telefon no = ")

orenciler.update(
    { number :
    {"ad" : name,
    "soyad" : surname,
    "telefon" : phone}
    })

print("*"*60)

ogrNo = input("öğrenci no giriniz = ")

ogrenci = orenciler[ogrNo]


print(f"{ogrNo} lu öğrencinin \nadı = {ogrenci['ad']} \nsoyadı = {ogrenci['soyad']} \ntelefon numarası = {ogrenci['telefon']}" )