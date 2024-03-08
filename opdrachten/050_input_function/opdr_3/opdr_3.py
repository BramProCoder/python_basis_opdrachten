# Opdracht 3 input functie
# Naam student:
# Groep:

# Vraag de gebruiker om een lijst van minimaal 5 objecten in te voeren
input_string = input("Voer minimaal 5 objecten gescheiden door komma's in: ")

# Maak een lijst van de ingevoerde objecten, gescheiden door komma's
objecten = input_string.split(", ")

# Sorteer de lijst op alfabetische volgorde met woorden die met "z" beginnen vooraan
objecten.sort(key=lambda x: (not x.startswith('z'), x))

# Print de gesorteerde lijst
print(objecten)



