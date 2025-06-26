#gives argv list when importing from the sys library works similar to c but dont have to create the parameter in the main method

from sys import argv

if len(argv) == 2:
    print(f"hey its mf {argv[1]}")
else:
    print("theres no one to say hi to :( )")
