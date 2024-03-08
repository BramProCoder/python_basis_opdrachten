# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

# Maak een lijst met de oorspronkelijke gasten
gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]

# Voeg jezelf toe aan de lijst
gasten.insert(0, "Bram")

# Print de lijst met gasten
print(gasten)

# Verwijder Marie uit de lijst
gasten.remove("Marie")

# Print de bijgewerkte lijst met gasten
print(gasten)

# Voeg George naast Kees toe
kees_index = gasten.index("Kees")
gasten.insert(kees_index + 1, "George")

# Print de uiteindelijke lijst met gasten
print(gasten)
