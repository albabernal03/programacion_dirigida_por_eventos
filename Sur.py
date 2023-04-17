    
class Surtidor:
    def __init__(self, id):
        self.id = id
        self.ocupado = False

    def __str__(self):
        return "Surtidor " + str(self.id) + " " + ("ocupado" if self.ocupado else "libre")