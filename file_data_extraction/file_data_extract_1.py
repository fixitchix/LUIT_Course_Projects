import os

# Get our cwd
cwd = os.getcwd()

# Get a list of files in our cwd
files = os.listdir(cwd)

# Create empty list to store our cwd file info.
file_dictionary_list = []

# Iterate each file in our cwd
for file_name in files:

    # Get the full path of the file
    full_path = os.path.join(cwd, file_name)
    
    # Check if it's a file and NOT a directory
    if os.path.isfile(full_path):
        
        # Get the file size
        file_size = os.path.getsize(full_path)
        
        # Get file creation info.
        file_creation = os.path.getctime(full_path)
      
        # Create dictionary with file information
        file_info = {
            "file_name": file_name,
            "file_path": full_path,
            "file_size": file_size,
            "file_creation": file_creation
        }

        # Add file info. to the dictionary list
        file_dictionary_list.append(file_info)

# Print the file information
for file_info in file_dictionary_list:
    print(file_info)