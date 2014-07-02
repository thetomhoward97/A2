#clss definition
class VirtualPet:
    """a representaion of a pet"""
    #constructor-runs automaticaly
    def __init__(self,name):
        #attributes
        self.name = name
        self.hunger=10
        self.energy=1
        self.happiness=1
        print('Ive been born')

    #methods
    def talk(self):
        print("Hi, I'm {0}".format(self.name))

    def feed(self, food):
        self.hunger=self.hunger-1
        self.energy=self.energy+1
        self.happiness=self.happiness+1
        print('yummy!')

    def walk(self):
        self.energy=self.energy-1
        self.happiness=self.happiness+1
        
    def poke(self):
        print('Ouch!')

def feed_pet(pet_one):
        pet_one.feed('cake')
        print()
        print('{0}-{1}'.format('Hunger',pet_one.hunger))
        print('{0}-{1}'.format('Energy',pet_one.energy))
        print('{0}-{1}'.format('Happiness',pet_one.happiness))

def poke_pet(pet_one):
    pet_one.poke()
    print()
    print('{0}-{1}'.format('Hunger',pet_one.hunger))
    print('{0}-{1}'.format('Energy',pet_one.energy))
    print('{0}-{1}'.format('Happiness',pet_one.happiness))

def walk_pet(pet_one):
    pet_one.walk()
    print('{0}-{1}'.format('Energy',pet_one.energy))
    print('{0}-{1}'.format('Happiness',pet_one.happiness))

def display_main_menu():
    print()
    print('MAIN MENU')
    print()
    print('{0:2}{1}'.format('f-', 'feed'))
    print('{0:2}{1}'.format('p-', 'poke'))
    print('{0:2}{1}'.format('w-', 'walk'))
    print()
    choice = input('Please enter your choice: ')
    return choice

def main():
    #create an instance of the class
    name= input('Please enter your pets name: ')
    pet_one = VirtualPet(name)
    pet_one.talk()
    run_sim = True
    while run_sim == True:
        choice = display_main_menu()
        if choice == 'f':
            if pet_one.hunger > 0:
                feed_pet(pet_one)
            else:
                print('Im too full!')
        elif choice == 'p':
            poke_pet(pet_one)
        elif choice == 'w':
            if pet_one.energy >= 1:
                walk_pet(pet_one)
            else:
                print('Not enough energy')
        else:
            print('Please enter something from the menu.')


if __name__ == '__main__':
    main()
