# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.


import math

print("Geef de lengte van de eerste zijde")
zijde1 = float(input())

print("Geef de lengte van de tweede zijde")
zijde2 = float(input())

schuine_zijde = math.sqrt(zijde1 ** 2 + zijde2 ** 2)

print("\nDe lengte van de schuine zijde is:", schuine_zijde)
