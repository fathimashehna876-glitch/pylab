class Father:
    def skills(self):
        print("Father: Gardening, Programming")
class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child: Dancing, Singing")
c = Child()
c.skills()
