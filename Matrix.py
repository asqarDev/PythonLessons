# Matritsa haqida tushunchalar

# 1. Matritsalarni tashkil etish va ularga qiymatlar kiritish.


# a = [[1,3,5],[2,6,7],[12,45,67]]
# print(a[1][2])


# 1-misol
# m, n = eval(input("Enter matrix number: "))
# massiv = []
# for i in range(1,m+1):
#     massiv.append(i*10)
# # print(massiv)
# matritsa = []
# for col in range(1,n+1):
#     matritsa.append(massiv)
# for i in matritsa:
#     print(i,'\n')


# m, n = eval(input("Enter matrix number: "))

# massiv = []
# matrix = []

# for i in range(0, m):
#     massiv = []
#     for j in range(0, n):
#         massiv.append((i+1)*10)
#     matrix.append(massiv)
# for col in matrix:
#     print(col,'\n')


# 2-misol

# m,n = eval(input("Enter matrix number: "))

# massiv = []
# matrix = []
# for i in range(1,n+1):
#     massiv.append(i*5)
# for j in range(1,n):
#     matrix.append(massiv)
# for row in matrix:
#     print(row,"\n")


# 3-misol

# m,n = eval(input("Enter matrix number: "))

# massiv = []
# matrix = []

# for i in range(1,m+1):
#     element = int(input("number: "))
#     massiv = []
#     for j in range(1,n+1):
#         massiv.append(element)
#     matrix.append(massiv)
# for row in matrix:
#     print(row,'\n')

# 4-misol
# m,n = eval(input("Enter matrix number: "))
# massiv = []
# matrix = []
# for i in range(1, n+1):
#     k = int(input("number: "))
#     massiv.append(k)
# for i in range(1,m+1):
#     matrix.append(massiv)
# for row in matrix:
#     print(row,'\n')

# 5-misol 
# m,n = eval(input("Enter matrix number: "))
# d = int(input("d = "))
# massiv = []
# matrix = []
# for i in range(1,m+1):
#     k = int(input("Enter number: "))
#     massiv = []
#     for j in range(1,n+1):
#         massiv.append(k)
#         k+=d
#     matrix.append(massiv)
# for row in matrix:
#     print(row,'\n')

# 6-misol 

# m,n = eval(input("Matritsa o'lchamini kiriting: "))
# d = int(input("d = "))
# massiv = []
# matrix = []
# for i in range(1,m+1):
#     k = int(input("k massiv elementlari >>> "))
#     massiv = []
#     for j in range(1,n+1):
#         massiv.append(k)
#         k*=d
#     matrix.append(massiv)
# for row in matrix:
#     print(row,'\n')


# 7-misol
import math
import random

# m,n = eval(input("matritsa elementlarini kiriting: "))
# k = int(input("k satirni kiriting: "))
#
# massiv = []
# matrix = []
# for i in range(1, m+1):
#
#     massiv = []
#     for j in range(1,n+1):
#         a = random.randint(1, 23)
#         massiv.append(a)
#     matrix.append(massiv)
#
# for row in matrix:
#     print(row)
#
# print(matrix[k-1], f"{k} - satirdagi element")

# 8-misol
# m, n = eval(input("Enter matrix of number: "))
# k = int(input("Ustun number: "))
#
# massiv = []
# matrix = []
# for index in range(1, m+1):
#     massiv = []
#     for j in range(1, n+1):
#         ustun = random.randint(1, 23)
#         massiv.append(ustun)
#     matrix.append(massiv)
#
# for row in matrix:
#     print(row)
#
# for j in range(m):
#     print(matrix[j][k-1])




# 9-misol
# m, n = eval(input("Enter number of matrix: "))
#
# massiv = []
# matrix = []
# for i in range(1, m+1):
#     massiv = []
#     for j in range(1,n+1):
#         element = random.randint(1,23)
#         massiv.append(element)
#     matrix.append(massiv)
# print(matrix)
# for i in range(m):
#     if i%2 == 0:
#         print("juft satrlar ", matrix[i])

# [[4, 10, 2, 6, 13], [8, 15, 16, 11, 16], [9, 10, 18, 15, 3], [3, 8, 14, 4, 22]]
# juft satrlar  [4, 10, 2, 6, 13]
# juft satrlar  [9, 10, 18, 15, 3]


# 10-misol

# m,n = eval(input("Enter number of matrix: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         ustun = random.randint(1, 24)
#         massiv.append(ustun)
#     matrix.append(massiv)
#
# for row in matrix:
#     print(row)
#
# for row in matrix:
#     for i in range(n):
#         if i % 2 != 0:
#             print(row[i])



# 11-misol
# m,n = eval(input("Number of matrix: "))
# massiv = []
# matritsa = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         element = random.randint(1, 12)
#         massiv.append(element)
#     matritsa.append(massiv)
#
# for row in matritsa:
#     print(row)
#
# print("Natija: ")
# for i in range(m):
#     if i % 2 == 0:
#         print(matritsa[i])
#     else:
#         res = matritsa[i][::-1]
#         print(res)

# 12-misol
# m, n = eval(input("matritsa number: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         k = random.randint(1,23)
#         massiv.append(k)
#     matrix.append(massiv)
#
# for row in matrix:
#     print(row)

# 1-usul
# m = int(input("Matritsani satrlar sonini kiriting = "))
# n = int(input("Matritsani ustunlar sonini kiriting = "))
# matrix = []
# massiv = []
#
# for a in range(n):
#     massiv = []
#     for b in range(m):
#         k = random.randint(0, 100)
#         massiv.append(k)
#     matrix.append(massiv)
# for d in range(n):
#     print("\n", matrix[d])
# for i in range(n):
#     print(matrix[i][0], end=' ')
# print("\n")
# for j in range(n):
#     print(matrix[n-j-1][1], end=' ')

# 2-usul
# m,n = eval(input("matritsa o'lchamlarini kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         k = random.randint(1,100)
#         massiv.append(k)
#     matrix.append(massiv)
#
# for row in matrix:
#     print(row)
# print("Natija \n")
# for i in range(n):
#     if i % 2 == 0:
#         for j in range(m):
#             print(matrix[j][i])
#     else:
#         for j in range(m-1,-1,-1):
#             print(matrix[j][i])






# 13-misol
# m = int(input("Matritsani satrlar sonini kiriting = "))
# matrix = []
# massiv = []
#
# for a in range(m):
#     massiv = []
#     for b in range(m):
#         k = random.randint(0, 100)
#         massiv.append(k)
#     matrix.append(massiv)
# for d in range(m):
#     print("\n", matrix[d])
# x = 0
# print(f"1-satr elementlari - {matrix[0]}\n")
# while x != m:
#     x += 1
#     for i in range(x, m):
#         print(matrix[i][m-x], end=' ')
#     print("\n")
#     for i in range(m-x):
#         print(matrix[x][i], end=' ')
#     print("\n")


# 2-usul
# m = eval(input("Matritsaning o'lchamini kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(m):
#         k = random.randint(1,33)
#         massiv.append(k)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# print("Natija \n")
#
# print("satir ", matrix[0])
# x = 0
# while x != m:
#     x += 1
#     for d in range(x, m):
#         k = matrix[d][m - x]
#         print(k)
#     print('\n')
#     for d in range(m - x):
#         k = matrix[x][d]
#         print(k)
#     print('\n')

# 14-misol
# m = int(input("Matritsaning o'lchamini kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(m):
#         k = random.randint(1, 25)
#         massiv.append(k)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
#
#
# for i in range(m):
#     k = matrix[i][0]
#     print(k,end=" ")
# print("\n")
# x = 0
# while x != m:
#     x += 1
#     for i in range(x, m):
#         k = matrix[m-x][i]
#         print(k,end=" ")
#     print('\n')
#     for i in range(m-x):
#         k = matrix[i][x]
#         print(k,end=" ")
#     print("\n")



# 15-misol
# m = int(input("Matritsaning o'lchovini kiriting: (m - toq son) >>> "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(m):
#         k = random.randint(1, 23)
#         massiv.append(k)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# for i in range(m):
#     k = matrix[0][i]
#     print(k, end=" ")
# print("\n")
#
# x = 0
# while x != m:
#     x += 1
#     for i in range(x, m):
#         k = matrix[i][m - x]
#         print(k, end=" ")
#     print("\n")
#     for i in range(x, m):
#         k = matrix[m - x][m - i - x]
#         print(k, end=" ")
#     print("\n")
#     for i in range(m - x, x, -x):
#         k = matrix[i - x][x]
#         print(k, end=" ")
#     print("\n")
#




# 16-misol







# 2. Matritsa elementlarini tahlil qilish.

# 17-misol
# m, n =eval(input("Matritsaning o'lchamini kiriting: "))
# k = int(input("k - satrni kiriting: "))
#
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         d = random.randint(1, 23)
#         massiv.append(d)
#     matrix.append(massiv)
# for i in matrix:
#     print(i)
# print("Natija \n")
# sum = 0
# kop = 1
# for i in range(m):
#     if k == i+1:
#         print(matrix[i])
#         for j in range(n):
#             sum += matrix[i][j]
#             kop *= matrix[i][j]
#         print("yig'indisi: ", sum)
#         print("ko'paytmasi: ", kop)

# 18-misol
# m, n = eval(input("Matritrsaning o'lchamlarini kiriting: "))
# k = int(input("siz tanlamoqchi bo'lgan ustunni tanlang: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         d = random.randint(1, 25)
#         massiv.append(d)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# print("Natija  \n")
# sum = 0
# kop = 1
# for u in range(m):
#     for e in range(n):
#         if e+1 == k:
#             sum += matrix[u][e]
#             kop *= matrix[u][e]
#             print(matrix[u][e])
# print("sum: ", sum)
# print("kop: ", kop)

# 19-misol
# m, n = eval(input("Matritsa o'lchamini kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         d = random.randint(1, 22)
#         massiv.append(d)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# sum = 0
# for i in range(m):
#     for j in range(n):
#         nat = matrix[i][j]
#         sum += nat
#     print(f"{i+1} satr yigindisi: ", sum)


# 20-misol
# m, n = eval(input("m x n o'lchamli matritsaning m, n ni kiritng:"))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         h = random.randint(1, 89)
#         massiv.append(h)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
#
# x = 0
# sum = 0
# while x != n:
#     for i in range(m):
#         sum += matrix[i][x]
#     x += 1
#     print(f"{x} - ustun yigindisi: ", sum)


# 21-misol
# m, n = eval(input("m x n o'lchamli matritsaning m, n ni kiritng:"))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         h = random.randint(1, 89)
#         massiv.append(h)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# arifmetika = 0
# for i in range(0, m, 2):
#     for j in range(n):
#         e = matrix[i][j]
#         arifmetika += e/n
#     print(f"{i+1}-satr o'rta arifmetigi: ", round(arifmetika,2))

# 22-misol
# m,n  = eval(input("m x n o'lchamli matritsani kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         a = random.randint(1, 34)
#         massiv.append(a)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# x = 1
# sum = 0
# while x-1 != n:
#     for i in range(m):
#         d = matrix[i][x]
#         sum += d
#     print(f"{x+1} ustun yig'indisi: ", sum)
#     x += 2


# 23-misol
# m, n= eval(input("m x n o'lchamli matritsani kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         a = random.randint(1, 34)
#         massiv.append(a)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
#
# for i in range(m):
#     print(min(matrix[i]))

# 24-misol
# m, n = eval(input("Matritsa o'lchamini kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         s = random.randint(1, 122)
#         massiv.append(s)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# x = 0
# ustun = []
# matrix2 = []
# while x != n:
#     ustun = []
#     for j in range(m):
#         e = matrix[j][x]
#         ustun.append(e)
#     matrix2.append(ustun)
#     x += 1
# print("Natija ustunlardagi max  \n")
#
# for i in range(n):
#     print(f"{i+1}-ustun max: ", max(matrix2[i]))


# 25-misol
# m, n = eval(input("m x n o'lchamli matritsani o'lchamlarini kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         a = random.randint(1, 34)
#         massiv.append(a)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# for i in range(m):
#     yigindi = sum(matrix[i])
#     print(f"{i+1} satir yigindisi: ", yigindi)
#

# 26-misol
# m, n = eval(input("m x n o'lchamli matritsani o'lchamlarini kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         a = random.randint(1, 34)
#         massiv.append(a)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# print("Ustunlar ko'paytmasi \n")
# x = 0
# ustun = []
# matritsa = []
# while x != n:
#     ustun = []
#     for i in range(m):
#         u = matrix[i][x]
#         ustun.append(u)
#     matritsa.append(ustun)
#     x += 1
# l = 0
# for i in matritsa:
#     l += 1
#     def multiply(i):
#         result = 1
#         for x in i:
#             result = result * x
#         return result
#
#     print(f"{l} ustun elemenlari ko'paytmasi: ",multiply(i))

# 27-misol

# m, n = eval(input("m x n matritsaning o'lchamini kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         q = random.randint(1, 34)
#         massiv.append(q)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# print("Ustundan maxni topish \n")
# x = 0
# ustun = []
# matritsa = []
# while x != n:
#     ustun = []
#     for i in range(m):
#         f = matrix[i][x]
#         ustun.append(f)
#     x += 1
#     matritsa.append(ustun)
# max_ustun = []
# for i in range(n):
#     h = max(matritsa[i])
#     max_ustun.append(h)
# print(max_ustun)
# print("min: ", min(max_ustun))


# 28-misol

# m, n = eval(input("Matritsaning o'lchamini kiriting: "))
# massiv = []
# matrix = []
# for i in range(n):
#     massiv = []
#     for j in range(m):
#         k = random.randint(1, 45)
#         massiv.append(k)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
#
# print("Natija: \n")
# l = []
# for min_s in matrix:
#     l.append(min(min_s))
# print(max(l))

# 29-misol
# m, n = eval(input("Matritsaning o'lchamini kiriting: "))
# massiv = []
# matrix = []
# for i in range(n):
#     massiv = []
#     for j in range(m):
#         k = random.randint(1, 45)
#         massiv.append(k)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
# count = 0
# for i in range(n):
#     w = sum(matrix[i])/m
#
#     for j in range(m):
#
#         if w > matrix[i][j]:
#             count += 1
#             print("kichik qiymatlar: ", matrix[i][j])
#             print("soni: ", count)
#
#     print(f"{i+1} start o'rta arifmetigi: ", w)

# 2-usul
# ????



# 30-misol
# m, n = eval(input("Matritsaning o'lchamini kiriting: "))
# massiv = []
# matrix = []
#
# for i in range(n):
#     massiv = []
#     for j in range(m):
#         k = random.randint(1, 45)
#         massiv.append(k)
#     matrix.append(massiv)
# for row in matrix:
#     print(row)
#
#
# print("Natija >>> \n")
# ustun_list = []
# matritsa = []
# for i in range(m):
#     ustun_list = []
#     for j in range(n):
#         ustun_list.append(matrix[j][i])
#     matritsa.append(ustun_list)
# summa = 0
# print(matritsa)
# for i in range(m):
#     arifmetika = sum(matritsa[i])/n
#     for j in range(n):
#         if arifmetika <= matritsa[i][j]:
#             print(matritsa[i][j])
#
#     print("O'rta arifmetigi: ", arifmetika)

# 31-misol
m, n = eval(input("Matritsaning o'lchamini kiriting: "))
massiv = []
matrix = []
for i in range(m):
    massiv = []
    for j in range(n):
        g = random.randint(1, 45)
        massiv.append(g)
    matrix.append(massiv)
for row in matrix:
    print(row)
summa = 0
for i in range(m):
    arifmetik = sum(matrix[i])/n
    summa += arifmetik
print("O'rta arifmetik: ", summa)
b = []
for i in range(m):
    b = []
    for j in range(n):
        b.append(abs(matrix[i][j] - summa))
    for f in range(n-1):
        if b[i] > b [i+1]:
            print(matrix[i][j])