def inches_to_feet(inches):
  feet = inches / 12
  return feet

# Read inches from the user
inches = float(input("Enter a value in inches: "))

# Convert inches to feet
feet = inches_to_feet(inches)

# Print the result
print(inches,'inches is equivalent to =',feet, 'feet.')


