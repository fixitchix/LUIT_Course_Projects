import random
import string

# Define the length of the string
name_length = 10

# Define the amount or instances needed
num_instances = int(input('How many ec2 instance names would you like?\n'))

# Define the department name
department = input('Please enter the name of your department?\n')
print('-------------------')


# Uppercase,lowercase and numbers to use for random instance names
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

#Generate random string
random_name = ''.join(random.choice(chars) for i in range(name_length))

# Set to store unique EC2 names (set ensures no duplicates)
random_name = set()

for i in range(num_instances):
    name = ""
    for j in range(name_length):
        name += random.choice(chars)
    print(name)

print('--------------------')
