import random

liste = []

for index in range(10):
    liste.append(random.randint(0, 100))

print(liste)

while True:
    try :
        index = int(input("Veuillez donner un index :"))
        print(liste[index])

        a = int(input("Donnez un premier nombre : "))
        b = int(input("Donnez un second nombre : "))
        print("Résultat :", a / b)
    except IndexError:
        print(f"ERREUR : L'index {index} est en dehors de la liste ([{-len(liste)}; {len(liste)-1 }])")

    except ValueError:
        print("ERREUR : La valeur saisie doit être un nombre ...")

    except ZeroDivisionError:
        print("ERREUR: La division par 0 est impossible")
