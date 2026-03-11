import random

liste = []

for index in range(10):
    liste.append(random.randint(0, 100))

print(liste)

while True:
    try :
        index = int(input("Veuillez donner un index :"))
        print(liste[index])
    except IndexError:
        print(f"ERREUR : L'index {index} est en dehors de la liste ([{-len(liste)}; {len(liste)-1 }])")
