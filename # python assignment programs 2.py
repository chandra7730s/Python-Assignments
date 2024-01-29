# python assignment programs 2
# use a loop to display element from a given list at odd index position
given_list=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,len(given_list,),2):
    print(given_list[i])
  
# write a program to display all prime numbers within a range
def is_prime(num):
    if num<=1:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(num** 0.5)+ 1,2):
        if num %i==0:
            return False
        return True
    def display_primes(start,end):
        print(f"prime numbers between {start} and {end}:")
        for num in range(start,end+1):
            if is_prime(num):
                print(num,end=' ')
    start_range=int(input("enter the start of the range:"))
    end_range=int(input("enter the end of the range:"))
    display_primes(start_range,end_range)

#write a program to print multipication table of a given numbers
def multipication_table(number):
    for i in range(1,11):
        print(f"{number} x{i}={number * i}")
if __name__ =="__main__": 
   try:
       num=int(input("enter a number:"))
       multipication_table(num)
   except ValueError:
       print("plase enter a valid number.")

def calculate_cubes(n):
    cubes={}
    for i in range(1,n+1):
        cubes[i]=i**3
    return cubes
given_number=int(input("enter a number"))
cubes_dict=calculate_cubes(given_number)
print("cubes of numbers from 1 to", given_number,"are:")
for num, cube in cubes_dict.items():
    print(num,":",cube)
