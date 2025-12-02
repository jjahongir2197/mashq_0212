1 - misol
is_even = lambda x:x % 2 == 0
print(is_even(10))
print(is_even(7))

2 - misol
katta_son = lambda a, b:a if a> b else b
print(katta_son(5, 9))
print(katta_son(12, 96))

3 - misol
uzun_ism = lambda s: len(s) > 7
print(uzun_ism("Ali"))
print(uzun_ism("Jahongir"))

4 - misol
str_uzunliki = lambda s: len(s)
print(str_uzunliki("Salom dunyo"))
print(str_uzunliki("dunyo"))

5 - misol
numbers = lambda x: "nol" if x == 0 else ("musbat" if x > 0 else "manfiy")
print(numbers(19))
print(numbers(-2))
print(numbers(0))
