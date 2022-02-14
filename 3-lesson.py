# a=int(input("a = "))
# print(a>0)

#2-misol
# a=int(input('a='))
# print(a%2==0)


# a=int(input('a='))
# print(a%2==1)

# 4-misol
# a,b=eval(input('a,b ni kiriting: '))
# print(a>2&b<=3)

# 5-misol
# a,b=eval(input('a,b ni kiriting: '))
# print(a>=0 | b<-2)

# 6-misol
# a,b,c = eval(input('sonlarni kiriting: '))
# print(a<=b and b<=c and a<=c)

# 7-miso
# a,b,c = eval(input('sonarni kiriting: '))
# print(a<b and b<c and a<c)
# 8-misol
# a,b = eval(input('a,b = '))
# print(a%2==0 and b%2==0)

# kun = input('bugun qanday kun? ')
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('bugun ish kuni')

# 9-misol
# a,b = eval(input('a,b = '))
# print(a%2==0 and b%2==1 or a%2==1 and a%2==0)


# 10-misol
# a,b = eval(input('a,b = '))
# print(a%2==1 and b%2==0 or a%2==0 and b%2==1 or a%2==1 and b%2==1)

# 11-misol
# a,b = eval(input('a,b = '))
# print(a%2==0 and b%2==0 or a%2==1 and b%2==1)

# 12-misol
# a,b,c = eval(input('a,b,c = '))
# print(a>0 and b>0 and c>0)


# a,b,c = eval(input('a,b,c = '))
# print(a<0 and b>0 and c>0 or a>0 and b<0 and c>0 or a>0 and b>0 and c<0)
# print(a>0 and b<0 and c<0 or a<0 and b>0 and c<0 or a<0 and b<0 and c>0)
# print(a>0 and b>0 and c<0 or a<0 and b>0 and c>0 or a>0 and b<0 and c>0)


# 16-misol
# n=int(input('n = '))
# print(n%2==0 and n>9 and n<99)

# n=int(input('n = '))
# print(n%2==1 and n>99 and n<999)



# a,b,c  = eval(input('sonlarni kiriting: '))
# print(a==b and a!=c or a!=b and a==c or c==b and a!=c)

# a,b,c = eval(input('sonlarni kiriting: '))
# print(a==b and b!=c or a==c and c!=b or c==b and b!=a)

# 19-misol
# a,b,c = eval(input("sonlarni kiritng: "))
# print(a<0 and b>0 and c>0 or b<0 and a>0 and c>0 or c<0 and a>0 and b>0)

# 20-misol
# a=int(input('uch xonali sonni kiriting: '))
# # b=a//100
# # i=a//10%10
# # u=a%10
# # print(b!=i and i!=u)

# 21-misol
# a=int(input('uch xonali sonni kiriting: '))
# b=a//100
# i=a//10%10
# u=a%10
# print(b<i and i<u or b>i and i>u)

# 23-misol
turtxonalison = int(input('sonni kiriting: '))
a=turtxonalison//1000
b=turtxonalison//100%10
c=turtxonalison%100//10
d=turtxonalison%10

print(a==d and b==c or a==b==c==d)