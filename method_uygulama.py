
# 1.SORU = ' hello world ' yazısının başındaki ve sonodakı boşlukları siliniz

from types import coroutine


s = "**hello world**"
#s = s.lstrip("*")
#s = s.rstrip("*")
s = s.strip("*")
print(s)

# 2. SORU = "www.abdulkadir.com" ifadesinde sadece abdulkadir kalsın

website="www.abdulkadir.com"
a = website.strip("w.com")
print(a)

# 3.SORU = kaç tane a karakteri var

course="www.abdulkadir.com ifadesinde sadece abdulkadir kalsın"
course = course.count("a")
print(course)