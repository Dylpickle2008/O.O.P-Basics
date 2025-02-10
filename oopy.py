import random 

class Character:
    #class attributes
    hair_colors = ["blonde", "emo", "ginger", "waifu", "gray"]
    size = ["extra-small", "small", "medium", "large", "extra-large", "extra-extra-large"]
    special_powers = ["flying", "invisibility", "super-strength", "lasers", "telepathy"]
    gender = ["male", "female", "trans", "non-binary", "xenomorph"]
    bench = ["the bar", "135", "180", "225", "315", "500", "700"]



    #Constructor
    def __init__(self):
        self.generate_character():

    #This is the method() function:
    def generate_character(self):
        self.hair_colors = random.choice(Character.hair_colors)
        self.size = random.choice(Character.size)
        self.bench = random.choice(Character.bench)
        self.special_powers = random.choice(Character.special_powers)
        self.gender = random.choice(Character.gender)
        self.description = (
            f"Your character is {self.gender}, has {self.hair_colors} hair, "
            f"is {self.size} in size and has the power of {self.special_powers}."
            f"Your character bench presses: {self.bench}."
        ) 

    def __str__(self):
        return self.description

char1 = Character()
char2 = Character()
