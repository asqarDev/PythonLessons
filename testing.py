import random
massiv = ["Asqar", "Muxtor", "Mirzayev", "dklasjf", "Gu'lom aka"]
# sonlar = random.random()
# sonlar = random.uniform(1, 10)
# sonlar = random.randint(1, 67)
# sonlar = random.choice(massiv)
# sonlar = random.choices(massiv, k=10)
# n = int(input("n = "))
# sonlimassiv = list(range(100))
# ran = random.sample(sonlimassiv, n)
# print(ran)

# a = [1, 2, 3, 4, 5, 6, 7]
# # print(random.choice(a))
# random.shuffle(a)
# print(a)


# # 6-misol
# n = int(input("n = "))
# a, b = eval(input("a, b = "))
# sonlar = [a, b]
# uch = a + b
# sonlar.append(uch)
# for i in range(1, n+1):
#     # temp = sonlar[-1]+sonlar[-2]
#     temp = sonlar[-1]+sonlar[-1]
#     sonlar.append(temp)
# print(sonlar)


# 16-misol
# n = int(input("n = "))
# massiv = list(random.sample(range(100), n))
# print(massiv)

# n = int(input("n = "))
# massiv = []
# for son in range(1, n+1):
#     element = int(input(f"{son}" "- elementini kiriting: "))
#     massiv.append(element)
# print(massiv)
# list2 = []
# for i in range(1, (len(massiv))//2+1):
#     list2.append(massiv[i-1])
#     list2.append(massiv[-i])
#
# print(list2)


# # 17-misol
# n = int(input("n = "))
# list = []
# for i in range(1, n+1):
#     element = int(input(f"{i}" "- elementni kiriting: "))
#     list.append(element)
# print(list)
# print(len(list))
# massiv = []
# for son in range(len(list)//4+1):
#     massiv.append(list[2*son])
#     massiv.append(list[2*son+1])
#     massiv.append(list[-1-2*son])
#     massiv.append(list[-2-2*son])
# massiv.pop(-1)
# print(massiv)






import random
# print(random.random())
# print(random.randint(-150, 150))

# print(list(random.sample([12, 2, 3, 4, 5, 6, 90], 3)))
# str = "text"
# print(type(str))
# print(type(list(str)))

# massiv = [12, 2, 3, 4, 5, 6, 7, 8, 11, 14, 31, 22]
# arr = random.choices(massiv, k=10)
# choice = random.choice(massiv)
# print(arr, choice)


# 18-misol
# n = int(input("n = "))
# a = list(random.sample(range(100), n))
# print(a)
# for son in a:
#     if son < a[n-1]:
#         print(son)
#         break
#     else:
#         continue


# a = 7_23
# b = 23_32
# print(a)
# c = a+b
# print(c)


# 19-misol

# n = int(input("n = "))
# a = list(random.sample(range(100), n))
# print(a)
# count = 0
# for i in a:
#     count += 1
#     if a[0] < i and  i < a[n-1]:
#          print(i)
#          print(count)
#          break
#     else:
#         continue


# Anvar Narzullayev darslaridan
# misollar
mevalar = ["olma", "Anor", "nok", "shaftoli", "behi", "olcha"]
narhlar = [1200, 1300, 1500, 1800, 2000, -34, 23.56]
mevalar[0] = "anor"
print(mevalar[0].upper(), mevalar[2].title(), mevalar[1].lower())
print(narhlar)
print(sum(narhlar))
narhlar.reverse()
print(narhlar)

print(len(mevalar))
numbers = list(range(1, 12))
print(numbers)
