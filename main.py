import random

#Vytvoření pole s 10ti náhodnými hodnotami (0-100)
array = [random.randint(0, 100) for _ in range(10)]
print("Původní pole:", array)

#Seřazení pole
sorted_array = sorted(array)
print("Seřazené pole:", sorted_array)