# Mavzu: String
# Standart funksiyalar yordamida satrlarni qayta ishlash. Izlash va almashtirish

# a = "Asqar& mIrzayev deveL\toper a 200\tabsc0"
# b = a.title()
# b = a.capitalize()
# b = a.lower()
# b = a.upper()
# b = a.casefold()
# b = a.center()
# b = a.count("a")    # sanaydigan medthod
# b = a.encode()
# b = a.endswith("00")            #True or False
# string = 'asqar \tdeveloper is python'
# b = string.expandtabs()
# b = string.find("python")  # string ichidan qidiradi
# ism = 'asqar'
# famlya = 'mirzayev'
# age = 22
# b = "Men {} {} {} yoshdaman".format(ism.title(), famlya.title(), age)
# print(b)
# text = 'Men23nsahd'
# a = text.index("in")
# print(len(text), text.isalnum())

# text = """How to in python
# how are
# you"""
# print(text)
# ism = "asqar"
# familya = "mirzayev"
# # result = ism + " " + familya
# result = "{} {} ".format(ism, familya)
# # new_text = ism*4
# print("asqar" in result)

# text = input("ismingizni kiriting: \n >>>")
# print("Assalomu aleykum ", text.title())






# 1-misol
# n = int(input("n = "))
# string = input(">>> ")
# if len(string) > n:
#     s = string[:n]
#     print(s.title())
# elif len(string) < n:
#     s = string + '.'*(n-len(string))
#     print(s.title())

# 2-misol
# n1, n2 = eval(input("n1 va n2 ni kiriting>>>"))
# s1 = input("s1>>>")
# s2 = input("s2>>>")
# s = s1[:n1] + s2[len(s2)-n2::]
# print(s)


# 3-miisol
# s = input(">>>")
# c = input("simvolni kiriting>>>")
# text = ''
#
# for i in s:
#     if i == c:
#         text += i
#     text += i
# print(text.title())

# 4-misol
# c = input(">>>")
# s = input("s>>>")
# s0 = input("s0>>>")
# new_s = ''
# for i in s:
#     if i==c:
#         new_s += s0
#     new_s += i
# print(new_s.title())


# 5 -misol
# c = input(">>>")
# s = input(">>>")
# s0 = input(">>>")
# new_s = ''
# for i in range(-1, len(s)-1):
#     if s[i] == c:
#         new_s += s0
#     new_s += s[i+1]
# print(new_s.title())

# 6-misol
# s = input(">>>")
# s0 = input("s0 satrni kiriting: ")
#
# if s0 in s:
#     print(True)
# else:
#     print(False)

# 7-misol
# s = input("s ni kiriting: ")
# s0 = input("s0 ni kiritng: ")
# sana = s.count(s0)
# print(sana)

# 8-misol
# s = input("s = ")
# s0 = input("s0 = ")
# new_s = ''
# if s0 in s:
#     count = s.index(s0)
#     new_s = s[:count] + s[count+len(s0):]
#     print(new_s)
# else:
#     print(s)


# 9-misol
# s = input(">>>")
# s0 = input("s0>>>")
# index = s.rfind(s0)
# new_s = s[:index] + s[index+len(s0):]
# print(new_s)






# 10-misol
# s = input(">>>")
# s0 = input("s0>>>")
# if s0 in s:
#
#     text = s.replace(s0, "")
#     print(text)
# else:
#     print(s)

# 11-misol
# s = input("s >>> ")
# s1 = input("s1 >>> ")
# s2 = input("s2 >>> ")
# text = s.replace(s1, s2)
# print(text)

# 12-misol
# sd = "men zo'r dasturchiman kelajaka zo'r bo'ladi"
# s = input("s >>> ")
# s1 = input("s1 >>> ")
# s2 = input("s2 >>> ")
# index = s.rfind(s1)
# news = s[:index] + s2 + s[index+len(s1):]
# print(news)







# 13-misol
# s = input("s >>> ")
# s1 = input("s1 >>> ")
# s2 = input("s2 >>> ")
# txt = s.replace(s1, s2)
# print(txt)


# 14-misol
# s = input("s >>> ")
# pustoy = s.count(" ")
# new_s = s[s.index(" ")+1:]
# if s.count(" ") > 1:
#     news = new_s[:new_s.index(" ")]
#     print(news)
# else:
#     print(" ")


# 15-misol
# s = input("s >>> ").strip()

# if s.count(" ") > 1:
#     lst = s.split()
#     news = lst[1:-1]
#     ne = " ".join(news)
#     print(ne)
# else:
#     print(" -- ")





#9-misol
# s = "zo'r Mening computerim zo'r uoguyf"
# print(s.count("zo'r"))
# s0 = "zo'r"
# index = s.rfind(s0)
# s = s[:index]+ s0+s[index+len(s0):]
# print("RESULT: ", s)






