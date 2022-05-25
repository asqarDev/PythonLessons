

# import pickle
# with open("info","rb") as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
# print(talaba1)
# print(talaba2)

import json
# x = 10
# x_json = json.dumps(x)
# print(x)
# print(type(x))
# print(x_json)
# print(type(x_json))

# tpl = (12, 23, 34, 56, 8)
# print(tpl)
# print(type(tpl))
# tpl_json = json.dumps(tpl)
# print(tpl_json)
# print(type(tpl_json))
# print(tpl_json[2])


# bemor = {
#     "ism":"Mirzayev Asqar",
#     "yosh": 21,
#     "oila": False,
#     "farzandlar": ("Ahmad", "Bonu"),
#     "allergiya": None,
#     "dorilar": [
#         {"nomi": "Analgin", "miqdori": 0.5},
#         {"nomi": "Panadol", "miqdori": 1.2}
#     ]
# }

# data_json = json.dumps(bemor, indent=4)
# print(data_json)
# print(bemor.keys())

# with open("bemor.json", "w") as f:
#     json.dump(bemor, f, indent=4)

# with open("bemor.json", "r") as f:

#     print(f.read())

# bemor2 = json.loads(data_json)
# print(bemor2)






# yosh = input("yoshingizni kiriting: ")

# try:
#     yosh = int(yosh)
    
# except:
#     print("Butun son kiriting iltimos!")
# else:
#     print(f"siz {2022-yosh} - yilda tug'ulgansiz")

# x,y=7,10
# try:
#    s = y/(x-5)
#    print(s)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")

# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)        
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas")
#     else:
#         print(talaba['ism'])
#         fayl ustida turli amallar 




