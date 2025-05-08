# class created
class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self): # base method for sound
        print ("sound")

    
class dog(animal): #subclass of animal
    def make_sound(self): # overriding the base method to print specific sound
        print (f" {self.name} a {self.species} woofs")
    
class horse(animal): 
    def make_sound(self): # overriding the base method to print specific sound
         print (f" {self.name}, an {self.species} neighs ")
class baboon(animal):
    def make_sound(self): # overriding the base method to print specific sound
        print(f" {self.name}, a {self.species} makes the sound, hoo hoo hoo haa haa haa!")


#instances created
dog1=dog("boscow", "german shepherd")
horse1=horse("bobby", "arabian horse")
baboon1=baboon("george", "congolese baboon")

#methids implemented
dog1.make_sound()
horse1.make_sound()
baboon1.make_sound()
