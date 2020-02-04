name = 'Lana'
last_name = input('What is your last name?    ')
species = input('What is your species?        ')
eye_colour = input('What is your eye colour?       ')
hair_colour = input('What is your hair colour?      ')

print('Hello' + ' ' + name + ' ' + last_name + ' ' + 'you are a' + ' ' + species + '. ' + 'And you have' + ' ' + eye_colour + ' ' + 'eyes' + ' ' + 'and your colour hair is' + ' ' + hair_colour)

birth_year = input('In what year were you born?     ')

age = 2020 - int(birth_year)
print(age)
