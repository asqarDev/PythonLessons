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

with open("absd","a") as file:
    file.write("Frontend")
print(file)


# Amaliyot masalalari

# 1-misol
