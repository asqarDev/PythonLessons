# 5-mavzu: For operatori

# k,n=eval(input('sonlarni kiriting: '))
# for i in range(1,n+1):
#     print(k)

# 2-misol
# a,b = eval(input('a,b = '))
# count=0
# if a>b:
#     for i in range(b,a+1):
#         print(i,sep=" ")
#         count+=1
#     print(count)
# else:
#     print("a>b katta emas xato kiritingiz!")



# 3-misol
# a,b = eval(input('b>a sonni kiriting: '))
# count=0
# if b>a:
#     for i in range(b,a,-1):
#         count+=1;
#         print(i)
#     print(count)
# else:
#     print("shart bo'yicha qiymat kiritmadiz iltimos to'g'ri kiriting! ")

# 4-misol
# narx=float(input('narxini kiriting: '))
# for i in range(1,10+1):
#     natija=narx*i;
#     print(int(natija))

# x=4.023;
# y=3;
# y="Asqar"
# print(type(x))
# print(type(y))

# 5-misol
# narx=float(input('narx = '))
# for i in range(1,11):
#     print(i/10*narx)

# 6-misol
# narxi=float(input('narxi = '))
# for i in range(12,21,2):
#     print(i/10*narxi)


# 7-misol
# a,b=eval(input('a, b = '))
# sum=0
# if b>a:
#     for i in range(a,b+1):
#         sum+=i
#         print(i)
#     print(sum)
# else:
#     print("no to'g'ri kiritdingiz!")


# a,b=eval(input('a, b = '))
# sum=1
# if b>a:
#     for i in range(a,b+1):
#         sum*=i
#         print(i)
#     print(sum)
# else:
#     print("no to'g'ri kiritdingiz!")


# 9-misol
# a,b=eval(input("a va b ni kiriting: "))
# natija=0
# if b>a:
#     for i in range(a,b+1):
#         print(i)
#         natija+=i**2
#     print(natija)
# else:
#     print("NO!")


# 10-misol
# n=int(input('n = '))
# summa=0
# for i in range(1,n+1):
#     summa+=i/n;
# print(summa)

# 11-misol
# n=float(input('sonni kiriting: '))
# summa=0
# for i in range(0,n+1):
#     summa+=pow(2*n,3)
#     print(i)
# print(summa)


# 12-misol
# import math
# n=eval(input('n = '))
# natija=1
# for i in range(1,n+1):
#     natija*=math.pow(0.1,i)*i;
# print(natija)


# # 13-misol
# n=int(input('n = '))
# sum=0
# for i in range(1,n+1):
#     sum-=-(1+i/10)
# print(sum)


# for i in range(10):
#     pass

# list = [12, "text", 34, 3.2]
# # for i in list:
# #     print(i)


# while len(list)!=0:
#     print(list.pop())

# n=2
# multiply = 1
# for i in range(1, n+1):
#     multiply*=float(f"1.{i}")
#     print(f"1.{i}")
# print(multiply)


# n=eval(input('n = '))
# sum=1
# for i in range(1,n+1):
#     sum*=float(f"1.{i}")
#     # print(f"1.{i}")
# print(sum)


# 13-misol
# n=eval(input('n = '))
# sum=0;
# for i in range(1,n+1,2):
#     sum+=(float(f"1.{i}")-float(f"1.{i+1}"))
# print(sum)


# 14-misol
# n=int(input('n = '))
# sum=0
# for i in range(1,n+1):
#     sum+=(2*i-1)
#     sum=i**2;
#     print(sum)

# 15-misol

# a,n = eval(input('a va n ni kiriting: '))
# multplay=1
# for i in range(1,n+1):
#     multplay=pow(a,i)
# print(multplay)


#16-misol
# a,n=eval(input('a va n ni kiriting: '))
# for i in range(1,n+1):
#     sum=pow(a,i)
#     print(sum)


# 17-misol
# a,n=eval(input('sonlarni kiriting: '))
# sum=0
# for i in range(n+1):
#     sum+=pow(a,i)
#     print(sum)

# 18-misol
# a,n=eval(input('sonlarni kiriting: '))
# sum=0;
# for i in range(n+1):
#     sum+=(pow(-a,i))
# print(sum)


# 19-misol
# n=int(input('n = '))
# count=1
# for i in range(1,n+1):
#     count*=i
# print(count)

# 20-misol

# n=int(input('n = '))
# sum=0;
# count=1
# for i in range(1,n+1):
#     count*=i
#     sum+=count
# print(sum)

# 21-misol
# from math import factorial
# n=int(input('n = '))
# sum=0;
# for i in range(n+1):
#     f=factorial(i)
#     sum+=1/factorial(i)
# print(sum,f)

# 22-misol
# from math import factorial


# x,n=eval(input('x and n = '))
# sum=0
# for i in range(n+1):
#     sum+=(pow(x,i)/factorial(i))
# print(sum)

# 23-misol
# from math import factorial


# x,n=eval(input('sonlarni kiriting: '))
# sum=0
# for i in range(1,n+1):
#     f=factorial(2*i-1)
#     sum+=(-(pow(-1,i)*pow(x,2*i-1))/f)
# print(sum,f)


# 24-misol
# from math import factorial


# x,n=eval(input('sonlarni kiriting: '))
# sum=0;
# for i in range(n+1):
#     f=factorial(2*i);
#     print(f)
#     sum+=(pow(-1,i)*pow(x,2*i)/f)
# print(sum)


#  25-misol
# x,n = eval(input('x va n ni kiriting: '))
# sum=0;
# for i in range(1,n+1):
#     sum+=pow(-1,i-1)*pow(x,i)/i;
# print(sum)


# 26-misol
# x,n=eval(input('x va n ni kiriting: '))

# sum=0;
# for i in range(1,n+1):
#     sum+=(pow(-1,i-1)*pow(x,2*i-1)/(2*i-1))
# print(sum)


# 27-misol
# x,n=eval(input('x,n = '))
# sum=0;
# for i in range(1,n+1):
#     sum+=((2*i-1)*pow(x,2*i-1)/(2*i));
# print(sum)


# 29-misol
# a,b,n=eval(input('sonlarni kiriting: '))
# if b>a:
#     for i in range(n+1):
#         h=(b-a)/n;
#         count=a+i*h;
#         print(count)
#     print("h = ",h)
    
# else:
#     print("No!")



# 30misol
# from math import ceil, floor, sin
# n,a,b=eval(input('sonlarni kiriting: '))
# if b>a:
#     for i in range(n+1):
#         h=(b-a)/n;
#         y=(1-sin(i))
#         print(round(y,2))
#     print(h)
# else:
#     print('No!')


# 31-misol
# n=int(input('n = '))
# sum=[2]
# for i in range(1,n+1):
#     a=2+1/sum[i-1]
#     sum.append(a)
# print(sum)

# 32-misol
# n=int(input('n = '))
# temp=[1]
# for i in range(1,n+1):
#     a=(temp[i-1]+1)/i;
#     temp.append(a)
# print(temp)

# 33-misol
# n=int(input('n = '))
# fibanachi=[1,2]
# for i in range(2,n+1):
#     f=fibanachi[i-2]+fibanachi[i-1]
#     fibanachi.append(f)
# print(fibanachi)


# 34-misol
# n=int(input('n = '))
# a=[1,2]
# for i in range(2,n+1):
#     fibanachi=(a[i-2]+2*a[i-1])/2
#     a.append(fibanachi)
#     print(a)


# 35-misol
# n=int(input('n = '))
# a=[1,2,3]
# for i in range(3,n):
#     ak=a[i-1]+a[i-2]-2*a[i-3]
#     a.append(ak)
# print(a)

