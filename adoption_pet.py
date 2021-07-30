# A Python program to adopt a pet and appending the details in a file
import datetime

# Defining a function to get the current time
def time_stamp():
    return datetime.datetime.now()

# Defining main function
def get_pet(pet):

    # If user input 1 then this condition executes
    if pet==1:
        adopt = int(input("Press 1 for Pet Dog 2 for Pet Cat: \n"))

        if adopt==1:
            with open("Pet-Dog.txt", "a") as f:
                f.write(str([str(time_stamp())]) + ":" + f"{name_inp} just adopted a Dog. \n")
            print("Successfully Entered.")

        elif adopt==2:
            with open("Pet-Cat.txt", "a") as f:
                f.write(str([str(time_stamp())]) + ":" + f"{name_inp} just adopted a Cat. \n")
            print("Successfully Entered.")


        else:
            print("We have only CATS and DOGS.")

    # If usr input 2 then this condition executes
    elif pet==2:
        info = int(input("Enter 1 for Pet Dog Details 2 for Pet Cat Details: \n"))
        if info==1:
            with open("Pet-Dog.txt") as f:
                for content in f:
                    print(content, end='')

        elif info==2:
            with open("Pet-Cat.txt") as f:
                for content in f:
                    print(content, end='')

        else:
            print("Enter Valid Option!!")

    else:
        print("Choose 1 for adoption and 2 for Information...")

# ----------------------------**********---------------------------*******-----------------

print("------------ Welcome to Pet Adoption Center -----------")

# Username Input
name_inp = input("Enter your name: \n")

# Taking Input from users
user_input = int(input("Press 1 for Adoption 2 for Information: \n"))

# Conditions according to user input
if user_input==1:
    get_pet(user_input)
else:
    get_pet(user_input)







