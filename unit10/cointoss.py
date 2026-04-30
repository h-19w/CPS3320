import random 

class coin:
    def __init__(self):
        self.__sideup = 'Heads'
        # private data attribute = __ before the name of the attribute.
        # prevents cheating by making it impossible to access the attribute directly from outside the class.

    def toss(self):
        if random.randint(0, 1) == 0: # randint determines the probabilities. 
            self.sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup
    
def main():
    
    coin1 = coin()
    coin2 = coin()
    coin1.toss()
    coin2.toss()
    print('coin 1: ', coin1.get_sideup())
    print('coin 2:', coin2.get_sideup())

if __name__ == "__main__":
    main()