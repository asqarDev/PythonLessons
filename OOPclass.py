# Mavzu: OOP // Obyektga yo'naltirilgan dasturlar
# class Person:
#     # yosh = 0
#     # ism = 0
#     familiya = None
#     def __init__(self, viloyat=None, yosh=114, ism=None):
#         self.yosh = yosh
#         self.ism = ism
#         self.viloyat = viloyat
#
#     def __str__(self):
#         return str(self.ism)
#
#     @property
#     def get_name(self):
#         return self.ism
#
# class Student(Person):
#
#     def __init__(self, oliygoh,ism, viloyat):
#         self.oliygoh = oliygoh
#         Person.__init__(self,ism=ism,  viloyat=viloyat)
#         print("init ishladi")
#
#
#
# student1 = Student(ism='Javohr', oliygoh=12, viloyat=True)
# student2 = Student(ism='Rustam', oliygoh=16, viloyat=True)
# print( student2.yosh, student2.ism, student2.viloyat)
# print(student2.get_name)
# print( student1.yosh, student1.ism, student1.viloyat)
# print(student1.get_name)
# # user = Person(ism='Husan')
# # print(user)
# # user2 = Person(yosh=22, ism='Rustam')
# # print(user2)



# x = lambda a, n:a**n
# print(x(3, 5))



# import math
#
# yuza = lambda pi, r : pi*r**2
# print(yuza(math.pi, 2))

# def daraja(n):
#     return lambda x : x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(kvadrat(5))
# print(kub(4))


from math import sqrt
# sonlar = list(range(11))
# ildizlari = list(map(sqrt, sonlar))
# print(sonlar)
# print(ildizlari)
# def daraja2(x):
#     return x*x
# kv = list(map(daraja2, sonlar))
# print(kv)

# kv = list(map(lambda x : x*x, sonlar))
# print(kv)

# a = [2, 4, 5, 7, 8, 4]
# b = [4, 6, 7, 9, 0, 8]
# plus = list(map(lambda x, y : x+y, a, b))
# print(plus)


# import random as r
# sonlar = r.sample(range(100), 10)
# print(sonlar)
# def juftmi(x):
#     return x%2==0
# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)















