class Tamagotchi:
    def __init__(self):
        self.hunger_lvl = 50
        self.happiness_lvl = 50

    def feed(self):
        self.hunger_lvl += 10
        if self.hunger_lvl >= 100:
            self.hunger_lvl = 100
        if self.hunger_lvl <= 0:
            self.hunger_lvl = 0

    def play(self):
        self.happiness_lvl += 10
        if self.happiness_lvl >= 100:
            self.happiness_lvl = 100
        if self.happiness_lvl <= 0:
            self.happiness_lvl = 0

    def update(self):
        self.hunger_lvl -= 0.1
        self.happiness_lvl -= 0.1
