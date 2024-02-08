# assignment programs list
# write down 4*4 matrix
x=[[10,20,30],[40,50,60],[70,80,90],[12,14,35]]
for i in x:
    print(i)
print("element in matrix style")
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=" ")
    print()

#print odd numbers in the range 0to30
for num in range(1,31,2):
    print(num)
#print even number in the range 1 to 30
for num in range(0,31,2):
    print(num)

#list comperhensive
l=[2*1,2*2,2*3,2*4,2*5]
l1=[]
for x in l:
    l1.append(x*x)
print(l1)

#compare string elements by using sort
l=["apple","banna","orange"]
l.sort()
print(l)

words=["balaya","shafi","chiru"]
output=''.join(word[0] for word in words)
print(output)
