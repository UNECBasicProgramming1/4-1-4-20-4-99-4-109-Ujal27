#4.1a
a=float(input())
b=float(input())
print(max(a,b))
#4.1b
a=float(input())
b=float(input())
print(min(a,b))
#4.2
import math
x=int(input())
if x>0:y=math.sin(x)*math.sin(x)
else:y=1-2*math.sin(x*x)
print(y)
#4.3
import math
x=int(input())
if x>0:y=math.sin(x*x)
else:y=1+2*math.sin(x)*math.sin(x)
print(y)
#4.4
x=int(input())
y=int(input())
if x>4:print(2)
else:print(1)
#4.5
x=int(input())
y=int(input())
if y>3:print(1)
else:print(2)
#4.6a
x=int(input())
if x<=2:y=x
else:y=(2)
print(y)
#4.6b
x=int(input())
if x<=3:y=-x
else:y=(-3)
print(y)
#4.7
import math
x=int(input())
if math.sin(x)<0:k=x**2
elif math.sin(x)>=0:k=abs(x)
if k<x:f=k*x
else: f=k+x
print(f)
#4.8
import math
x=int(input())
if math.sin(x)>=0:k=x**2
elif math.sin(x)<0:k=abs(x)
if x<k:f=abs(x)
else: f=k*x
print(f)
#4.9
a=float(input())
b=float(input())
if a>b:print("maks:a,min:b")
else: print("maks:b,min:a")
#4.10
a=int(input())
b=int(input())
a=a*1000
b=b*0.3048
if a>b:print("b")
else: print("a")
#4.11
a=int(input())
b=int(input())
b=b*3.6
if a>b:print("a")
else: print("b")
#4.12
import math
a=int(input())
b=int(input())
a=a*a*math.pi
b=b*b
if a>b:print("a")
else: print("b")
#4.13
v1,v2=int(input()),int(input())
m1,m2=int(input()),int(input())
if m1/v1>m2/v2:print("1")
else:print("2")
#4.14
r1,r2=int(input()),int(input())
u1,u2=int(input()),int(input())
if u1/r1<u2/r2:print("1")
else:print("2")
#4.15
a=int(input())
b=int(input())
c=int(input())
if b*b-4*a*c>=0:print("yes")
else:print("no")
#4.16
a=int(input())
b=int(input())
c=int(input())
d=b*b-4*a*c
if d>0:
    x1=(-b+d**0.5)/(2*a)
    x2=(-b-d**0.5)/(2*a)
    print(x1,x2)
else:print("net korney")
#4.17
a,b=int(input()),int(input())
c,d=int(input()),int(input())
if b>=d:print(a-c)
else:print(a-c-1)
#4.18a
import math
s1,s2=int(input()),int(input())
if ((s1/math.pi)**0.5)*2<=s2**0.5:print("da")
else:print("net")
#4.18b
import math
s1,s2=int(input()),int(input())
if ((s1/math.pi)**0.5)*2>=s2**0.5:print("da")
else:print("net")
#4.19a
import math
s1,s2=int(input()),int(input())
r=math.sqrt((4*s2)/math.sqrt(3))*math.sqrt(3)/6
if s1<=math.pi*r*r:print("da")
else:print("net")
#4.19b
import math
s1,s2=int(input()),int(input())
R=(math.sqrt((4*s2)/math.sqrt(3))*math.sqrt(3))/3
if s1>=math.pi*R*R:print("da")
else:print("net")
#4.20
x1,y1,x2,y2=int(input()),int(input()),int(input()),int(input())
x3,y3,x4,y4=int(input()),int(input()),int(input()),int(input())
xmin=min(x1,x3)
ymin=min(y1,y3)
xmax=max(x2,x4)
ymax=max(y2,y4)
print(xmin,ymin,xmax,ymax)
#4.99a
a=float(input())
b=float(input())
if a>b:print("a")
if b>a:print("b")
#4.99b
a=float(input())
b=float(input())
if a>b:maks=a
maks=max(a,b)
print("max-",maks)
#4.100a
a=float(input())
b=float(input())
if a>b:print("a max b min")
if b>a:print("b max a min")
#4.100b
a=float(input())
b=float(input())
if a>b:maks=a
maks=max(a,b)
minn=min(a,b)
print("maks-",maks,"min-",minn)
#4.101a
a=float(input())
b=float(input())
c=float(input())
print(max(a,b,c))
#4.101b
a=float(input())
b=float(input())
c=float(input())
print(min(a,b,c))
#4.102a
a=float(input())
b=float(input())
c=float(input())
d=float(input())
print(max(a,b,c,d))
#4.102a
a=float(input())
b=float(input())
c=float(input())
d=float(input())
print(min(a,b,c,d))
#4.103
n=float(input())
if n>=0:print(n)
if n<0:print(-n)
#4.104a
a=float(input())
b=float(input())
if a>=0:a=a
else:a=-a
if b>=0:b=b
else:b=-b
print((a+b)/2)
#4.104b
a=float(input())
b=float(input())
if a>=0:a=a
else:a=-a
if b>=0:b=b
else:b=-b
print((a*b)**0.5)
#4.105
a=int(input())
b=int(input())
a=abs(a)
b=abs(b)
if a>b:print(a/2)
#4.106
a=int(input())
b=int(input())
if b**0.5<a:print(b*5)
#4.107
a=int(input())
b=int(input())
c=int(input())
if a%2==0:print(a)
if b%2==0:print(b)
if c%2==0:print(c)
#4.108
a=float(input())
b=float(input())
c=float(input())
if a%2==0:print(a*a)
if b%2==0:print(b*b)
if c%2==0:print(c*c)
#4.109
a=float(input())
b=float(input())
c=float(input())
if 1.6<=a<=3.8:print(a)
if 1.6<=b<=3.8:print(b)
if 1.6<=c<=3.8:print(c)