# Mavzu: Shart operatorlari 
#1-misol
# a = int(input('a = '))
# if(a<0):
#     print(a+1)
# else:
#     print(a-2)



# 3-misol
# a = int(input('a = '))
# if(a<0):
#     print(a-2)
# elif(a==0):
#     print(10)
# else:
#     print(a)

# 4-misol
# a,b,c = eval(input('sonlarni kiriting: '))
# if(a>0 and b<0 and c<0 or a<0 and b>0 and c<0 or a<0 and b<0 and c>0):
#     print(1,2)
# elif(a>0 and b>0 and c<0 or a<0 and b>0 and c>0 or a>0 and c>0 and b<0):
#     print(2,1)
# else:
#     print(3,0)

# 6-misol
# a,b = eval(input('sonlarni kiriting: '))
# if a>b:
#     print(a)
# else:
#     print(b)

# 7-misol
# a,b=eval(input('sonlarni kiriting: '))
# if a>b:
#     print(a,b)
# else:
#     print(b,a)

# 9-misol
# a,b=eval(input('sonlarni kiriting: '))
# if a>b:

#     print(a,b)
# else:
#     a=a+b
#     b=a-b
#     a=a-b
#     print(a,b)

# 10-misol
# a,b = eval(input('sonlarni kiriting: '))
# if a==b:
#     a=0;
#     b=0;
#     print(a,b)
# else:
#     a=a+b;
#     b=a;
#     print(a,b)

# 11-misol
# a,b = eval(input('sonlarni kiriting: '))
# if a==b:
#     a=0
#     b=0
#     print(a,b)
# elif a>b:
#     b=a;
#     print(a,b)
# 14-misol
# a,b,c=eval(input('sonlarni kiriting: '))
# if a<b and b<c:
#     print(c,a)
# elif c<b and b<a:
#     print(a,c)
# elif a<c and c<b:
#     print(b,a)
# elif c<a and a<b:
#     print(b,c)
# elif a>b and a<c:
#     print(c,b)
# elif c>b and c<a:
#     print(a,b)

# 15-misol
# a,b,c = eval(input('sonlarni kiritng: '))
# if a>b and b>c:
#     print(a,b,a+b)
# elif c>b and b>a:
#     print(c,b,c+b)
# elif b>a and a>c:
#     print(b,a,a+b)
# elif b>c and c>a:
#     print(b,c,b+c)
# elif a>b and a<c:
#     print(c,a,c+a)
# elif c>b and c<a:
#     print(a,c,a+c)


# 16-misol
# a,b,c=eval(input('sonlarni kiriting: '))
# if a<b<c:
#     print(2*a,2*b,2*c)
# else:
#     print(1/a,1/b,1/c)


# a,b,c=eval(input('sonlarni kiriting: '))
# if c<b<a:
#     print(2*a,2*b,2*c)
# else:
#     print(-a,-b,-c)

# 18-misol
# a,b,c = eval(input('sonlarni kiriting: '))
# if a>0 and b>0 and c>0:
#     print(3)
# elif a>0 and b<0 and c>0:
#     print(2)
# elif a<0 and b>0 and c>0:
#     print(1)

# 19-misol
# a,b,c,d = eval(input('sonni kiriting: '))
# if a%2!=0 and b%2!=0 and c%2!=0 and d%2==0 or a%2==0 and b%2==0 and c%2==0 and d%2!=0:
#     print(4)
# elif a%2!=0 and b%2!=0 and c%2==0 and d%2!=0 or a%2==0 and b%2==0 and c%2!=0 and d%2==0:
#     print(3)
# elif a%2!=0 and b%2==0 and c%2!=0 and d%2!=0 or a%2==0 and b%2!=0 and c%2==0 and d%2==0:
#     print(2)
# else:
#     print(1)

# 20-misol

# a,b,c=eval(input('kordinatalarni kiriting: '))
# if abs(b-a)<abs(c-a):
#     print(b,abs(b-a))
# elif abs(c-a)<abs(b-a):
#     print(c,abs(c-a))
# elif abs(a-b)>abs(c-a):
#     print(c,abs(c-a))

# 21-misol
# x,y=eval(input('kardinatalarni kiriting: '))
# if x==0 and y==0:
#     print(0)
# elif y==0 and x!=0:
#     print(1)
# elif x==0 and y!=0:
#     print(2)
# else:
#     print(3)


# 22-misol

# x,y=eval(input('kordinatalarni kiriting: '))
# if x!=0 and y!=0:
#     if x>0 and y>0:
#         print(1)
#     elif x<0 and y>0:
#         print(2)
#     elif x<0 and y<0:
#         print(3)
#     else:
#         print(4)
# else:
#     print("shart bo\'yicha kordinatani kiritmadiz")



# 23-misol

# x1,y1,x2,y2,x3,y3=eval(input('kordinatalarni kiritng: '))
# if y1==y2 and x2==x3:
#     x4=x1;
#     y4=y3;
#     print(x4,y4)
# else:
#     print('Erorr')

# 24-misol
# from math import sin


# x=float(input('sonni kiriting: '))
# if x>0:
#     y=2*sin(x)
#     print(y)
# else:
#     print(6-x)

# 25-misol

# x=int(input('sonni kiriting: '))
# if x<-2 or x>2:
#     print(2*x)
# else:
#     print(-3*x)


# 26-misol
# x=float(input('x = '))
# if x<=0:
#     print(-x)
# elif x>0 and x<2:
#     print(x**2)
# else:
#     print(4)

# 27-misol
# x=float(input('x = '))
# if x<0 or x>=4:
#     print(0)
# elif x>=0 and x<1 or x>=2 and x<3:
#     print(1)
# elif x>=1 and x<2 or x>=3 and x<4:
#     print(-1)

# 28-misol
# yil=int(input('yilni kiriting: '))
# if yil%4==0 and yil%100==0 and yil%400==0:
#     print('kabissa yili ',366)
# else:
#     print('kabissa yilimas')

# 29-misol
# a=int(input('sonni kiriting: '))
# if a<0 and a%2==0:
#     print("manfiy juft son")
# elif a<0 and a%2!=0:
#     print("manfiy toq son")
# elif a>0 and a%2!=0:
#     print("musbat toq son")
# elif a>0 and a%2==0:
#     print("musbat juft son")
# elif a==0:
#     print("nol soni")
# else:
#     print('!!!')

# 30-misol
# son = int(input('son = '))
# if son//10>=10:
#     if son%10%2==0:
#         print("3-xonali  juf son")
#     else:
#         print("3-xonali toq son")
        
# elif son//10>0:
#     if son%10%2==0:
#         print("2-xonali  juft son")
#     else:
#         print("2-xonali toq son")
        
# else:
#     if son%2==0:
#         print('1-xonali  juft son')
#     else:
#         print("1-xonali toq son")
print("jhkhg")












