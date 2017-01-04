# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate():

    number = 0

    def drink_rum(self, number):
        self.number = number

    def hows_goin_mate(self):
        if self.number >= 5:
            print("Arrrr!")
        else:
            print("Nothin'")

pirate = Pirate()

pirate.drink_rum(2)
pirate.hows_goin_mate()
