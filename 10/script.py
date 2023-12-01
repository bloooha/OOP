class Game:
    def __init__(self, name):
        self.name=name
    def show(self):
        print("Назва гри: "+self.name)

class Videogame(Game):
    def __init__(self,name,year,genre):
        super().__init__(name)
        self.year=year
        self.genre=genre
    @property
    def enter_name(self):
        return self.name
    def show(self):
        print(self.name + " %s"%self.year +" "+self.genre)
    @enter_name.setter
    def enter_name(self, name):
        self.name=name

ob=Videogame("Doom",2016, "fps")
ob.enter_name="DoomEternal"
ob.show()