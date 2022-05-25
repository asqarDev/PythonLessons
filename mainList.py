# Mavzu: Bir o‘lchovli massivlar. Bir o‘lchovli massivlarni tashkil etish va ularga qiymatlar  kiritish.

# 1-misol
# n=eval(input('n = '))
# i=0
# list=[]
# while 2*n>i:
#     i+=1
#     if i%2!=0:
#         list.append(i)
#         print(list)


# 2-misol
# n=int(input("n = "))
# list=[]
# for i in range(1,n+1):
#     natija=pow(2,i)
#     list.append(natija)
# print(list)


# 3-misol
# n,a,d=eval(input("n,a,d = "))
# list=[]
# for i in range(1,n+1):
#     an=a+(i-1)*d
#     list.append(an)
# print(list)

# 4-misol
# n,b,q=eval(input("n,b,q = "))
# list=[]
# for i in range(1,n+1):
#     bn=b*pow(q,i-1)
#     list.append(bn)
# print(list)


# 5-misol
# n=int(input("n = "))
# massiv=[1,1]
# for i in range(3,n+1):
#     massiv.append(massiv[i-2]+massiv[i-3])
# print(massiv)


# 6-misol
# n,a,b = eval(input("n,a,b = "))
# list=[a,b]
# list.append(a+b)
# print(list)
# for i in range(2,n):
#     list.append(list[i]+list[i])
# print(list,i)


# 7-misol
# n=eval(input('n = '))
# list=[]
# massiv2=[]
# for i in range(1,n+1):
#     massiv=eval(input('massiv elemanti '))
#     list.append(massiv)
# print(list)

# for i in range(1,len(list)+1):
#     nex=list.pop()
#     massiv2.append(nex)
# print(massiv2)


# 8-misol
# n=eval(input("n = "))
# list=[]
# list2=[]
# for i in range(1,n+1):
#     element=int(input("massiv elemantlarini kiriting: "))
#     list.append(element)
# list.sort()
# print(list)
# for x in list:
#     if x%2==0:
#         list2.append(x)
# list2.sort(reverse=True)
# print(list2)
# print("soni: ",len(list2))

# 9-misol
# n=eval(input('n = '))
# list=[]
# for i in range(1,n+1):
#     elemen=eval(input('elemantni kiriting: '))
#     list.append(elemen)

# print(list)
# print(len(list))
# list2=[]
# i=0
# while len(list)>i:
#     if i%2!=0:
#         list2.append(list[i])
#     i+=1;
# print(list2)
# print("soni: ",len(list2))


# 10-misol

# n=eval(input("n = "))
# list=[]
# for i in range(1,n+1):
#     new=eval(input('massiv elementini kiriting: '))
#     list.append(new)
# print(list)
# print("massiv elementlar soni: ",len(list))
# list1=[]
# list2=[]
# i=1
# while len(list)+1>i:

#     if list[i-1]%2!=0:
#         list1.append(i)
#         list1.sort(reverse=True)
#     else:
#         list2.append(i)
#         list2.sort()
#     i+=1
# print("juft no'merdagi massiv index ",list2)
# print("toq no'merdagi messivlarni index ",list1)


# 11-misol

# n,k=eval(input("n,k = "))
# list1=[]
# list2=[]
# for i in range(1,n+1):
#     list1.append(i)
# list2=list1[k:0:-1]
# print(list2)
# list2=list[:k ]
# list2.sort(reverse=True)
# print(list2.count(2))


# 12-misol
# n=eval(input('n = '))
# a=[]
# for i in range(1,n+1):
#     a.append(i)
# print(a)
# b=a[1:n:2]
# print(b)

# 13-misol
# n=eval(input('(toq son kiriting: ) n = '))
# a=[]
# for i in range(1,n+1):
#     a.append(i)
# print(a)
# b= a[n::-2]
# print(b)

# 14-misol
# n=int(input('n = '))
# a=[]
# for x in range(0,n,1):
#     a.append(x)
# print(a)
# a1=a[x::-2]
# a2=a[x-1::-2]
# print(a1,a2)

# 15-misol
# n=int(input('n = '))
# a=[]
# for i in range(1,n+1):
#     a.append(i)
# print(a)
# a1=a[n-2::-2]
# a2=a[n-1::-2]
# print(a1)
# print(a2)

# 16-misol
# n=int(input('n = '))
# a=[]
# for i in range(1,n+1):
#     element=eval(input(f"{i} " '- massiv elementini kiriting: '))
#     a.append(element)
# print(a)
# b=[]
# for x in range(len(a)//2):
#     b.append(a[x])
#     b.append(a[-x-1])
# print(b)


# 17-misol

# n = eval(input("(n juft son) n = "))
# a = []
# for i in range(1, n + 1):
#     elemnt = int(input(f"{i} " "-element "))
#     a.append(elemnt)
# print(a)

# b=[]
# for x in range(len(a)//4+1):
#     b.append(a[2*x])
#     b.append(a[2*x+1])
#     b.append(a[-1-2*x])
#     b.append(a[-2-2*x])

# b.pop(-1)
# b.pop(-1)
# print(b)


# 2. Massiv elementlarini tahlil qilish

# 18-misol
# import random
#
# n = int(input("n = "))
# sonlar = list(random.sample(range(100), n))
# print(sonlar)
# for son in sonlar:
#     if son < sonlar[n-1]:
#         print(son, "nima")
#         break
#     else:
#         continue


# n = int(input("n = "))
# massiv = []
# for i in range(1, n+1):
#     element = int(input(f"{i}" "- massiv elementini kiriting: "))
#     massiv.append(element)
# print(massiv)
#
# for son in massiv:
#     if son < massiv[n-1]:
#         print(son)
#         break
#     else:
#         continue


# 20misol
# import random
#
# n = int(input("n = "))
# a = list(random.sample(range(100), n))
# k, l = eval(input("k va l ni kiriting: "))
# print(a)
# if (1<=k and k <= l and l <= n):
#     for i in a:
#         massiv = a[k:l+1]
#     print(sum(massiv))
# else:
#     print("Sorry, No")

# n = int(input("n = "))
# a = []
# k, l = eval(input("k va l ni kiriting: "))
# for i in range(1,n+1):
#     massiv = int(input("elemantini kiriting: "))
#     a.append(massiv)
# print(a)
# for x in a:
#     if 1<=k and k <= l and l <= n:
#         list2 = a[k-1:l]
#         print(sum(list2))
#         break
#     else:
#         continue



# 21-misol
# n, k, l = eval(input("n, k, l = sonlarini kiriting: "))
# a = []
# for i in range(n):
#     element = int(input("elemenitini kiriting: "))
#     a.append(element)
# print(a)
#
# for x in a:
#     if 1 <= k and k <= l and l <= n:
#         sonlar = a[k-1:l]
#         print(sum(sonlar)/(l-k+1))
#         break
#     else:
#         continue
import math
import random

# n, k, l = eval(input("n, k, l = "))
# sonlar = list(random.sample(range(10), n))
# print(sonlar)
# for son in sonlar:
#     if 1<=k and k<=l and l<=n:
#         a = sonlar[k-1:l]
#         print(sum(a)/(l-k+1))
#         break
#     else:
#         continue

# 22 - misol
# n, k, l = eval(input("n, k, l = "))
# lst = list(random.sample(range(10), n))
# print(lst)
# a = lst[k:l+1]
# print(a)
# c = sum(lst)-sum(a)
# print(c)


# 23-misol
# n, k, l = eval(input("n, k l ni kiriting: "))
# a = []
# for i in range(n):
#     lst = int(input("elementini kiriting: "))
#     a.append(lst)
# print(a)
# list2 = a[k-1:l]
# print(sum(list2))
# natija = sum(a)-sum(list2)
# print(natija/(l-k+1))

# 24-misol
# n = eval(input("n = "))
# a = []
# for x in range(n):
#     element = eval(input("elementni kiriting: "))
#     a.append(element)
#
# print(a)
# k = 0
# while len(a) > 0:
#     a1=a.pop()
#     print(a1)


# 26-misol
# n = int(input("n = "))
# lst = []
# for i in range(n):
#     a = int(input("list elementi "))
#     lst.append(a)
# print(lst)
# a = len(lst)
# # print(a)
# count = 0
# for i in lst:
#     # print(i)
#     count += 1
#     if i % 2 == 0:
#         pass
#     elif i % 2 != 0:
#         pass
#     else:
#         print("buzulgan elementni tartib npmeri => ", i+1)
#         break
#     if count == len(lst):
#         print(0)


# 24-misol
# n = int(input("n = "))
# a = []
# for i in range(n):
#     element = eval(input(f"{i}" " - elementi "))
#     a.append(element)
# print(a)
# for i in range(len(a)):
#     # print(i)
#     if a[i+1]-a[i] == a[-1]-a[-2]:
#         print(a[-1]-a[-2])
#         break
#     else:
#         print(0)
#         break


# 25-misol

# n = int(input("n = "))
# lst = []
# for son in range(n):
#     a = int(input(f"{son}" "-elementi "))
#     lst.append(a)
# print(lst)
# for i in range(len(lst)):
#     if lst[i+1]/lst[i] == lst[-1]/lst[-2]:
#         q = lst[-1]/lst[-2]
#         print(q)
#         break
#     else:
#         print(0)
#         break

# 26-misol


# 27-misol
# n = int(input("n = "))
# a = []
# for i in range(n):
#     el = int(input(f"{i}" "-elementini kiriting: "))
#     a.append(el)
# print(a)
#
# for x in range(len(a)):
#     if a[x] > 0 and a[x+1] < 0 and a[-1] > 0:
#         print(0)
#         break
#     elif a[x] < 0 and a[x+1] > 0 and a[-1] < 0:
#         print(0)
#         break
#     else:
#         print("buzulgan tartib nomeri ", x)
#
#     if x == len(a)-1:
#         print(0)
#         break

# 28-misol
# n = int(input("n = "))
# massiv = list(random.sample(range(10), n))
# print(massiv)
# a = massiv[:n:2]
#
# print(min(a))

# 29-misol
# n = int(input("n = "))
# lst = list(random.sample(range(10), n))
# print(lst)
# a = lst[1:n:2]
# print(max(a))

# 30-misol

# n = int(input("n = "))
# # a = list(random.sample(range(10), n))
# a = []
# for i in range(n):
#     b = int(input(f"{i}" "-element "))
#     a.append(b)

# print(a)

# for i in range(len(a)):
#     if a[i] == n:
#         print(i+1)
#         break
#     elif a[i+1] <= n:
#         print(i+1)
#     elif a[i] == a[-i]:
#         print(i+1)
#     else:
#         continue



# 32-misol
# n = int(input('n = '))
# a = list(random.sample(range(10), n))
# print(a)
# lst_mins = []
# for i in range(len(a)-2):
#
#     if a[i] > a[i+1] and a[i+1] < a[i+2]:
#         print(a.index(a[i+1]))
#         lst_mins.append(a[i+1])
#         break
#     else:
#         continue


        


# 33-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
#
# for i in range(len(a)-2):
#     if a[i] < a[i+1] and a[i+1] > a[i+2]:
#         print(f"{a.index(a[i+1])}-index", a[i+1])
#     else:
#         continue




# for i in range(len(a)//2):
#     if a[i] > a[i+1] and a[i+1] < a[i+2]:
#         print(a.index(a[i+1]))

#     else:
#         continue
# else:
#     print("shart bo'yichamas! ")


# 34-misol
#
# n = int(input("n = "))
# a = list(random.sample(range(100), n))
# lst_main = []
# for i in range(len(a)-2):
#     if a[i] > a[i+1] and a[i+1] < a[i+2]:
#         lst_main.append(a[i+1])
#     else:
#         continue
# if len(lst_main) > 0:
#     print(a)
#     print(lst_main)
#     print(max(lst_main))
# else:
#     print(0)


# 35-misol
# n = int(input("n = "))
# a = list(random.sample(range(100), n))
# print(a)
# lst_a = []
# for x in range(len(a)-2):
#     if a[x] < a[x+1] and a[x+1] > a[x+2]:
#         print(f"{x+1}-index ", a[x+1])
#         lst_a.append(a[x+1])
#     else:
#         continue
# if len(lst_a) > 0:
#     print(lst_a)
#     print(min(lst_a))
# else:
#     print(0)




# 36-misol
# n = int(input('n = '))
# a = list(random.sample(range(100), n))
# lst1 = []
# lst2 = []
# print(a)
#
# for i in range(1, len(a)-1):
#     # print(i)
#     if a[i] > a[i-1] and a[i] > a[i+1]:
#         temp = a.pop(i)
#         lst2.append(temp)
#         print("local max: ", lst2)
#     elif a[i] < a[i-1] and a[i] < a[i+1]:
#         temp2 = a.pop(i)
#         lst1.append(temp2)
#         print("local min: ", lst1)
#
#     else:
#         continue
# print("qolgan list: ", a)




# for i in range(len(a)-2):
#     if a[i-1] < a[i]  and a[i] < a[i+1]:
#         # lst1.append(a[i+1])
#         # print(i, i+1, i+2)
#         print('local min: ', a.pop(i+1))
#     if a[i] > a[i - 1] and a[i] > a[i + 1]:
#         # lst2.append(a[i+1])
#         print('local max:', a.pop(i+1))
#         # del a[i+1]
# # for i in range(len(a) - 2):
# #     if a[i] > a[i-1] and a[i] > a[i+1]:
# #         # lst2.append(a[i+1])
# #         print('local max:', a.pop(i+1))
# #         # del a[i+1]
#
# print(a, max(a), min(a))
# # if len(lst2) > 0 or len(lst1) > 0:
# #     print("local max ", lst1, ",\nlocal min ", lst2)
# # else:
# #     print(0)






# 37-misol
# n = int(input("n = "))
# a = list(random.sample(range(100), n))
# print(a)
#
# count = 0
# step = 0
# for i in range(len(a)):
#     for j in range(i, len(a)-1):
#         if a[j] < a[j+1]:
#             step += 1
#             continue
#         elif step > 0:
#             step = 0
#             i = j+1
#             count += 1
#             break
#         elif step == 0:
#             i = j + 1
#             break
# print("resultat: ", count)




# 37

# count, step = 0, 0
# n = 10
# lst = random.sample(range(100), n)
#
# print("lst:", lst)
#
# for i in range(len(lst)):
#     # print("i:  ", i)
#     for j in range(i, len(lst)-1):
#         if lst[j] < lst[j+1]:
#             step += 1
#             continue
#         elif step > 0:
#             step = 0
#             i = j+1
#             count += 1
#             break
#         elif step == 0:
#             i = j+1
#             break
# print("Resultat", count)

# 38-misol
# n = int(input("n = "))
# lst = list(random.sample(range(100), n))
# print(lst)
# step = 0
# count = 0
# for i in range(len(lst)):
#     for j in range(i, len(lst)-1):
#
#         if lst[j] > lst[j+1]:
#             step += 1
#             continue
#         elif step > 0:
#             step = 0
#             i = j+1
#             count += 1
#             break
#         elif step == 0:
#             i = j+1
#             break
# print("result: ", count)




# 39-misol
# n = int(input("n = "))
# a = list(random.sample(range(100), n))
# print(a)
# step = 0
# count = 0
# for i in range(len(a)):
#     for j in range(i, len(a)-1):
#         if a[j] < a[j+1] or a[j] > a[j+1]:
#             step += 1
#
#         if step > 0:
#             step = 0
#             i = j+1
#             count += 1
#             break
#         if step == 0:
#             i = j+1
#             break
# print("Result", count)

# 40-misol

# print(math.floor(3.2))
# print(math.ceil(3.2))
# print(round(3.6))

# r, n = eval(input("r va n ni kiriting: "))
# lst = list(random.sample(range(10), n))
# print(lst)
# a = []
# for i in lst:
#
#     a.append(abs(i-r))
# print(a)
# for x in range(1, len(a)+1):
#     if min(a) == a[x-1]:
#         print(lst[x-1])
#
# print(min(a))

# 41-misol
# n = int(input("n = "))
# # a = list(random.sample(range(10), n))
# # print(a)
# b = list(random.choices(range(10), k=n))
# print(b)
# lc = []
# for i in range(len(b)-2):
#     if b[i] + b[i+1] > b[i+1] + b[i+2]:
#         lc.append(b[i] + b[i+1])
#         print("yonma yon elementlar yig'indisi: ", b[i]+b[i+1], "\tindex: ", i, i+1)
#     elif b[i]+b[i+1] < b[i+1] + b[i+2]:
#         lc.append(b[i+1]+b[i+2])
#         print("yonma yon elementlar yig'indisi:", b[i+1]+b[i+2], "\tindex: ", i+1, i+2)
#     else:
#         continue
#
# print(lc)
# print(f"{n} o'lchamli masivning eng katta 2 ta yonma yon massiv elementlari yig'indis: ", max(lc))


# 42-misol
# r, n = eval(input("r va n ni kiriting: "))
# massiv = list(random.choices(range(10), k=n))
# print(massiv)
# a = []
# for i in range(len(massiv)-1):
#     a.append(abs(massiv[i]+massiv[i+1]-r))
# print(a)
#
# for i in range(len(a)):
#     if min(a) == a[i]:
#         print(massiv.index(massiv[i]), massiv.index(massiv[i])+1, end=" , ")




# for i in range(len(massiv)-2):
#     if abs(massiv[i]+massiv[i+1]-r) > abs(massiv[i+1]+massiv[i+2]-r):
#         print("index: ", i+1, i+2)
#     elif abs(massiv[i] + massiv[i+1] - r) < abs(massiv[i+1] + massiv[i+2] - r):
#         print("index: ", i, i+1)
#     else:
#         continue

# 43-misol
# n = int(input("n = "))
# a = list(random.choices(range(10), k=n))
# a.sort()
# print(a)
# print("toq indexdagi elementlar: ", a[1::2])
# a.sort(reverse=True)
# print(a)
# print("toq indexdagi elementlar: ", a[1::2])


# 44-misol
# 1-usul
# n = int(input("n = "))
# a = list(random.choices(range(10), k=n))
# print(a)
# for i in range(len(a)):
#     if i > 1 and a[i] in a[:i]:
#         continue
#     else:
#         index = i
#         for j in a[i:]:
#             if j in a[i+1:]:
#                 if j == a[i]:
#                     print(index, end=" , ")
#             index += 1

# 2-usul
# n = int(input("n = "))
# a = list(random.choices(range(10), k=n))
# print(a)
# for i in range(len(a)):
#     # print(a.count(a[i]))
#     if a.count(a[i]) > 1 and a[i] in a[:i+1]:
#         print(a[i], f', {a.count(a[i])}' " marta takrorlangan element ")
#         print("index: ", i)
#
#     else:
#         continue


# 45-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# temp = []
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         temp = (abs(a[i]-a[j]))
#
# print(temp)





# 46-misol
# r, n = eval(input('r va n ni kiriting: '))
# a = list(random.sample(range(10) ,n))
# print(a)
# temp = []
# for i in range(len(a)-1):
#     temp.append(abs(a[i]+a[i+1]-r))
# print(temp)
# for i in range(len(a)-1):
#     if min(temp) == temp[i]:
#         print("index: ", a.index(a[i]), a.index(a[i+1]))





# 47-misol
# n = int(input("n = "))
# a = list(random.choices(range(10), k=n))
# print(a)
# count = 0
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         count += 1
#
#     else:
#         continue
# print(count)

# 48-misol
# n = int(input("n = "))
# a = list(random.choices(range(10), k=n))
# print(a)
# for i in range(len(a)-1):
#     if a.count(a[i]) != 1:
#         if a.count(a[i]) < a.count(a[i+1]):
#             print("index: ", i+1, " , ", a.count(a[i+1]), " marta takrorlangan")
#         elif a.count(a[i]) >= a.count(a[i+1]):
#             print("index: ", i, " , ", a.count(a[i]), " marta takrorlangan ")
#
#
#     else:
#         continue


# 49-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# for i in range(len(a)):
#     if a[i] not in range(1, n+1):
#         print("index: ", a.index(a[i]))
#         break
#     if a.index(a[i]) == n-1:
#         print(0)


# 50-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# inv_count = 0
# # for i in range(len(a)-1):
# for i in range(n):
#     for j in range(i + 1, n):
#         if (a[i] > a[j]):
#             inv_count += 1
#
# print(sorted(a))
# print(inv_count)











# Mavzu: 3. Bir necha massivlar bilan ishlash

# 51-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# b = list(random.sample(range(10), n))
# print(f"a = {a} \nb = {b}")
#
# for j in range(n):
#     if a[j] == b[j]:
#         count = j
# a.pop(count)
# b.pop(count)
# print(a)
# print(b)
# for i in range(len(a)):
#     a[i] = b[i]+a[i]
#     b[i] = a[i]-b[i]
#     a[i] = a[i]-b[i]
#
# print(f'a = {a} \nb = {b}')

# 52-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# b = []
# for i in range(n):
#     if a[i] < 5:
#         b.append(a[i]*2)
#     else:
#         b.append(a[i]/2)
# print(b)


# 53-misol
# n = int(input("n = "))
# a = list(random.sample(range(100), n))
# b = list(random.sample(range(100), n))
# c = []
# print(a)
# print(b)
# for i in range(len(a)):
#     if a[i] > b[i]:
#         c.append(a[i])
#     else:
#         c.append(b[i])
# print(c)


# 54-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# b = []
# for i in range(len(a)):
#     if a[i]%2 == 0:
#         b.append(a[i])
# print("uzunligi ", len(b), b)

# 55-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# print("uzunligi: ", len(a[1::2]))
# print(a[1::2])

# 56-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# print("uzunligi: ", len(a[3::3]), a[3::3])


# 57-misol

# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# b = a[::2] + a[1::2]
#
# print(b)


# 58-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# b = []
# temp = 0
# for i in range(len(a)):
#     temp += a[i]
#     b.append(temp)
# print(b)


# 59-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# temp = 0
# b = []
# count = 0
# for i in range(len(a)):
#     count += 1
#     temp += a[i]
#     b.append(temp/count)
# print(b)


# 60-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# temp = 0
# y = sum(a)
# b = []
# for i in range(len(a)):
#     b.append(y)
#     y -= a[i]
# print(b)


# 61-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# print(a)
# b = []
# yig = sum(a)
# for i in range(len(a)):
#     b.append(yig/(n-i))
#     yig -= a[i]
# print(b)

# 62-misol
# n = int(input("n = "))
# a = list(random.sample(range(-10, 10), n))
# print(a)
# b = []
# c = []
# for i in range(len(a)):
#     if a[i] > 0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
# print("uzunligi ", len(b), b)
# print("uzunligi ", len(c), c)



# 63-misol
# n = int(input("n = "))
# a = list(random.sample(range(30), n))
# b = list(random.sample(range(30), n))
# a.sort()
# b.sort()
# print(a)
# print(b)
# c = a + b
# c.sort()
# print(c)


# 64-misol
# n = int(input("n = "))
# a = list(random.sample(range(10), n))
# b = list(random.sample(range(20), n))
# c = list(random.sample(range(30), n))
# a.sort(reverse=True)
# b.sort(reverse=True)
# c.sort(reverse=True)
# print(a)
# print(b)
# print(c)
# d = a + b + c
# print(sorted(d))


# 12-misol matritsadan
# m,n = eval(input("matritsa o'lchamlarini kiriting: "))
# massiv = []
# matrix = []
# for i in range(m):
#     massiv = []
#     for j in range(n):
#         d = random.randint(1, 21)
#         massiv.append(d)
#     matrix.append(massiv)
# print(matrix)
# x = 0
# while x != 0:
#     for d in range(m):
#         k = matrix[d][x]
#         print(k)
#     for d in range(m):
#         k = matrix[m - 1 - d][x]
#         print(k)
#     x += 1
# for i in range(n):
#     if i%2==0:
#         for j in range(m):
#             print(matrix[j][i], end=" ")
#     else:
#         for j in range(m-1, -1, -1):
#             print(matrix[j][i], end=" ")
#     print('\n')








