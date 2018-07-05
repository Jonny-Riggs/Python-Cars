showroom = {'bike', 'truck', 'car', 'motorcylcle'}

print(showroom)

print(len(showroom))

showroom.add('truck')

showroom_new = {'plane', 'boat'}

showroom.update(showroom_new)

print(showroom)

showroom.discard('plane')

print(showroom)

junkyard = {'racecar', 'boat', 'trike'}

print(showroom.intersection(junkyard))

print(showroom.union(junkyard))

print(showroom.discard('boat'))