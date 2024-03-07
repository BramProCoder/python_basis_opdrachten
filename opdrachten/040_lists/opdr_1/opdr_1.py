# Opdracht 1 lists
# Naam student:
# Groep:
# Maak een lijst aan
# Maak een lege lijst aan
lijst = []

# Maak 4 dictionaries om gegevens van personen op te slaan
persoon1 = { "id": 1, "voornaam": "John", "achternaam": "Doe" }
persoon2 = { "id": 2, "voornaam": "Jane", "achternaam": "Smith" }
persoon3 = { "id": 3, "voornaam": "Alice", "achternaam": "Johnson" }
persoon4 = { "id": 4, "voornaam": "Bob", "achternaam": "Brown" }

# Voeg de dictionaries toe aan de lijst met behulp van de append-methode
lijst.append(persoon1)
lijst.append(persoon2)
lijst.append(persoon3)
lijst.append(persoon4)

# Print de volledige naam van de 2e persoon op het scherm
print(lijst[1]["voornaam"], lijst[1]["achternaam"])

