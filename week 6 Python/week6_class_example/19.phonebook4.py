import csv

file = open("phonebook.csv", "a") # opening file in append mode

#another way to opena file so that you dont have to close it is
                # "with open("phonebook.csv") as file :"

name = input("give name ")
number = input("gibe phone ")

writer = csv.writer(file) # creating a object called writer connected to the phonebook.csv file
# if i want to write in dictionaires i put:
                # "writer = csv.DictWriter(file, fieldnames = ["names", number])"


#this is how you use the object to write to the file
writer.writerow([name, number])
# with the dictonairy methode you would have to write :
                # "write.writerrow({"name" : name, "number : number"})"

file.close()
