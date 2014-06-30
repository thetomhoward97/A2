#clss definition
class VirtualPet:
    """a representaion of a pet"""
    #constructor-runs automaticaly
    def __init__(self,name):
        #attributes
        self.name = name
        self.hunger=10
        self.energy=1
        print('Ive been born')

    #methods
    def talk(self):
        print("Hi, I'm {0}".format(self.name))

    def feed(self, food):
        self.hunger=self.hunger-1
        self.energy=self.energy+1
        print('yummy')

def main():
    #create an instance of the class
    name= input('Please enter your pets name: ')
    pet_one = VirtualPet(name)
    pet_one.talk()
    choice = input('f-feed,p-poke,')
    if choice == 'f':
        pet_one.feed('cake')
        print('{0}-{1}'.format('hunger',pet_one.hunger))
        print(pet_one.energy)
    elif choice == 'p':
        print(pet_one.hunger)
        print(pet_one.energy)

if __name__ == '__main__':
    main()
