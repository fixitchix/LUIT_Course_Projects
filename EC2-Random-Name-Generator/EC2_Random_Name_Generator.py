import random
import string

# Allowed departments list
allowed_departments = ["marketing", "accounting", "finops"]

# Function that generates random names
def generate_ec2_names():
    # Ask how many names
    num_instances = int(input("How many EC2 instance names would you like?\n"))

    # Ask which department
    department_name = input("What is the name of your department?\n")
    # Check if department is allowed
    if department_name not in allowed_departments:
        print("Sorry, that department does not have access to this name generator.")
        return

    # Set the characters to use
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

    # Length of each name
    name_length = 10

    print("Here are your EC2 instance names:\n")

    # Loop to generate and print names
    for i in range(num_instances):
        name = ""
        for j in range(name_length):
            name += random.choice(chars)
        print(f"{department_name}-{name}")

# Call the function to run it
generate_ec2_names()

