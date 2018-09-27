class Sword:
    def __init__(self, name):
        self.name = name
        self.enchant_level = 0
        self.probability = 100
        self.broken = False

    def __rper(self):
        return f'Sword : {self.name} id : {id(self)}'
