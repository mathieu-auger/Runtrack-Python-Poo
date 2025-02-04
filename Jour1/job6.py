class Animal():

    def __init__(self,age,prenom):
        self.age=age
        self.prenom=prenom

    def vieillir(self):
        self.age=0
        print(f'L age de l animal est {self.age}')
        self.age=1
        print(f'L age de l animal est {self.age}')

    def nommer(self):
        self.prenom='luna'
        print(f'l animal se nomme {self.prenom}')

age=Animal('0','1')
age.vieillir()
prenom=Animal('1','luna')
prenom.nommer()