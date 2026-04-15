class Parent:
    def afficher(self):
        print("Méthode de la classe Parent")

class Enfant(Parent):
    def afficher(self):
        print("Méthode de la classe Enfant")
        super().afficher()

# Test
obj = Enfant()
obj.afficher()