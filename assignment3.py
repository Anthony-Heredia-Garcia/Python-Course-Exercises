people = [{'name': 'Anthony', 'age': 31, 'hobbies': ['cooking', 'gaming', 'coding']}, {'name': 'Aszalea', 'age': 28, 'hobbies': ['reading', 'gaming', 'design']}]

names = [person['name'] for person in people]

drinking_buddies = all([person['age'] >= 21 for person in people])

copy_of_people = people[:]
copy_of_people[0]['name'] = 'Tony'


person1, person2 = [person['name'] for person in people]

print(names)

print(drinking_buddies)

print(people)

print(copy_of_people)

print(person1, person2)
