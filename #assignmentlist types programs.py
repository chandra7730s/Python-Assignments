#assignmentlist types programs
l=list(range(1,20,2))
print(l)
 
l=list(range(0,20,2))
print(l)

#list sliceing operator#
l=[10,23,45,67,[11,24],67]
print(l[4])

l=[10,20,30,[40,50],60,70,[80,90],100]
print(l[3],l[6])

# list lenght method
l=[10,20,30,40,50,60]
i=0
while i<len(l):
    print(l[i])
    i=i+1

l=[1,2,3,4,5,7]
for i in l:
    print(i)

#append()
#insert()
#extend()
l=[]
l.append(10)
l.append(20)
l.append(50)
print(l)

l=[1,2,3,4,5,7]
l.append("chandra")
print(l)
    
#insert()
l=[1,3,4,5,6,9,]
l.insert(24,678)
print(l)

l=[2,3,56,67,89]
l.insert(24,"chandra")
print(l)

#extend()
l1=["beera","visky","ramu"]
l2=["chicken","fish","prwns"]
l.extend("aman raju")
print(l1)
print(l2)

l=["chicken","fish","fry"]
l.extend("with fry")
print(l)

# remove
l1=["ajay","teja","kiran","ramu"]
l1.remove("ramu")
print(l1)

l1=[30,40,50,90]
l1.remove(30)
print(l1)
