members = [
    {"name": "Fiker", "house": "Tsehaye", "location":"Addis Ababa"},
    {"name": "Naomi", "house": "Birhanu", "location": "Johannesberg"},
    {"name": "Emma", "house": "Biniyam", "location":"Texas"},
]

for member in members:
    print (member["name"], member["house"], member["location"], sep = ", ")
