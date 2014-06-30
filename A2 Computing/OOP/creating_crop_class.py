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
        
def main():
    #instantiate
    new_crop = Crop(1,4,3)
    #test
    print(new_crop.needs())
    print(new_crop.report())
    new_crop.grow(4,4)
    print(new_crop.report())

if __name__ == '__main__':
    main()
