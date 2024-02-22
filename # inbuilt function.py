# inbuilt function 
def wish():
    print("hello hi")
wish()
wish()
wish()

def friend():
    print("hello where are you")
friend()
friend()
friend()
friend()

def champion():
    print("best wish")
champion()
champion()

def squ(x):
    print(x,x*x)
squ(20)
squ(30)

def sum(x):
    print(x,x%x)
sum(10)
sum(5)

def squ(x):
    print(x,x&x)
squ(10)
squ(15)

def evenodd(x):
    if x%2==0:
        print(x,"even")
    else:
        print(x,"odd")

evenodd(10)
evenodd(1)

def num (x):
    t=0
    for i in range(2,num):
        t=1
        break
        if i%2==0:
            print(x,"even")
        else:
            print(x,"odd")
evenodd(3)
evenodd(12)

#position arguement
def sub(x,y):
    print(x-y)
sub(10,20)

def sub(x,y):
    print(x-y)
sub(20,5)

def sub(x,y):
    print(x*y)
sub(20,9)
#keyword arguement
def wish(name,msg):
    print("hi",name,msg)
wish(name="raju",msg="hello hi ra")
    
def wish (name,msg,age):
    print(name,msg,age)
wish(name="ramu",msg="good boy",age=20)

#varaible length
def sum(*a):
    print(a)
sum(20)
sum(40)
sum(60)
   
def sum (*a):
    result=0
    for i in a:
        result=result+i
    print(result)
sum(10,20,30,40,50,70)

def sum(*a):
    count=0
    for x in a:
        count=count+x
    print(count)
sum(1,2,3,4,56,78,9)


def f1(arg1,arg2,arg3=6):
    print(arg1,arg2,arg3)
f1("hello")

def f1(arg1,arg3=6):
    print(arg1,arg3)
f1(10,30,40,50,60)
    
def f1(arg1,arg2,arg3=6):
    print(arg1,arg2,arg3)
f1(10.20.30.)