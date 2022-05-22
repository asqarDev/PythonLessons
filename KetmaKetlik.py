# Mavzu: Ketma-ketliklar

# 1-misol
# n = int(input("Sonlarni kiriting: "))
# summa = 0
# for i in range(n):
#     son = float(input(">>> "))
#     summa += son
# print(round(summa,2))

# 2-misol
# import random
# n = int(input("n = "))
# multiply = 1
# for i in range(n):
#     son = float(random.randint(1, 23))
#     multiply *= son
#     print(son)
# print(multiply)


# 3-misol
# n = int(input("n = "))
# summa = 0
# multiply = 1
# for i in range(n):
#     a = float(input("sonlarni kiriting: "))
#     summa += a
#     multiply *= a
# print(f"yig'indisi {summa}, ko'paytmasi {multiply}")

# 4-misol
# import random
#
# n = int(input("n = "))
# summa = 0
# for i in range(n):
#     a = random.randint(1, 23)
#     summa += a
#     print(a)
# arifmetik = summa/n
# print("o'rta arifmetigi: ", arifmetik)


# 5-misol
import math

# n = int(input("n = "))
# summa = 0
# lst = []
# for i in range(n):
#     a = float(input("sonlarni kiriting: "))
#     lst.append(int(a))
#     summa += int(a)
# print(lst)
# print(summa)

# 6-misol
# n = int(input("n = "))
# i = 0
# lst = []
# multply = 1
# while n > i:
#     a = float(input("sonlarni kiriting: "))
#     s = (a*10)%10
#     lst.append(int(s))
#     multply *= s
#     i += 1
# print(lst)
# print("kasir ko'paytmalari: ", multply)

# 7-misol

# n = int(input("n = "))
# lst = []
# summa = 0
# for i in range(n):
#     a = float(input("son: "))
#     y = round(a)
#     lst.append(y)
#     summa += y
# print(lst)
# print(summa)

# 8-misol
# n = int(input("n = "))
# lst = []
# count = 0
# for i in range(n):
#     a = random.randint(1, 34)
#     lst.append(a)
#     if a % 2 == 0:
#         count += 1
#         print(a)
# print(count)
# print(lst)

# 9-misol
# n = int(input("n = "))
# count = 0
# for i in range(n):
#
#     a = random.randint(1, 33)
#     if a%2 != 0:
#         print(a)
#         count += 1
# print("toq sonlar miqdori: ", count)

# 10-misol

# n = int(input("n = "))
# for i in range(n):
#     a = random.randint(-23, 23)
#     if a > 0:
#         continue
#     else:
#         print(False)
# 11-misol

# k, n = eval(input("k va n ni kirting: "))
# lst = []
# for i in range(n):
#     a = int(input(" >>> "))
#     lst.append(a)
# print(lst)
# for j in range(len(lst)):
#     if lst[j] < k:
#         print(True)
#
#     else:
#         print(False)
#         break

# 12-misol
# n = int(input("n = "))
# count = 0
# for i in range(n):
#     a = int(input(">>> "))
#     if a > 0:
#         count += 1
#         print(a)
# print("miqdori: ",count)

# 13-misol

# n = int(input("n = "))
# lst = []
# summa = 0
# for i in range(n):
#     a = random.randint(-12, 22)
#     lst.append(a)
#     if a > 0 and a % 2 == 0:
#         summa += a
#     else:
#         print(0)
# print(lst)
# print(summa)

# 2-usul
# i = 0
# summa = 0
# lst = []
# while n > i:
#     a = random.randint(-3, 21)
#     lst.append(a)
#     if a % 2 == 0:
#         summa += a
#
#     i += 1
# print(lst)
# if summa == 0:
#     print(0)
# else:
#     print(summa)

# 14-misol

# k, num = eval(input("k va n >>> "))
# count = 0
# while num != 0:
#     num = int(input("num: "))
#     if k > num and num > 0:
#         count += 1
# print(count)

# 15-misol
# k = int(input("k = "))
# n = int(input("n = "))
# lst = []
# while n != 0:
#     n = int(input("num: "))
#     lst.append(n)
# print(lst)
# count = 0
# for i in range(len(lst)):
#     if lst[i] > k:
#         count += 1
#         print(lst[i])
#         break
#     else:
#         continue
# if count == 0:
#     print(0)
#


# 16-misol
# k = int(input("k = "))
# n = int(input("n = "))
# lst = []
# while n != 0:
#     n = int(input(">>> "))
#     lst.append(n)
# print(lst)
# i = 0
# count = 0
# while len(lst) > i:
#     i += 1
#     if lst[-i] > k:
#         count += 1
#         print(lst[-i])
#         break
#     else:
#         continue
#
# if count == 0:
#     print(0)


# 17-misol
# b = float(input("b = "))
# n = int(input("n = "))
# lst = []
# i = 0
# while n > i:
#     a = float(input(">>> "))
#     lst.append(a)
#     i += 1
# print(lst)
# print(lst.index(b))
# print(lst[lst.index(b):])


# 18-misol
# n = int(input("n = "))
# lst = []
# for i in range(n):
#     lst.append(int(input(">>> ")))
# lst.sort()
# print(lst)
#
# print(set(lst))

# 19-misol
import random
# n = int(input("n = "))
#
# lst = list(random.sample(range(1, 100), n))
# print()
# lst.insert(random.randint(1, n), n)
# print(lst)
# count = 0
# for i in range(n+1):
#     if lst[lst.index(n)-1] > lst[i]:
#         count += 1
#         print(lst[i])
#
# print("miqdori: ", count)

# 2-usul
# n = int(input("n = "))
#
# lst = list(random.sample(range(1, 100), n))
# print(lst)
# count = 0
# for i in range(n-1):
#     if lst[i] < lst[i+1]:
#         count += 1
#         print(lst[i])
# print("count: ", count)

# 20-misol
# n = int(input("n = "))
# lst = list(random.sample(range(1, 100), n))
# print(lst)
# count = 0
# for i in range(n-1):
#     if lst[i] < lst[i+1]:
#         count += 1
#         print(lst[i])
# print("count: ", count)

# 21-misol

# n = int(input("n = "))
# lst = list(random.sample(range(1, 30), n))
# print(lst)
# a = lst.sort()
# if a == lst:
#     print(True)
# else:
#     print(False)

# 22-misol
# n = int(input("n = "))
# lst = list(random.sample(range(1, 30), n))
# print(lst)
# a = sorted(lst,reverse=True)
#
# if lst == a:
#     print(0)
# else:
#     print(1)

# 23-misol
# n = int(input("n = "))
# lst = random.sample(range(1,22), n)
# print(lst)
# count = 0
# for i in range(n-2):
#     if lst[0] < lst[i+1] and lst[i+1] > lst[-1]:
#         count += 1
#     else:
#         continue
#
# if count == n-2:
#     print(0)
# else:
#     print(1)

# 24-misol
# n = int(input("n = "))
# i = 0
# lst = []
# while n > i:
#     a = int(input(">>> "))
#     lst.append(a)
#     i += 1
#
# print(lst)
# if lst.count(0) >= 2:
#     indexes = []
#     for i in range(1, n):
#         if lst[n-i] == 0:
#             print(lst[i])
#             indexes.append(n-i)
#     print(indexes)

# 25-misol



# 26-misol

# k, n = eval(input("k va n ni kiritng: "))
# lst = list(random.sample(range(1, 20), n))
# print(lst)
# for i in range(n):
#     print(pow(lst[i], k))


# 27-misol
# n = int(input("n = "))
# lst = list(random.sample(range(1, 10), n))
# print(lst)
# for i in range(n):
#     x = pow(lst[i], i+1)
#     print(x)

# 28-misol
# n = int(input("n = "))
# lst = list(random.sample(range(1, 10), n))
# print(lst)
# for i in range(n, 0, -1):
#     x = pow(lst[n-i], i)
#     print(x)

# 29-misol
# k, n = eval(input("k va n ni kiriting: "))
# summa = 0
# for i in range(k):
#     lst = list(random.sample(range(1, 12), n))
#     print(lst)
#     summa += sum(lst)
# print("yig'indi: ", summa)

# 30-misol
# k, n = eval(input("k va n ni kiriting: "))
# summa = 0
# for i in range(k):
#     lst = list(random.sample(range(1, 12), n))
#     summa = sum(lst)
#     print(lst, end=" ")
#     print("yig'indisi: ", summa, end=" ")
#     print("\n")

# 31-misol
# k, n = eval(input("k va n ni kiriting: "))
# matrix = []
# for i in range(k):
#     lst = list(random.sample(range(1, 13), n))
#     matrix.append(lst)
# for row in matrix:
#     print(row)
# count = 0
# for i in range(k):
#     if 2 in matrix[i][::]:
#         count += 1
#
# if count > 0:
#     print(count)
# else:
#     print(0)

# 2-usul
# k, n = eval(input("k va n ni kiriting: "))
# summa = 0
# count = 0
# for i in range(k):
#     lst = list(random.sample(range(1, 12), n))
#     print(lst)
#     if 2 in lst[::]:
#         count += 1
#         for j in range(n):
#             if lst[j] == 2:
#                 pass
#             else:
#                 pass
# if count > 0:
#     print(1)
# else:
#     print(0)

# 32-misol
# k, n = eval(input("k va n ni kiriting: "))
# for i in range(k):
#     lst = list(random.sample(range(1, 15), n))
#     print(lst)
#     if 0 or 2 in lst[::]:
#         print(0)
#     else:
#         print(lst[0])

# 33-misol
# k, n = eval(input("k va n ni kiriting: "))
# for i in range(k):
#     lst = list(random.sample(range(1, 15), n))
#     print(lst)
#     if 0 or 2 in lst[::]:
#         print(0)
#     else:
#         print(lst[-1])

# 34-misol
# k, n = eval(input("k va n ni kiriting: "))
# summa = 0
# for i in range(k):
#     lst = list(random.sample(range(1, 14), n))
#     print(lst)
#     if 2 in lst[::]:
#         summa = sum(lst)
#         print(summa)
#     else:
#         print(0)

# 35-misol
k = int(input("k = "))
i = 0
lst = []
for j in range(k):
    while k != 0:
        k = int(input(">>> "))
        lst.append(k)
        i += 1
    print(lst)


# 36-misol






