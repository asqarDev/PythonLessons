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







