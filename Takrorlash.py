from ctypes.wintypes import PINT
from math import ceil, floor


# print("hello world")
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

# name = "Asqar"
# age = "2122222"

# print("Assalomu aleykum "+ name + " yoshingiz " + age +" da")



# string haqida qisqacha malumot
# string = "IT Academy"
# print(string.lower().islower())
# print(string.lower().isupper())
# print(string.index("A"))
# print(string.replace("IT","Evers"))


# number haqida qisqacha tushuncha
# print(type(2.4))
# my_num = -4
# print(str(my_num)+ " my favorite num ")
# print(round(3.3))

# input bilan o'zgaruvchilarni kiritish


# name = input("Enter your name: ")
# age = input("Enter you age: ")
# print("Hello " + name + "!\n you are "+age)




# list haqida tushunchalar
# numbers = [2, 4, 6, 2, 3, 87, {"name": "name","age":"21"},[2],6]
# lst = ['Asqar', 'sherzod', 'kamron','Umid']
# lst.extend(numbers)
# lst.insert(1,"olma")
# lst.remove("olma")
# lst2 = lst.copy()
# print(lst)
# print(lst2)
# for i in lst:
#     print(i)




# tuple haqida qisqacha tushuncha
# lst = [1,4,7]
# lst[1] = 3
# print(lst)
# tpl = (3,6,4,7,9,5,0,3,1)
# print(tpl[1])
# print(type(tpl))
# for i in tpl:
#     print(i)


# funksiya haqida qisqacha tushuncha

# def sum(name):
#     print("hello "+name)
# sum("Asqar")

# def kvadrat(a):
#     return a*a

# kv = kvadrat(32)
# print(kv)



# if shart operatori haqida

# is_mail = False

# if is_mail:
#     print("salom dunyo")
# else:
#     print("xayir")


#
# def max_num(num1,num2,num3):
#     if num1< num2 and num2 > num3:
#         return (num2)
#     elif num1 > num2 and num1 > num3:
#         return(num1)
#     elif num3 > num2 and num3>num1:
#         return(num3)

# result = max_num(4,7,9)

# print(result)

# num1 = float(input("Enter  first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))

# def calculator(num1,op,num2):
#     if op == "+":
#         return (num1+num2)
#     elif op == "-":
#         return(num1-num2)

#     elif op == "*":
#        return num1 * num2

#     elif op == "/":
#         return num1/num2
#     else:
#         return("Notdifined")

# result = calculator(num1,op,num2)
# print(result)

# lug'atlar haqida tushuncha

# lugatlar = {
#     "Dekabr":[
#         "March",
#         "Aprel",
#         "May"
#     ]
# }
lugatlar = {
    "num1":"1",
    "num2":"2",
    "num3":"3",
    "num4":"4",
    "num5":"5",
    "num6":"6",
    "num7":"7",
    "num8":"8",
    "num9":"9",
    "num10":"10",
    "num11":"11",
    "num12":"12"
}
# print(lugatlar.get("num42","not valu and key"))
# print(lugatlar.get("num2"))
# print(lugatlar.keys())
# print(lugatlar.values())
# print(lugatlar.items())

# lugatlar["num13"] = "13"
# print(lugatlar)

# res = lugatlar.copy()
# print(lugatlar)
# res = lugatlar.clear()
# print(res)
 

#  while haqida tushunchalar
# i = 0
# while i <= 10:
#     i+=1
#     print(i)
# print("Tugadi!")

# secret_word = "Academy"
# new_word = ""
# new_count = 0 
# new_limit = 3
# out_of_new = False

# while new_word != secret_word and not(out_of_new):
#     if new_count < new_limit:

#         new_word = input("Enter new word: ")
#         new_count += 1
#     else:
#         out_of_new = True
# if out_of_new:
#     print("Out of new")
# else:
#     print("you win!")


# def raise_to_power(base_num,pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result

# print(raise_to_power(2,4))



