import sys as np #using the nameplace np for the library sys

if len(np.argv) != 2:
    print ("no ones is here ")
    np.exit(1) # this is how you do exit Status
else:
    print(f"hey {np.argv[1]}")
    np.exit(0)
