# this is a script i am making on my own where i go into every dir and and a file and delete it 
    #so that i can push empty dir to github

# importing os librarie to be able gives us functions for interacting with the operating 
    #system—like walking through directories, creating and deleting files
import os 

# this gives us the path of the root dir that we are in so = "C:\Users\alica\Desktop\coding\cs50" for us 
root_dir = os.path.abspath(".")

# Gather the list of first‐level subdirectories (skipping .git) and put it in a list called subdirs
subdirs = []

# List everything in root_dir except the git dir 
for name in os.listdir(root_dir):
            # os.listdir(root_dir) returns all names (files and folders) in root_dir

    # os.path.join(root_dir, name) builds the full path for each by 
        # joining the root dir "C:\Users\alica\Desktop\coding\cs50" to the end of one we have found example "Week 6 Python"
    path = os.path.join(root_dir, name)
   

    # Only act on directories, and skip .git
    if os.path.isdir(path) and name != ".git":
        subdirs.append(path)


"""
printing all subdir on a new line 
print(*subdirs, sep = "\n")
"""

# Name of the file we’ll create & delete
tmp = "temp.txt"

# Looping over all the list of dir 
for _ in subdirs:
    
    # Creating a path to tmp from joining each path found in the list and the tmp file name 
    tmp_path = os.path.join(_, tmp)

    # Creating the file by opening it in writing mode because the open function opens a file but if not found it creates 
    with open(tmp_path, "w", encoding="utf-8") as file:
       
        #this is the confirmation we created the file 
        print(f"Created: {tmp_path}")
       
        # we don't need to write anything
        pass


    # Deletes the file we crated 
    #os.remove(tmp_path)

    # Conferation of that we deleted the file 
    print(f"Deleted: {tmp_path}")




