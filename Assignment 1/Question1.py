# Q1. Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary.

b_salary = float(input("Enter Basic salary of Ramesh: "));
d_a = 0.4 * b_salary;
house_rent = 0.2 * b_salary;
gross_salary = b_salary + d_a + house_rent;
print(f"Gross salary of Ramesh: {gross_salary}");