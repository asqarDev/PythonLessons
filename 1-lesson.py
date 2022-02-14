# 1-Mavzu
# 1-misol
# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x//100 + 1)
#     t.forward(x)
#     t.left(59)


# import math
# a=int(input('kvadratni tomonni kiriting: '))
# p=4*a
# s=math.pow(a,2)
# print(p,s)

# a=int(input("to\'g\'ri to\'rt burchakni tomonni kiriting:" ))
# b=int(input("to\'g\'ri to\'rt burchakni tomonni kiriting:" ))
# s=a*b;
# p=2*(a+b)
# print(s,p)

# pi=3.14;
# d=float(input('aylana diametrini kiriting: '))
# l=pi*d
# print('aylana uzunligi: ',l)


# 5-misol
# import math
# a=int(input('kubni qirrasini kiriting: '))
# v=math.pow(a,3)
# s=6*a*a
# print('hajim',v,'\nsirt yuzasi',s)

# a=int(input('paralapepedni tomonlarini kiriting: '))
# b=int(input('paralapepedni tomonlarini kiriting: '))
# c=int(input('paralapepedni tomonlarini kiriting: '))
# v=a*b*c
# s=2*(a*b+a*c+b*c)
# print('hajmi: ',v,'\nto\'la sirt yuzasi',s)


# # 7-misol
# r=float(input('aylana radiusini kiriting: '))
# pi=3.14
# l=2*pi*r
# s=pi*r*r
# print('aylana uzunligi: ',l,'aylana yuzasi: ',s)


# # 8-misol
# a=int(input('sonnni kiriting: '))
# b=int(input('sonni kiriting: '))
# natija=(a+b)/2
# print('ikki sonning o\'rta arifmetigi',natija)


# import math
# a=int(input('a>0 sonni kiriting: '))
# b=int(input('b>0 sonni kiriting: '))
# c=math.sqrt(a*b)
# print(c)

# import math
# a=int(input('sonni kiriting: '))
# b=int(input('kiriting: '))
# yigindi=a+b
# ayirma=math.fabs(a-b)
# bolinma=a/b
# kopaytma=a*b
# print(yigindi,ayirma,bolinma,kopaytma)

# # 12-misol
# import math
# a=int(input('katetni kiriting: '))
# b=int(input('kiriting: '))
# c=math.sqrt(a*a+b*b)
# p=a+b+c
# s=a*b/2
# print(c,p,s)


# 13-misol
# from math import pi
# r1=int(input('radiusni kiriting: '))
# r2=int(input('r2 radiusni kiriting: '))
# s1=r1**2*pi
# s2=r2**2*pi
# s3=s1-s2
# print(s3,s1,s2)

# 14-misol
# from math import pi
# l=float(input('l ni kiriting: '))
# r=2*pi/l
# s=pi*r**2
# print(r,s)


# import math
# s=float(input('kiriting: '))
# d=math.sqrt(4*s/math.pi)
# l=math.pi*d
# print(d,l)



# x=int(input('sonni kiriting: '))
# y=3*pow(x,6)-6*pow(x,3)-7;
# print(y)

# m=int(input('m gramda bering: '))
# kilogram=m/1000;
# print(kilogram)


# t=int(input('t ni kiriting: '))
# t=(t-4)%7
# print(t)


# a=int(input('a ni kiriting: '))
# b=int(input('b ni kiriting: '))
# c=int(input('c ni kiriting: '))
# natija=(a>0 & b<0 & c<0 | a<0 & b>0 & c<0 | a<0 & b<0 & c>0 )
# print(natija)

# a=int(input('sonni kiriting: '))
# if a<0:
#     print(a+1)
# else:
#     print(a-2)


# x=int(input('x ni kiriting: '))
# if x<-2 or x>2:
#     print(2*x)
# else:
#     print(-3*x)
    


# cars = ["Yomon", "Qoniqariz", "Qoniqarli", "Yaxshi", "A'lo"]
# i=int(input("Bahoni kiriting = "))
# print(cars[i-1])
# def put(self, request, pk):
#     object = MyModel.objects.get(id=pk)
#     serializer=self.serializer_class(object, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=200)
#     return Response(serializer.errors)

# def delete(self, request, pk):
#     object = MyModel.objects.get(id=pk)
#     object.delete()
#     return Response({"detail":"ok"})


# # 17-misol
# a=int(input("A nuqtani kiriting: "))
# b=int(input("B nuqtani kiriting: "))
# c=int(input("C nuqtani kiriting: "))
# a=c-a;
# b=c-b;

# print(a,b,a+b)


#18-misol
# a,b,c =eval(input("nuqtalarni kiriting: "))
# d=c-a;
# e=b-c;
# print(d,e,e*d)

# 19-misol
# x1,y1=eval(input('sonni kiriting: '))
# x2,y2=eval(input('sonni kiriting: '))
# a=abs(x1-x2);
# b=abs(y1-y2)
# p=2*(a+b);
# s=a*b;
# print(p,s)




# a,b=eval(input('kiriting: '))
# c=abs(a-b)
# print(c,type(c))

# 20-misol
# from math import sqrt

# x1,y1,x2,y2=eval(input('kordinatalarni kiriting: '))
# d=sqrt(pow((x2-x1),2)+pow((y2-y1),2))
# print(d)


# 21-misol
# from math import sqrt
# x1,y1,x2,y2,x3,y3=eval(input('uchburchakni kordinatalarini kiriting: '))
# a=sqrt(pow((x2-x1),2)+pow(y2-y1,2))
# b=sqrt(pow(x3-x2,2)+pow(y3-y2,2))
# c=sqrt(pow(x3-x1,2)+pow(y3-y1,2))
# p=(a+b+c)/2;
# s=sqrt(p*(p-a)*(p-b)*(p-c))
# print(p*2,s)


#22-misol
# a,b = eval(input('qiymatlarni kiriting: '))
# a=a+b;
# b=a-b;
# a=a-b;
# print(a,b)

#23-misol
# a,b,c=eval(input('a,b,c ni kiriting: '))
# a=a+b;
# b=a-b;
# a=a-b;
# a=a+c;
# c=a-c;
# a=a-c;
# print(a,b,c)


# 24-misol
# a,b,c = eval(input('sonlarni kiriting: '))
# a=a+c;
# c=a-c;
# a=a-c;
# a=a+b;
# b=a-b;
# a=a-b;
# print(a,b,c)


# 25-misol
# x=eval(input('x ni kiriting: '))
# y=3*pow(x,6)-6*pow(x,3)-7;
# print(y)


# 26-misol
# x=eval(input('x ni kiriting: '))
# y=4*pow(x-3,6)-7*pow(x-3,3)+2;
# print(y)


# 27-misol
# a=float(input('a='))
# a=a;
# b=a*a;
# a=b*b*a;
# print(a)


# from cmath import pi


# burchak=float(input('burchakni kiritng:  '))
# radian=burchak*pi/180;
# print(radian)


# 30-misol
# from cmath import pi


# radian=float(input('burchakni kiritng:  '))
# burchak=radian*180/pi;
# print(burchak)


# # 37-misol
# v1,v2,s,t=eval(input('sonlarni kiriting: '))
# s1=s-t*(v1+v2);
# print(s1)


# 38-misol
# a,b = eval(input('a and b = '))
# x=-b/a;
# print(x)


# 39-misol
# from math import sqrt


# a,b,c=eval(input('tenglama koyfitsentlarini kiriting: '))
# x1=(-b+sqrt(b*b-4*a*c))/(2*a)
# x2=(-b-sqrt(b*b-4*a*c))/(2*a)
# print(x1,x2)

# 40-misol
a1,b1,c1, a2,b2,c2=eval(input(' koeffisientlarni kiriting: '))
y=(c2-a2*c1)/(b2-b1*a2)
x=c1-b1*((c2-a2*c1)/(b2-b1*a2))
print(x,y)