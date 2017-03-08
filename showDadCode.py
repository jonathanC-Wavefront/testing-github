familyMembers = ['emma', 'jonathan', 'david', 'maria', 'olivia']

print(familyMembers)

sentence = "Today at the wedding I saw emma, jonathan, and david. Later I saw olivia and maria."

print(sentence)

for i in range(len(familyMembers)):
    sentence = sentence.replace(familyMembers[i], (familyMembers[i] + ' Claypool'))

print(sentence)

#I love my family
