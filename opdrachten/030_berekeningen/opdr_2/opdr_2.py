# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

c = -12
f = 144

# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9//5) + 32
    print(f"{celsius} graden Celsius is gelijk aan {fahrenheit} graden Fahrenheit")

# Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5//9
    print(f"{fahrenheit} graden Fahrenheit is gelijk aan {celsius} graden Celsius")

# Test the functions
celsius_to_fahrenheit(-12)
fahrenheit_to_celsius(144)
celsius_to_fahrenheit(62.2)
fahrenheit_to_celsius(96)
print()