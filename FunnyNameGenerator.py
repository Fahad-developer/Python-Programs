import sys
import random

print("Welcome to funny name generator.")
print("Programmed by Muhammad Fahad.")

first = ["Ziggy", "Fanny", "Buddy", "Gizmo", "Sparkey", "Fluffy",
         "Squishy", "Waldo", "Cheddar", "Peanut"]

last = ["toothbrush", "toothpaste", "Shampoo", "Conditioner", "Soap",
        "body wash", "razor", "shaving cream", "deodorant", "perfume"]

while True:
 firstName = random.choice(first)
 lastName = random.choice(last)
 print("{} {}".format(firstName, lastName), file=sys.stderr)
 print("\n\n")

 try_again = input("\n\nTry again? (Press Enter else n to quit.)\n")
 if try_again.lower() == "n":
  break

input("\n Press Enter to Exit.")
