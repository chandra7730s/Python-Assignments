# strip()
city=input("enter city name")
list=["hyd","Bng","chanai","gova"]
if city.strip() in list:
    print("it is availble")
else:
    print(city," not availble")

string="hello,world!"
stripped_string=string.strip()
print(stripped_string)

#rstrip()
orginal_string=" hello , world "
stripped_string=orginal_string.rstrip()
print("orginal string:",orginal_string)
print("stripped string:",stripped_string)

str1='aaaaahelloaaaa'
str1.rstrip()
print(str1)

#l strip()
str1='!!!!!hello!!!!!!!!'
str1.lstrip()
print(str1)
