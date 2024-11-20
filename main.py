import random

#Vytvoření pole s 10ti náhodnými hodnotami (0-100)
array = [random.randint(0, 100) for _ in range(10)]
print("ÚKOL 1-Původní pole:", array)

#Seřazení pole
sorted_array = sorted(array)
print("ÚKOL 1-Seřazené pole:", sorted_array)

#Budu pracovat na bubble sortu

array2 = [random.randint(0, 100) for _ in range(10)]
print("ÚKOL 2-Původní pole:", array2)

n = len(array2)
for i in range(n-1):
    for j in range(n-i-1):
        if array2[j] > array2[j+1]:
            array2[j], array2[j+1] = array2[j+1], array2[j]

print("ÚKOL 2-Bubble sorted pole:", array2)
