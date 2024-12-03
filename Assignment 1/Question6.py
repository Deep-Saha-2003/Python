# Question6 #Assignment1 
# Two numbers are input through the keyboard into two locations C and D. Write a program to interchange the contents of C and D.

C = float(input("Enter first value: "))
D = float(input("Enter second value: "))

print(f"Before interchange of C = {C}, D = {D}")

# temparature = C
# C = D
# D = temparature

# or

C, D = D, C

print(f"After interchange C = {C}, D = {D}")