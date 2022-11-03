names = ['Anthony', 'Aszalea', 'Pumpkin', 'Loaf', 'Squeak', 'Mew']
for name in names:
  if len(name) > 5 and ('n' or 'N') in name:
    print(name)
    print(len(name))

while len(names) > 0:
  names.pop()

print(names)