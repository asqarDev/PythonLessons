
# Mavzu: dictionary and Lug’atlar topshiriq

# dic = {
#     "key":"value",
#     "text":234,
#     "status":True,
# }
#
# print(dic['status'])
# print(dic.keys())
# print(dic.values())
#
# for value in dic.values():
#     print(value)
#
# for key in dic.keys():
#     print(key)
#     print(dic[key])
#
# dic['key'] = 1111
# print(dic.keys())
#
#
# dic['lst'] = [12, 23, 5, True]
# print(dic.items())
# print(list(dic.items()))
# dc1 = dic.copy()
# print(dc1.pop('key'))
# print(dc1)
# print(sorted(dic.values()))

# 1-misol


# dict = {'name': 21, 'sunname': 23, 'fulname': 20, 'alkdgj': 22, "aksjgds": 78}
# dict = {}
# n = int(input("n = "))
#
# for item in range(n):
#     key = (input("key: "))
#     value = int(input("value: "))
#     dict[key] = value
# print(dict)
# print(sorted(dict.items(), key=lambda v: v[1], reverse=True))

# 2-misol
# dict = {}
# n = int(input("n = "))
# for i in range(n):
#     key = input("key: ")
#     value = float(input("value: "))
#     dict[key] = value
# print(sorted(dict.items()))


# 3-misol
# dic = {}
# n = int(input("n = "))
# for i in range(n):
#     key = input("key: ")
#     value = int(input("value: "))
#     dic[key] = value
# print(dic)
# elements = int(input("nechta element qo'shmoqchisiz "))
# for i in range(elements):
#     key = input("key: ")
#     value = int(input("value: "))
#     dic[key] = value
# print(dic)


# 4-misol
# import random
#
# dic = {}
# n = int(input("n = "))
# for i in range(n):
#     key = random.randint(1, 12)
#     value = random.randint(12, 23)
#     dic[key] = value
#
#
# for i in range(n):
#     key = random.randint(11, 223)
#     value = random.randint(22, 33)
#     dic[key] = value
#
#
#
# for i in range(n):
#     key = random.randint(22, 34)
#     value = random.randint(44, 56)
#     dic[key] = value
# print(dic)


# 6-misol
# n = int(input("n = "))
# dic = {}
# for item in range(1, n):
#     dic[item] = item**2
# print(dic)

# 7-misol
# import random
#
# dict = {}
# n = int(input("n = "))
# for i in range(n):
#     dict[i] = random.randint(1, 23)
# print(dict)
# sum = 0
# for i in dict.values():
#     sum += i
# print(sum)

# 8-misol
# n = int(input("n = "))
# dic = {}
# for i in range(n):
#     key = input("key: ")
#     value = int(input("value: "))
#     dic[key] = value
# print(dic)
# a = input("elementni o'chirmoqchimisiz ? ")
# if a.lower()=="ha":
#
#     element = input("kalitni kiriting: ")
#     dic.pop(element)
#     print(dic)
# elif a.lower() == "yo'q":
#     print(dic)


# 9-misol
# dic = {"name":"nima"}
# if len(dic) > 0:
#     print(True)
# else:
#     print(False)

# 10-misol
# s = input("stringni kiriting: ")
# d = {}
# for i in range(len(s)):
#     d[s[i]] = s.count(s[i])
# print(d)


# internetdan massalalari

# 1-misol
# import random
#
# n = int(input("n = "))
# dic = {}
# for i in range(n):
#     dic[i] = random.randint(1, 23)
# print((sorted(dic.items(), key=lambda v: v[1])))
# print((sorted(dic.items(), key=lambda v: v[1], reverse=True)))
import random


# 2-misol
# n = int(input("n = "))
# dic = {}
# for item in range(n):
#     dic[item] = random.randint(4, 23)
# print(dic)
#
# a = elem = input("element qo'shmoqchimisiz ? ")
# if a.lower() == "ha":
#     key = int(input("key: "))
#     value = int(input("value: "))
#     dic[key] = value
#     print(dic)
# elif a.lower() == "yo'q":
#     print(dic)

# 3-misol
#
# n = int(input("n = "))
# lst1 = list(random.sample(range(24), n))
# lst2 = list(random.sample(range(22, 45), n))
# print(lst1, lst2)
# lst = lst1+lst2
# # dic = {lst[i]: lst[i+1] for i in range(0, len(lst), 2)}
# dic = {}
# for i in range(0, len(lst), 2):
#     dic[i] = lst[i+1]
# print(dic)


# 4-misol
# dic = {}
# n = int(input("n = "))
# for i in range(n):
#     key = random.choice("jalsfbgeuhrakbh")
#     value = random.randint(1, 34)
#     dic[key] = value
# print(dic)
# print(sorted(dic.items()))

# 5-misol
# dic = {}
# n = int(input("n = "))
# for i in range(n):
#     key = random.choice("abscdefghijjkadbasmmcxbvn")
#     value = random.randint(1, 23)
#     dic[key] = value
# print(dic)
# print(max(dic.values()))

# 6-misol
# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = Counter(d1) + Counter(d2)
# print(d)

# 7-misol

# data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# for i in range(len(data)):
#     pass
#
#
# print(data)


talabalar = {
    "ali":"iphone 4",
    "hasan": "iphone x",
    "vali": "iphone 12 pro max",
    "asadbek": "redmi"
}

# for i in talabalar.values():
#     print(i)
# print(talabalar.items())
# phone = talabalar.get("murod", "bunday qiymat yo'q")
# print(phone)
#
# print(talabalar.items())

# for kalit, qiymat in talabalar.items():
#     print(f"kalit: {kalit}")
#     print(f"qiymat: {qiymat}\n")

# for k, q in talabalar.items():
#     print(f"{k.title()}ning telifoni {q.title()}")


car0 = {
    "model": "Lasseti",
    'rangi': "qora",
    "yili": "2019",
    "narxi": "23000$"
    }
car2 = {
    "model": "Gentra",
    'rangi': "movi",
    "yili": "2019",
    "narxi": "26000$"
    }
car3 = {
    "model": "Matiz",
    'rangi': "oq",
    "yili": "2014",
    "narxi": "2000$"
    }
# car = car0
# print(f"{car['model'].title()} rangi {car['rangi'].title()} yili {car['yili']} narxi {car['narxi']}")

# cars = [car0, car2, car3]
# for car in cars:
#     print(f"{car['model'].title()} "
#           f"{car['rangi'].title()} rang "
#           f"{car['yili']} - yil narxi {car['narxi']}"
#           )

#
# malibus = []
# for i in range(10):
#     new_car = {
#         "model": "malibu",
#         "rangi": None,
#         "yili": 2020,
#         "narxi": None,
#         "Km": 0,
#         "korobka": "avtomat"
#
#     }
#     malibus.append(new_car)
#
# for malibu in malibus[:3]:
#     malibu['rangi']='qizil'
# for malibu in malibus[3:6]:
#     malibu['rangi'] = 'qora'
#
# for malibu in malibus[6:]:
#     malibu['rangi'] = "oq"
#     malibu['korobka'] = 'mexanika'
# for malibu in malibus:
#     print(malibu)





# Amaliyot masala


StiwJobs = {
    "ismi": "Stiw Jobs",
    "tyili": 1968,
    "vyili": 2020,
    "manzili":"Amerika",
    "kasbi": "ixtirochi"
}

Alisher_Navoiy = {
    "ismi": "Alisher Navoiy",
    "tyili": 1441,
    "vyili": 1501,
    "manzili": "Hirot",
    "kasbi": "Adabiyot shunos"

}
buxoriy = {
    "ismi": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyili": 810,
    "vyili": 870,
    "manzili": "Buxoro",
    "kasbi": "G'irt bekorchi"
}

shaxslar = [StiwJobs, Alisher_Navoiy, buxoriy]
for item in shaxslar:
    ism = item['ismi']
    tyili = item['tyili']
    vyili = item['vyili']
    manzili = item['manzili']
    kasbi = item['kasbi']
    # print(f"{ism} {tyili}-yil {manzili} da tug'ilgan " f"{kasbi} bo'lgan {vyili} yili vafot etgan")
    # print(f"{item['ismi'].title()} {item['tyili']}-yilda tug'ilgan {item['manzili'].title()} da yashagan va {item['vyili']}-yil vafot etgan"
    #       f"{item['tyili']-item['vyili']} yil umr ko'rgan kasbi {item['kasbi']} bo'lgan")













