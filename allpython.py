# massalalar to'plami

# a = [1,4,6]
# b = [3,7,2]
# item_sum = []
# for (item1, item2) in zip(a, b):
#     item_sum.append(item1+item2)
# print(item_sum)




# string:
# 8-misol
# s = "Mening satrim satrga ega"
# s0 = "satr"
# if s0 in s:
#
#     index = s.index(s0)
#     s = s[:index]+s[index+len(s0):]
# print("Natijaviy s:{}".format(s))

# #2-misol
# n1, n2 = eval(input('Son:\n'))
#
#
# s1 = "Telegram"
# s2 = "instagram mesenger"
# s = "Telefon aloqa mesenger"
#
# s = "Salom Jamshid, qalaysan"

# if s.count(" ")>1:
#     result = ''
#     index = s.index(" ")+1
#     while s[index]!=" ":
#         result += s[index]
#         index+=1
#     print(result)
# else:
#     print("")




import random
def sontop(x):
    i = 0
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi")
    while True:
        i += 1
        taxmin = int(input(">>> "))
        if taxmin > tasodifiy_son:
            print(f"Xato, men o'ylagan son bundan kichik qaytadan kiriting: ")
        elif taxmin < tasodifiy_son:
            print(f"Xato, men o'ylagan son bundan katta qaytadan kiriting: ")
        else:
            print(f"Topdingiz {i} taxmin bilan topdingiz")

            break
    return i


sontop(10)







