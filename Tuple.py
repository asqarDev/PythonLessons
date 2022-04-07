# Mavzu: Tuple

# 1-misol
# import random
#
# n = int(input("n = "))
# x = tuple(random.sample(range(12), n))
# print(x)


# 2-misol
# n = int(input("n = "))
# a = []
# for i in range(n):
#     a.append(int(input("elementini kiriting: ")))
# b = tuple(a)
# print(b)
# print("max:", max(b), "min", min(b), "summa:", sum(b), end=" ")

# 3-misol
# import random
# n = int(input("n = "))
# tpl = tuple(random.sample(range(10), n))
# print(tpl)
# print(tpl[0:2])

# 5-misol
import random

# n = int(input("n = "))
# tpl = tuple(random.sample(range(12), n))
# print(tpl)
# a = list(tpl)
# print(a)
# a.append(int(input("element kiriting: ")))
# print(a)


# 6-misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(21), n))
# print(tpl)

# 7-misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(21), n))
# print(tpl)
# print("boshidan 4- element: ", tpl[4])
# print("oxoridan 4-element: ", tpl[-4])

# 8-misol
# from copy import deepcopy
# tpl = ("hello", 34, [], True, {})
# print(tpl)
# tuplex_colon = deepcopy(tpl)
# tuplex_colon[2].append(int(input("a = ")))
# print(tuplex_colon)
# print(tpl)

# 9-misol
# n = int(input("n = "))
# tpl =  tuple(random.choices(range(21), k=n))
# print(tpl)
# for i in range(n):
#     for j in range(i+1, n):
#         if tpl[i] == tpl[j]:
#             print(tpl[j])

# 10-misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(21), n))
# print(tpl)
# if len(tpl) > 0:
#     print(True)
# else:
#     print(False)


# 11-misol
# n = int(input("n = "))
# lst = list(random.sample(range(20), n))
# tpl = tuple(lst)
# print(tpl)

# 12-misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(20, 45), n))
# print(tpl)
# lst = list(tpl)
# a = int(input("nechta elementni olmoqchisiz a = "))
# for i in range(a):
#     lst.pop(int(input("indexsini kiriting: ")))
# tpl = tuple(lst)
# print(tpl)

# 13-misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(21), n))
# lst = list(tpl)
# print(tpl)
# tpl = lst[int(input("dastlabki elementni kiriting: ")):int(input("oxirgi lelementni kiritin:"))]
# tpl = tuple(tpl)
# print(tpl)


# 14-misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(30), n))
# print(tpl)
# index = tpl.index(int(input("qaysi elementni kiritmoqchisiz! ")))
# print("index: ", index)

# 15-misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(20), n))
# print(tpl)
# print("uzunligi: ", len(tpl))

# tuplex = tuple("3ewkslfsdkjflshjglgfh;df")
# print(tuplex)
# print(len(tuplex))


# 16-misol
# tpl = (("key", 3),("qwerty", 34))
# print(tpl)
# dictionars = dict(tpl)
# print(dictionars)

# 17-misol
# tpl = [(1,2,3),(4,2,6),(7,9,5)]
# print(list(zip(*tpl)))


# 18-misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(20), n))
# print(tpl)
# lst = list(tpl)
# lst.sort(reverse=True)
# tpl = tuple(lst)
# print(tpl)



# 19-misol
# tpl = ((2, "w"), ("qwerty", 23), ("sgsh", 33))
# print(tpl)
# dic = dict(tpl)
# print(dic)

# tpl = [("x", 3), ("x", 4), ("f", 23),("d", 222), ("f" ,56), ("k", 34), ("k", 3), ("a", 888)]
# d = {}
# for a, b in tpl:
#     d.setdefault(a, []).append(b)
#     print(a)
#     print(b)
# print(d)


# 21-misol

# n = int(input("n = "))
# lst = []
# for i in range(1, n+1):
#
#     tpl = tuple(random.sample(range(1, 30), 3))
#     lst.append(tpl)
# print(lst)
# lst_item = []
# for x in lst:
#     lst_item.append(list(x))
# print(lst_item)
# rslt = []
# for item in lst_item:
#     item[2] = int((input("sadhlska ")))
#     rslt.append(tuple(item))
# print(rslt)

# 22-misol
# tpl = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# print(tpl)
# lst = []
# for item in tpl:
#     lst.append(list(item))
#
# tpl_item = []
# for item in lst:
#     if len(item) > 0:
#         tpl_item.append(tuple(item))
#
# print(tpl_item)

# 23-misol
# tpl = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# print(tpl)
# tpl.sort(reverse=True)
# print(tpl)

# 24-misol
# numbers = [12, 34, 45, 10, (12, 43), 987]
# print(numbers)
# count = 0
# for item in numbers:
#     if type(item) != int:
#         break
#     else:
#         count += 1
# print(count)

# 25-misol
# string = "python 3.0"
# tpl = tuple(string)
# print(tpl)


# 26-misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(-10, 10), n))
# print(tpl)
# print("summa: ", sum(tpl))
# sum = 1
# for item in tpl:
#     sum *= item
# print(sum)


# 27-misol
# n = int(input("n = "))
# tpl_item = []
# for i in range(n):
#     tpl = tuple(random.sample(range(100), n))
#     tpl_item.append(tpl)
# tpl_s = tuple(tpl_item)
# print(tpl_s)
# i = 0
# lst = []
# temp = 0
# for item in range(len(tpl_s)):
#
#     for j in range(0,len(tpl_s)):
#         temp += tpl_s[item][j]
#         lst.append(temp/len(tpl_s))
#         break
#
# print(lst[-1::-1])

# 28-misol
# tpls = (('333', '33'), ('1416', '55'))
# print(tpls)
# tpl_s = []
# for item in tpls:
#    for items in item:
#        tpl_s.append(int(items))
# print(tuple(tpl_s))


# 29 - misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(20), n))
# print(tpl)
#
# for item in tpl:
#     print(item, end="")




# 30-misol
# tpl = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# print(tpl)
# for item in tpl:
#     for rang in item:
#         if rang == "Lime":
#             print(True)
#         elif rang == "Olive":
#             print(False)


# 31-misol
# n = int(input("n = "))
# tpl = tuple(random.sample(range(20), n))
# tpl2 = tuple(random.sample(range(20), n))
# tpl3 = tuple(random.sample(range(20), n))
#
# print(tpl)
# print(tpl2)
# print(tpl3)
#
# result = tuple(map(sum, zip(tpl, tpl2, tpl3)))
# print(result)

# 32-misol
# n = int(input("n = "))
# lst = []
# for i in range(n):
#     temp = tuple(random.sample(range(20), 2))
#     lst.append(temp)
# print(lst)
# temp = 0
# lst_item = []
# for item in lst:
#     temp = sum(item)
#     lst_item.append(temp)
# print(lst_item)


# n = int(input("n = "))
# lst = []
# for i in range(n):
#     a = tuple(random.sample(range(20), 3))
#     lst.append(a)
# print(lst)
# summa = []
# for item in lst:
#     temp = sum(item)
#     summa.append(temp)
# print(summa)




# 33-misol

# a = [(1, 2), (2, 3), (3, 4)]
# print(a)
# lst = []
# for i in a:
#     temp = list(i)
#     lst.append(temp)
# print(lst)
















