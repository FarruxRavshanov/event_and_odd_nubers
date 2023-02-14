#A four-digit integer is given. Find the number of even digits in it.
num = 7777
#Create a variable "var_int" and assign it a four-digit integer value.
x1 = num % 10
x2 = num // 10 % 10
x3 = num // 100 % 10
x4 = num // 1000
#Print the number of even digits in the variable "var_int".
print(x1 % 2 + x2 % 2 + x3 % 2 + x4 % 2)