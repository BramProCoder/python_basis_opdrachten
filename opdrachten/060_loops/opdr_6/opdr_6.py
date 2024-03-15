pizza_lijst = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']
print(pizza_lijst)

#sorteer
pizza_lijst.sort()
print(pizza_lijst)

pizza_lijst.append('beste-pizza-in-de-game')
print(pizza_lijst)

pizza_lijst.remove('olivio')
print(pizza_lijst)

print(pizza_lijst[:3])

print([pizza_lijst[len(pizza_lijst)//2]])

print(pizza_lijst[-3:])