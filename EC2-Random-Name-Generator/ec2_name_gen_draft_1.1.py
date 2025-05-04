import random

# List of characters: A-Z and 0-9 
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Ask the user how many ec2 instance names to generate
num_instance = int(input("How many ec2 instance names would you like to generate?\n"))

# Ask the user how long each ec2 instance name should be
name_length = int(input("How long should each ec2 instance name be?\n"))

# Ask the user what department they belong to
department_name = input('What is the name of your department?\n')

print("Here are your ec2 instance names:\n")

# Generate the ec2 instance names
for i in range(num_instance):
    name = ""
    for j in range(name_length):
        name += random.choice(characters)
    print(name)