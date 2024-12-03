# Question7 #Assignment1 
#If a five-digit number is input through the keyboard, write a program to calculate the sum of its digits.(Hint: Use the modulus operator ‘%’) Input a five-digit number

number = int(input("Enter a five-digit number: "))

# Checking if the number is a valid five-digit number
if 10000 <= number <= 99999:
    sum_of_digits = 0
     # Storing the original number for later display
    original_number = number
    while number > 0:
        # Get the last digit
        digit = number % 10 
         # Add it to the sum     
        sum_of_digits += digit   
        # Remove the last digit 
        number //= 10             
    print(f"The sum of the digits of {original_number} is: {sum_of_digits}")
else:
    print("Please enter a valid five-digit number!")