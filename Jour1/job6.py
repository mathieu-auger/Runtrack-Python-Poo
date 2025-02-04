class Animal():

    def __init__(self):
        self.age=0
        self.prenom=""

    def vieillir(self):
        print(self.age)
        self.age = self.age +1
        print(f'L age de l animal est {self.age}')

    def nommer(self, nom):
        self.prenom = nom
        print(f"l'animal se nomme {self.prenom}")

mon_animal = Animal()
mon_animal.nommer("luna")

mon_animal.vieillir()