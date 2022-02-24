# while shartli takrorlash operatori


# summa=input("summani kiriting: ")
# if summa.isdigit() and int(summa)>0 and int(summa)<100000:
#     print("tashakkur to'lov amalga oshirildi!")



# x="texr  text"
# print(x.split("t"))


# 1-misol


# a=eval(input('a va b ni kiriting: '))
# i,sum=0,0;
# while i<a:
#     i+=1;
#     if i%2==0:
#         continue;
#     print(i)
#     sum+=i;
# print(sum)

# a=eval(input('a = '))
# i,sum=0,0
# while a>i:
#     i+=1;
#     if i==4:
#         break;
#     print(i)
#     sum+=i;
# print(sum)
# print("Dastur tugadi")


# a=[12,122,32,34,56,67,2,3,55,3,0,34]
# b={}
# while a:
#     a=sorted(a)
#     print(a)
#     c=a.pop()
#     print(c)
#     break;


#-----------------<  While  >------------------
# 1-misol
# a,b=eval(input('a,b = '))
# count=0
# while b<a:
#     count+=1
#     a=a-b
#     print(count)
# print("qolgan qismi = ",a)


# 2-misol
# a,b=eval(input('a,b = '))
# count=0
# while a>b:
#     a=a-b;
#     count+=1;
# print("kesmalar soni",count)
# print(a)



# 3-misol
# n,k=eval(input('n,k = '))
# i=0
# while n>k:
#     i+=1;
#     n=n-k;
# print(i,n)


# n=12
# n=n/5
# print(n)
# 15/3    5/3   1/3  0
# 27/3     9/3   3/3  1
# 4-misol




# 5-misol
# n=int(input("n = "))
# i=0
# if n%2==0 and n>0:
#     while n>0 and n%2==0:
#         i+=1;
#         n=n/2;
#     print(i)
# else:
#     print("NO!")



# 6-misol

# n=int(input("n = "))
# i=0
# a=1
# while i<n:
#     a*=n-i
#     i+=2;
# print(a)

# 7-misol

# n=int(input('n = '))
# i=0;
# while i*i<n:
#     i+=1;
# print(i)



# 8-misol
# n=int(input("n = "))
# i=0;
# while i*i<n:
#     i+=1;
# print(i-1)


# 9-misol
# n=int(input('n = '))
# i=1;
# while i<n:
#     if pow(3,i)>n:
#         print(i)
#         break
#     i+=1;
# # print(i)

# 10-misol
# n=int(input('n = '))
# i=1;
# while 3**i<n:
#     i+=1;
# print(i-1)

# 11-misol
# n=int(input('n = '))
# i=0;
# sum=0
# while sum<n:
#     i+=1;
#     sum+=i
# print(i,sum)



# 12-misol
# n=int(input('n = '))
# i=0;
# sum=0;
# while sum<n:
#     i+=1;
#     sum+=i
# print(i-1,sum-i)



# 13-misol
# a=float(input('a = '))
# i=0;
# sum=0;
# while sum<=a:
#     i+=1;
#     sum+=1/i;
# print(i,round(sum,1))



# 14-misol
# a=float(input('a = '))
# i=0;
# sum=0;
# while sum<a:
#     i+=1;
#     sum+=1/i;
# print(i-1,sum-1/i)


# 15-misol
# p=float(input('p = '))
# i=0;
# sum=1000;
# while sum < 1100:
#     i+=1;
#     sum=sum*(1+p/100)
# print(i,round(sum))



# 16-misol
# from math import ceil


# p=float(input('p = '))
# s1=10;
# k=0;
# s2=0
# sum=10
# while sum<40:
#     k+=1;
#     s1=s1*(1+p/100);
#     sum+=s1
# print(k,round(sum,1))



# 17-misol
# n=int(input('n = '))
# i=0;
# while n>0 and i==0:
#     i+=1
#     oxiri=n%10;
#     onlik=n//10%10;
#     yuzlik=n//100%10;
#     n=n//1000;
# print(oxiri,onlik,yuzlik,n)

# 17-misol
# n=int(input('n = '))
# i=0
# while n>0:
#     qoldiq=n%10;
#     n=n//10;
#     i+=1;
#     print(qoldiq,end=" ")





# 18-misl
# n=int(input('n = '))
# i=0;
# sum=0;
# while n>0:
#     i+=1;
#     qoldiq=n%10;
#     n=n//10
#     sum+=qoldiq
# print(sum,i)

# 19-misol
# n=int(input('n = '))
# k=0;
# while n>0:
#     k+=1;
#     qoldiq=n%10;
#     n=n//10
#     print(qoldiq,end="")



# 20-misol
# n=int(input('n = '))
# k=0;
# while n>0:
#     k+=1;
#     qoldiq=n%10;
#     n=n//10;
#     if qoldiq==2:
#         print(True)
#         break
#     elif n==0:
#         print(False)
#         break


# 21-misol
# n=int(input('n = '))
# while n>0:
#     qoldiq=n%10
#     n//=10;
#     if qoldiq%2!=0:
#         print(True)
#         break
#     else:
#         print(False)
#         break


# 22-misol
# n=int(input('n = '))

# i=2
# while n%i!=0:
#     i+=1;
#     if n>i:
#         continue
#     else:
#         print(True)
#         break
# else:
#     print(False)


# 23-misol
# a,b=eval(input('a va b ni kiriting: '))
# i=1;
# a1,b1=a,b
# while a!=b:
#     i+=1;
#     if a>b:
#         a=a-b
#     elif b>a:
#         b=b-a
# else:
#     print("EKUB({},{}) = ".format(a1,b1),a)


# 24-misol
# n=eval(input('n = '))
# i=0
# a=[1,1]
# while n>i:
#     i+=1;
#     fib=a[i-1]+a[i]
#     a.append(fib)
#     if a[i]==n:
#         print(True)
        
#     else:
#         continue
#         print(False)
# print(a)


# 25-misol
# n=eval(input('n = '))
# i=1;
# a=[1,1]
# while a[i]<n:
#     i+=1;
#     fib=a[i-2]+a[i-1]
#     a.append(fib)
# print(a)
# print(fib)
    
        


# 26-misol
# n=eval(input('n = '))
# i=0;
# a=[1,1]

# while a[i]!=n:
#     i+=1;
#     fib=a[i-1]+a[i];
#     a.append(fib)
#     # print(a)
#     if a[i]>n:
#         print(0)
#         break
# else:
#     print(a[i+1],a[i-1])


# 27-misol
# n=eval(input('n = '))
# i=0
# a=[1,1]
# while a[i]!=n:
#     i+=1;
#     fib=a[i]+a[i-1]
#     a.append(fib)
#     # print(a)
#     if a[i]>n:
#         print(0)
#         break
# else:
#     print(i)
  


# 28-misol
# e=eval(input('e = '))
# i=1;
# list=[2,2.5]
# ak=2+1/2
# list.append(ak)
# print(list)
# while abs(list[i]-list[i-1])>e:
#     temp=(2+1/list[i])
#     i+=1;
#     list.append(temp)
# print(list[i-1],list[i],i+1)



#28-misol
# list = [2]
# e = float(input())

# while True:
#     list.append(2+1/list[-1])
#     if abs(list[-1]-list[-2])<e:
#         print(list[-2], list[-1], len(list))
#         break

# 29-misol
# e = eval(input('e = '))
# list=[1,2]

# while list[-1]!=e:
    
#     list.append((list[-2]+2*list[-1])/3)
    
#     if abs(list[-1]-list[-2])<e:
#         print(list[-2],round(list[-1],1),len(list))
#         break
    
# print(list)


# 30-misol
# a,b,c=eval(input('a,b,c = '))
# i=0;
# countb=0
# counta=0
# while a>=c or b>=c:
#     i+=1;
#     if a>=c:
#         counta+=1
#         a=a-c;
#     if b>=c:
#         countb+=1
#         b=b-c;

# print(counta*countb)







# 22-misol
# n = eval(input('n = '))
# i=1
# list=[]
# while n-1>i:
#     i+=1

#     if (n-1)%i==0:
#         print("tub emas")
#         break
#     else:
#         list.append(i)
# else:
#     print("tub")
# print(list)





















