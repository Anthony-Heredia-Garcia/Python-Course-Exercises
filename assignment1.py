
name = input('What is your name? ')
age = input('What is your age? ')

print('Hello ' +name+'. Your age is '+age+'.')

def decades(age):
  decade_num = age//10
  print('You have lived for '+str(decade_num)+' decades.')

decades(int(age))