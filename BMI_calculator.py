# A simple BMI calculator for beginners

# Python program to calculate BMI ( Body Mass Index)
'''
If your BMI is less than 18.5, it falls within the underweight range.
If your BMI is 18.5 to <25, it falls within the healthy weight range.
If your BMI is 25.0 to <30, it falls within the overweight range.
If your BMI is 30.0 or higher, it falls within the obesity range.
'''

print("--------Calculate your BMI (Body Mass Index)--------")

# Taking input from user
height_input = int(input("Enter your Height(in cms): \n"))
weight_input = int(input("Enter your Weight(in Kgs): \n"))

# Created a function to calculate BMI
def calculate_bmi(height, weight):
    # round function is used to round off the output
    return round(((weight/height/height) * 10000), 2)

# Passing the argument taken from user
bmi = calculate_bmi(height_input, weight_input)
# Printing the BMI
print(f"Your BMI is {bmi}")

print("***********************************************\n")
# Defining the conditions according to the BMI output
if bmi < 18.5:
    print("You are Underweight.")
elif bmi == 18.5 or bmi < 25:
    print("You are Healthy.")
elif bmi == 25 or bmi < 30:
    print("You are Overweight.")
else:
    print("You are in Obesity range.")
