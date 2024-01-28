# python assignment programs
# display number from a list using loop
number=[1,2,3,4,5,6,7,8]
for i in number:
    print(i)

#print list in revese order using loop
mylist=[12,34,56,14,67,89,90]
newlist=[]
for i in range(1,len(mylist)+1):
    newlist.append(mylist[-i])
print(newlist)

#write a program to display all prime number within  a range

#find the sum of the series upto n terms
def series_sum(n):
    sum=0
    for i in range(1, n+1):
        sum+=i
        return sum
    n=int(input("enter the number of terms:"))
    result=series_sum(n)
    print("sum of the series upto",n,"terms is:",result)

# reverse a given integer number
n=int(input("enter a number:"))
while n>0:
    r=n%10
    print(r,)
    n=n//10
    
#display nubers from -10 to -1 usinfg foor loop
for i in range(-10,0):
    print(i)
# count the total number of digits in a number
def count_digits(number):
    return len(str(number))
numbers=123456
total_digits=count_digits(number)
print("total number of digits:",total_digits)

#calculate the sum of all numbers from 1 to a given number


def sum_of_numbers(n):
    total_sum=0
    for i in range(1,n+1):
        total_sum+=1
        return total_sum
given_number=10
result=sum_of_numbers(given_number)
print("sum of numbers from 1 to",given_number, "is:",result)
    
    




