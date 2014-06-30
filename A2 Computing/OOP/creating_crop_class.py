import random

class Crop:
    """A generic food crop"""

    #constructor
    def __init__(self,growth_rate, light_need, water_need):
        #atribues

        self._growth=0
        self._days_growing=0
        self._growth_rate = growth_rate
        self._light_need=light_need
        self._water_need=water_need
        self._status = 'Seed'
        self._type='Generic'

    def needs(self):
        #return dictonary w light + water needed
        return {'light need':self._light_need, 'water need':self._water_need}

    #reports current state of crop
    def report(self):
        #returns dictonary
        return {'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}

    def _update_status(self):
        if self._growth > 15:
            self._status = 'Old'
        elif self._growth > 10:
            self._status = 'Mature'
        elif self._growth > 5:
            self._status = 'Young'
        elif self._growth > 0:
            self._status = 'Seeding'
        elif self._growth == 0:
            self._status = 'Seed'

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        #increment days
        self._days_growing += 1
        #udate status
        self._update_status()

def auto_grow(crop,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
    #get light + water values form user
    valid = False
    while not valid:
        try:
            light = int(input('Please enter a light value (1-10): '))
            if 1 <= light <= 10:
                valid = True
            else:
                print('Value entered not valid - please enter a value between 1 and 10')
        except ValueError:
            print('Value entered not valid - please enter a value between 1 and 10')
    valid = False
    while not valid:
        try:
            water = int(input('Please enter a water value (1-10): '))
            if 1 <= water <= 10:
                valid = True
            else:
                print('Value entered not valid - please enter a value between 1 and 10')
        except ValueError:
            print('Value entered not valid - please enter a value between 1 and 10')
    #grow crop
    crop.grow(light,water)

def display_menu():
    print('1. Grow manually over 1 day')
    print('2. Grow automaically over 30 days')
    print('3. Report status')
    print('0. Exit test program')
    print()
    print('Please select option from the above menu')

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input('option Selected: '))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print('Please enter a valid option')
        except ValueError:
            print('Please enter a valid option')
    return choice

def manage_crop(crop):
    print('This is the crop managemnt program')
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(crop)
            print()
        elif option == 2:
            auto_grow(crop,30)
            print()
        elif option == 3:
            print(crop.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print('Thank you for using the crop management program')
                

def main():
    #instantiate
    new_crop = Crop(1,4,3)
    manage_crop(new_crop)

if __name__ == '__main__':
    main()
