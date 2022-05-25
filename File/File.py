# Mavzu: Filelar bilan ishlash


# file = open("pi.txt")
# PI = file.read()
# print(PI)
# file.close()

# with open("pi.txt") as file:
#     pi = file.read()
#
# print(pi)
# print(type(pi))
#
# pi = pi.rstrip()
# pi = pi.replace("\n","")
# pi = float(pi)
# print(pi)
# print(type(pi))

# filename = "data/talabalar.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)

# with open(filename) as file:
#     talabalar = file.readlines()
# print(talabalar)
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)


# filename = 'data/new_file'
# ism = "Olimjonov Hasan"
# tyil = "2001"
# with open(filename,"w") as file:
#     file.write(ism+"\n")
#     file.write(str(tyil)+'\n')
# print(filename)

# filename = "data/new_file"
# with open(filename,"a") as file:
#     file.write("Asqar Mirzayev"+"\n")
#     file.write("2000")
#     print(file)

# import pickle
# talaba1 = {"ism":"Asqar", "familya":"Mirzayev","tyil":"2001","kurs":"3"}
# talaba2 = {"ism":"Begzod", "familya":"Axadovich","tyil":"1996","kurs":"1"}
# with open("info","wb") as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)



# with open("absd","a") as file:
#     file.write("Mirzayev")
# print(file)

# with open("absd","w") as file:
#     file.write("Asqar")
# print(file)
# with open("absd","x") as file:
#     file.write("Qaxramonivich")
# print(file)

# with open("absd","a") as file:
#     file.write("Frontend")
# print(file)


# fileni o'chirish
# import os
# os.remove("absd")

# fileni yaratish
# with open("file.txt", "w") as file:
#     file.write("Mirzayev")



# fileni mavjudligini tekshirish
# import os
# if os.path.exists("file.txt"):
#     os.remove("file.txt")
# else:
#     print("Hello file")


import os
# os.mkdir("myfolder")
# os.rmdir("myfolder")

import json
# file = open("../1-lesson.py")
# data = json.load(file)
#
# with open("data.json") as file:
#     data = json.load(file)
# data = file.read()
#
# print(data)

# for i in data:
#     print(i.values())












# Amaliyot masalalari

# 1-misol
# f = open("vazifa.txt", "w")
# f.write("Men Mirzayev Asqar Frontend developer")

# with open("vazifa.txt", "w+") as file:
#     file.write("Men Mirzayev Asqar")
#
# file.close()
# with open("vazifa.txt", "r") as file:
#     print(file.read())

# 2-misol
# 06.08.2001
# with open("pi_million_digits (1).txt", "r") as file:
#     if "06082001" in file:
#         print("uchradi")
#     else:
#         print("NO")

# 3-misol
# import pickle
# with open("pi_million_digits (1).txt") as file:
#     pi = file.read()
# pi = pi.rstrip()
# pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
# pi = pi.replace(' ','')
# bdate = '31122000'
# print(bdate in pi)
# pi = float(pi)
# with open('pi_million_digits (1).txt','wb') as file:
#     pickle.dump(pi, file)




# 4-misol

# while True:
#     book = input("Yaxshi ko'rgan kitobizni kiriting: ")
#     if not book:
#         break
#     with open("books.txt", "a") as file:
#         file.write(book+"\n")


# Json mavzusi:
# 1-misol
# import json
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# with open("testing.json", "w") as file:
#     data1 = json.dump(data, file, indent=4)
#
# with open("testing.json", "r") as file:
#     print(file.read())


# 2-misol
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# with open("testing.json", "w") as f:
#     talaba = json.dump(talaba_json, f, indent=4)
#
# with open("testing.json", "r") as f:
#     print(f.read())

# 3-misol

# with open("api-result.json", "r") as f:
#     new_json = f.read()
#     print(new_json)
# new_lst = json.loads(new_json)
#
#
# print(new_lst["query"]["pages"]["13801"]["title"])
# print(new_lst["query"]["pages"]["13801"]["extract"])


# 4-misol
# with open("students.json", "r") as f:
#     student = f.read()
# a = json.loads(student)
# print(type(a))
# s = json.dumps(a, indent=4)
# print(s)
#
# for i in a['student']:
#
#     print(f'{i["name"]} {i["lastname"]} {i["year"]} - kurs {i["faculty"]} talabasi')



