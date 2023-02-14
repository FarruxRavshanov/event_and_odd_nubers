#A four-digit integer is given. Find the sum of odd digits in it.
num = 7799
#Create a variable "var_int" and assign it a four-digit integer value.
sum_odd = 0
#Create a variable "sum_even" and assign it 0.
x1 = num % 10
x2 = num // 10 % 10
x3 = num // 100 % 10
x4 = num // 1000
#Find the sum of the odd digits in the variable "var_int".
sum_odd = (x1 % 2) * x1 + (x2 % 2) * x2 + (x3 % 2) * x3 + (x4 % 2) * x4
print(sum_odd)