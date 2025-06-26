
#this is a list of dictonaires
people = [
     {"name":"ali", "number ":"416"},
     {"name":"malak", "number ":"647"},
     {"name":"yassine", "number ":"905"}
]

name = input("give me name plz ")

# x[y["name"]] = is how you look inside a list of dictionaries

for person in people:
    if person["names"] == name:
        number = person["number"]
        print(f"found you mf your number {number}")
        break
else:
    print("your not in this mf")
# my_dict.update(new_data) or thisdict.update({"color": "red"}) to put add to dict
