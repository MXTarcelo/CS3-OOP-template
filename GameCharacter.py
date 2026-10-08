class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    @property
    def health(self):
        return f"{self.name} has {self.__health} health points"

    @health.setter
    def health(self, health_points):
        if health_points % 10 == 0:
            self.__health = health_points
        else:
            print("health points should be an increments of 10")


hero = GameCharacter("Aline", 100)
print(hero.health)
hero.health = 2
print(hero.health)
