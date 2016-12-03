print('Hello, Django girls!')

# name = 'Lauren'

# if name == 'Lauren':
#   print('Hey, Lauren!')
# elif name == 'Sonja':
#   print('Hey, Sonja!')
# else:
#   print('Hey, Anonymous!')

def hi(name):
  if name == "Lauren":
    print("Hi there, Lauren!")
  elif name == "Sonja":
    print ("How are you, Sonja?")
  else:
    print ("What's up, " + name + "?")

# hi("Bob")

girls = ["Rachel", "Monica", "Phoebe", "Ola", "Lauren"]

for name in girls:
  hi(name)
  print("Next girl")


for i in range (1,6):
  print(i)