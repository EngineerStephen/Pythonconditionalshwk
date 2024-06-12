#Code Correction 
number = int(input("Enter a number:"))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
    
   #2The Greatest showdown
print("Hello user, welcome to the GREATEST SHOWDOWN. Where our contemporary numbers exercise their BIGNESS! Follow the prompts below")

number1 = int(input("Please enter a number:")) 
number2 = int(input("How about another one?")) 
number3 = int(input("One last time:")) 

if number1 >= number2 and number3:
    print(f"{number1} is the greatest")
elif number2 >= number1 and number2:
    print(f"{number2} is the greatest")
else:
    print(f"{number3} is the greatest")
    