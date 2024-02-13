# tuple types methods
t=()
print(type(t))
# len method
t=(10,20,30,40)
print(len(t))

t=(10,"chandra","ramu",60)
for i in t:
    print(i)

t=(20,40,90,"raju")
for i in range(len(t)):
    print(i)
# count method
t=(10,20,30,40,50)
count=0
for i in t:
    count=count+1
print("element in ",count)

t=(10,20,30,40,90)
count=0
for i in t:
    count=count+1
print(t)

#index method
numbers=(10,30,40,50)
sorted_numbers=sorted("numbers")
print(numbers)

#tuple packing and unpacking
a=10 
b=20
c=30
d=40
f=a,b,c,d
print(f)
#tuple unpackind
t=(10,20,30,40)
a,b,c,d=t
print(t)

l=(x*x for x in range(10) if x%2==0)
print(i)

t=(10,30,40,50)
for i in l:
    print(i)

#set data types
s={10,20,30,40,}
print(s)

s={10,20,30,40}
s.add(15)
s.add(100)
s.add(78)
s.add(100)
print(s)

s={10,20,30,40,90}
s.update()
print(s)

s1={10,20,30,40}
s2=s1.copy()
print(s2)

#pop
s={10,20,30,40}
print(s.pop())
print(s.pop())
print(s.pop())

s={1,2,5,9}
print(s.pop())
print(s.pop())

#remove
s={12,34,56,89}
s.remove(34)
print(s)

s={34,45,67,89}
s.remove(34)
print(s)

#discard
s={10,20,30,40,50}
s.discard(140)
print(s)

s={10,34,56,90}
s.discard(10)
print(s)
# set
s={10,30,40,50,70,56}
s.clear()
print(s)

s={10,20,38,45,67,90}
s.clear(10)
print(s)
