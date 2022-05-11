
# Mavzu: Fuction amaliy massalalar

# def toliq_fullname(ism, yoshi):
#     """Foydalanuvchini to'liq ism familyasi"""
#     print(f"foydalanuvchi ismi: {ism.title()}\n"
#           f"foydalanuvchi tug'ulgan yili: {int(input('hozirgi yilni kiriting: ')) - yoshi}")
# toliq_fullname(ism = 'Asqar', yoshi=22)

# 2-misol
# def darajaga_oshirish(number):
#     """foydalanuvchi kiritgan sonni kvadrati va kubini hisoblash fucsiyasi"""
#
#     print(f"son {number} ning kvadrati {number**2} va kubi {number**3} ")
# darajaga_oshirish(number = int(input("sonni kiriting: ")))

# 3-misol
# def juft_toq(son):
#     if son % 2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")
# juft_toq(6)

# 4-misol
# def kattasini_top(son1, son2):
#     if son1 > son2:
#         print(son1)
#     elif son1 == son2:
#         print("sonlar teng ")
#     else:
#         print(son2)
# kattasini_top(4, 7)

# 5-misol
# def darajaga_oshirish(x, y):
#     """foydalanuvchidan son olib x darajasida y ni hisoblovchi funksiya"""
#     print(f"natija: {x**y}")
# darajaga_oshirish(4, 7)

# 6-misol
# def daraja(x, y=2):
#     """darajani hisoblovchi funksiya"""
#     print(f"{x} ni {y}-darajasi {x**y}")
# daraja(5, 5)

# 7-misol
# def qoldiqsizbolishni_tekshirish(son):
#     """"""
#     for i in range(2, 11):
#         if son % i == 0:
#             print(f"{son} {i} ga qoldiqsiz bo'linadi")
# qoldiqsizbolishni_tekshirish(70)


# def oraliq(min, max, qadam):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar
#
# print(oraliq(1, 21, 3))

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rang": rangi,
#         "korobka": korobka,
#         "yil": yili,
#         "narh": narhi
#     }
#     return avto
#
# avtolar = []
# while True:
#     print("n\Quyidagilarni kiriting: ")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("model: ")
#     rangi = input("rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("ishlab chiqilgan yili: ")
#     narhi = input("narhi: ")
#
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#
#     javob = input("Yana avto qo'shasizmi? (yes/no) ")
#     if javob == "no":
#         break
# print(avtolar)
# print("Online bozordagi mavjud avto mashinalar")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "nomalum"
#         print(f"{avto['rang'].title()} {avto['model'].title()} {korobka} karobka  Narhi {narhi}")
#

# def fac(a):
#     if a == 0:
#         return 1
#     else:
#         return a*fac(a-1)
# x = fac(5)
# print(x)

# 1-misol
# def sign(x):
#     if x < 0:
#         return -1
#     elif x == 0:
#         return 0
#     elif x > 0:
#         return 1
# a = sign(3)
# b = sign(-3)
# print(a, b)

# 2-misol
# def RootCount(a, b, c):
#     d = b**2-4*a*c
#     if d > 0:
#         return 2
#     elif d == 0:
#         return 1
#     else:
#         return 0
#
# result = RootCount(1, -5, 6)
# result2 = RootCount(1, -4, 4)
# result3 = RootCount(1, 4, 6)
# print(result, result2, result3, end='\n')

# 3-misol
# import math
# def  CircleS(r):
#     return math.pi*r**2
# result = CircleS(10)
# result2 = CircleS(100)
# result3 = CircleS(1)
#
# print(math.floor(result))
# print(result2)
# print(result3)

# 4-misol
# import math
# def RingS(r1, r2):
#     s1 = math.pi*r1**2
#     s2 = math.pi*r2**2
#     return s1-s2
# a = RingS(4, 2)
# b = RingS(2, 1)
# c = RingS(3, 2)
# print(a, b, c, sep='\n')

# 5-misol

# def Range(a, b):
#     sum = 0
#     if a > b:
#         return 0
#     else:
#         while a < b:
#             sum += a
#             a += 1
#         return sum
# result = Range(2, 7)
# result2 = Range(6, 3)
# print(result, result2)

# 6-misol
# def Calc(a, b, op):
#     if op == 1:
#         return a-b
#     elif op == 2:
#         return a*b
#     elif op == 3:
#         return a/b
#     else:
#         return a+b
# result = Calc(6, 3, 1)
# print(result)

# 7-misol
# def Quarter(x,y):
#     if x > 0 and y > 0:
#         return 1
#     elif x < 0 and y > 0:
#         return 2
#     elif x > 0 and y < 0:
#         return 4
#     else:
#         return 3
# result = Quarter(2, 3)
# result2 = Quarter(-2, 3)
# result3 = Quarter(2, -3)
# print(result, result2, result3)

# 8-misol
# def Even(k):
#     return not bool(k%2)
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = 0
# for i in range(10, 100 ):
#     if Even(i):
#         count+=1
# print("count: ", count)


# def Event(k):
#     return not bool(k%2)
# count = 0
# for i in range(1, 11):
#     if Event(i):
#         count += 1
# print(count)

# 9-misol
# import math
# def IsSquare(k):
#     return not bool(math.sqrt(k) % int(math.sqrt(k)))
# count = 0
# for i in range(2, 10):
#     print(i)
#     if IsSquare(i):
#         count += 1
# print("count: ", count)


# 10-misol
import math
import asyncio

# def IsPowerS(k):
#     while k:
#         if k%5:
#             if k!=1:
#                 return False
#             else:
#                 return True
#         k/=5
#     return True
#
# count = 0
# for i in range(1, 12):
#     result =  IsPowerS(i)
#     if result:
#         count += 1
# print(count)


# 11-misol

# def IsPowerN(k, n):
#     while k:
#         if k % n:
#             if k != 1:
#
#                 return False
#             else:
#
#                 return True
#         k /= n
# count = 0
# n = 3
#
# for i in range(1, 11):
#     result = IsPowerN(k=i, n=n)
#     if result:
#         count += 1
# print(count)

# 12-misol
# def IsPrime(n):
#     for i in range(2, n):
#         if n%i != 0:
#             return True
#         else:
#             return False
# count = 0
# for i in range(1, 12):
#     if IsPrime(i):
#         count += 1
# print(count)

# 13-misol

# def DigitCount(k):
#     count = 0
#     while k > 0:
#         count += 1
#         k = k // 10
#     return count
# a = DigitCount(12)
# b = DigitCount(123)
# c = DigitCount(3)
# print(a, b, c)

# print(count)
# k = 12
# count = 0
# while k > 0:
#         count += 1
#         k = k // 10
# print(count)

# 14-misol
# def DigitN(k, n):
#     k = k % 100
#     while k > 0:
#         if k < 10:
#             return -1
#         else:
#             k = k // 10
#             return k
# a = DigitN(234, 2)
# print(a)

#15 -misol

# def Ispalindron(k):
#     temp = k
#     r = 0
#     while k > 0:
#         r = r*10+k%10
#         k//=10
#     return temp==r
#
#
# lst = [123, 22, 101, 21, 64]
# count = 0
# for i in lst:
#     if Ispalindron(i):
#         count += 1
# print(count)

# 16-misol
# def DegToRad(d):
#     r = d * math.pi/180
#     return r
# lst = [0, 90, 180, 360]
# for i in lst:
#     s = DegToRad(i)
#     print(s)

# 17-misol
# def DRadtodeg(r):
#     g = r * 180 / 3.14
#     return g
# lst = [0, 1.57, 3.14, 6.28]
# for i in lst:
#     s = DRadtodeg(i)
#     print(s)

# 18-misol
# def Fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * Fact(n-1)
# for i in range(1, 7):
#     print( f"{i} factarial", Fact(i))

# 19-misol
# def  Fact2(n):
#     if n <= 0:
#         return 1
#     return n * Fact2(n-2)
# lst = [5, 6, 4, 8, 12]
# for item in lst:
#     a = Fact2(item)
#     print(a)


# 20-misol
# def Fib(n):
#     a, b = 1, 2
#     fib = [a, b]
#     for i in range(1, n+1):
#         temp = fib[i - 1] + fib[i]
#         fib.append(temp)
#
#     if fib[n] == fib[i]:
#         return fib[i]
#
# print(Fib(10))

# def Fib(n):
#     a, b = 1, 1
#     fib = [a, b]
#     for i in range(n):
#         a = a + b
#         b = a + b
#         fib.append(a)
#         fib.append(b)
#     print(fib[n-1])
#
# Fib(3)



# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rangi": rangi,
#         "korobka": korobka,
#         "yili": yili,
#         "narhi": narhi
#
#     }
#     return avto
# print("Saytimizdagi avtolar ro'yxatini shakillantiramiz")
# sonlar = []
# while True:
#
#     print("\n Quyidagilarni kiriting: ")
#
#     kompaniya = input("Ishlab chiqaruvchi ")
#     model = input("model ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka ")
#     yili = input("Ishlab chiqarilgan yili ")
#     narhi = input("narhi ")
#
#
#     sonlar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#
#     javob = input("yana avto qo'shasizmi? ")
#     if javob == "no":
#         break
# print(sonlar)
#
# for avto in sonlar:
#      if avto['narhi']:
#          narhi = avto['narhi']
#      else:
#          narhi = "nomalum"
#      print(f"{avto['rangi'].title()} {avto['model'].title()} korobka Narhi: {narhi} ")




# def bahola(isimlar):
#     baholar = {}
#     while isimlar:
#         ism = isimlar.pop()
#         baho = input(f"talab {ism}ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar
# talabalar = ["Ali", "Vali", "Hasan", "Husan"]
# baholar = bahola(talabalar.copy())
# print(baholar)
# print(talabalar)


# def summa(*args):
#     yigindi = 0
#     for i in args:
#         yigindi += i
#     return yigindi
#
# print(summa(12, 23, 34))


# def avto_info(**malumotlar):
#     return malumotlar
# avtolar = avto_info(kompaniya = "GM", model = "Malibu", rangi = "oq", narhi = "23000")
# print(avtolar)

def kopaytma(*sonlar):
    sum = 1
    for i in sonlar:
        sum *= i
    return sum
# print(kopaytma(1, 2, 3, 4, 5))

def talabalar(familya, ism, **malumotlar):
    malumotlar["familya"] = familya
    malumotlar["ism"] = ism
    return malumotlar
# talaba = talabalar("Mirzayev", "Asqar", yoshi = 20, boyi = "1.70", ogirligi = "65")
# print(talaba)











# OOP
# from datetime import datetime
# class Human:
#     def __init__(self, familya, ism, tugulgan_sana):
#         self.familya = familya
#         self.ism = ism
#         self.tugulgan_sana = tugulgan_sana
#     def age(self):
#         year = int(self.tugulgan_sana.split("-")[0])
#         age = int(datetime.now().year) - year
#         return age
# ism = input("ism: ")
# familya = input("familya: ")
# tugulgan_sana = input("tug'ulgan sanasi: ")
# objects = Human(familya, ism, tugulgan_sana)
# print(objects.ism, objects.familya, objects.tugulgan_sana, "yoshi ", objects.age())
# from datetime import datetime
# class Car:
#     def __init__(self, color, name, yili, narhi):
#         self.color = color
#         self.name = name
#         self.yili = yili
#         self.narhi = narhi
#     def chiqqan_yildan(self):
#         yil = int(self.yili)
#         age = int(datetime.now().year) - yil
#         return age
#
# color = input("rangi: ")
# name = input("nomi: ")
# yili = input("yili: ")
# narhi = input("narhi: ")
#
# object1 = Car(color, name, yili, narhi)
# object2 = Car(color, name, yili, narhi)
# a = f"Mashinaning rangi {object1.color} nomi {object1.name} ishlab chiqilgan yili {object1.yili} narxi {object1.narhi}"
# print(a)
# print("hozirgacha ", object1.chiqqan_yildan(), " yil")



























