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


from math import pi

# alfa1 va alfa2 burchakar birxi qiymat qabu qiadi
alfa=eval(input('alfa burchakni kirting: ( gradus) '))
radius=eval(input('radiusni kiriting: '))
betta, w =eval(input('tirqish va magnit singdiruvchanligi kiriting: '))
# s1, s2 va s3 s1=s2=s3 bir xi qiymat qabu qiadi va bularni umumiy s deb olamiz;
a,b,c=eval(input('qalinliklarni kiriting: '))
s0=a*b;
s=b*c;
magnitDoimisi=4*pi*(pow(10,-7));
v,I=eval(input('  sonini va tok kuchini kiriting: '))

if alfa==0:
    R0=betta/(w*magnitDoimisi*s0);
    l1=alfa*(pi/180)*radius;
    l2=alfa*(pi/180)*radius;
    R1=l1/(w*magnitDoimisi*s);
    R2=l2/(w*magnitDoimisi*s);
    R3=2*radius/(w*magnitDoimisi*s);
    Rumumiy1=(2*R0+R3+R1+R2);
    F=(v*I)/Rumumiy1;
    print("R = ", Rumumiy1,"F = ",F,R1,R2,R3,R0,sep='\n')
elif alfa>0 and alfa<=45:
    R0=betta/(w*magnitDoimisi*s0);
    l1=alfa*(pi/180)*radius;
    l2=alfa*(pi/180)*radius;
    R1=l1/(w*magnitDoimisi*s);
    R2=l2/(w*magnitDoimisi*s);
    R3=2*radius/(w*magnitDoimisi*s);
    Rumumiy2=(2*R0+R3+R1+R2);
    F=(v*I)/Rumumiy2;
    print(Rumumiy2)
elif alfa>45 and alfa<90:
    R0=betta/(w*magnitDoimisi*s0);
    l1=alfa*(pi/180)*radius;
    l2=alfa*(pi/180)*radius;
    R1=l1/(w*magnitDoimisi*s);
    R2=l2/(w*magnitDoimisi*s);
    R3=2*radius/(w*magnitDoimisi*s);
    Rumumiy3=(2*R0+R3+R1+R2);
    F=(v*I)/Rumumiy3;
    print(Rumumiy3)
elif alfa==90:
    R0=betta/(w*magnitDoimisi*s0);
    l1=alfa*(pi/180)*radius;
    l2=alfa*(pi/180)*radius;
    R1=l1/(w*magnitDoimisi*s);
    R2=l2/(w*magnitDoimisi*s);
    R3=2*radius/(w*magnitDoimisi*s);
    Rumumiy4=(2*R0+R3+R1+R2);
    F=(v*I)/Rumumiy4;
    print(Rumumiy4)
elif alfa>90 and alfa<=115:
    R0=betta/(w*magnitDoimisi*s0);
    l1=alfa*(pi/180)*radius;
    l2=alfa*(pi/180)*radius;
    R1=l1/(w*magnitDoimisi*s);
    R2=l2/(w*magnitDoimisi*s);
    R3=2*radius/(w*magnitDoimisi*s);
    Rumumiy5=(2*R0+R3+R1+R2);
    F=(v*I)/Rumumiy5;
    print(Rumumiy5)
elif alfa>115 and alfa<=150:
    R0=betta/(w*magnitDoimisi*s0);
    l1=alfa*(pi/180)*radius;
    l2=alfa*(pi/180)*radius;
    R1=l1/(w*magnitDoimisi*s);
    R2=l2/(w*magnitDoimisi*s);
    R3=2*radius/(w*magnitDoimisi*s);
    Rumumiy6=(2*R0+R3+R1+R2);
    F=(v*I)/Rumumiy6;
    print(Rumumiy6)
elif alfa>150 and alfa<180:
    R0=betta/(w*magnitDoimisi*s0);
    l1=alfa*(pi/180)*radius;
    l2=alfa*(pi/180)*radius;
    R1=l1/(w*magnitDoimisi*s);
    R2=l2/(w*magnitDoimisi*s);
    R3=2*radius/(w*magnitDoimisi*s);
    Rumumiy7=(2*R0+R3+R1+R2);
    F=(v*I)/Rumumiy7;
    print(Rumumiy7)
else:
    print("Xato bajardingiz! ")
