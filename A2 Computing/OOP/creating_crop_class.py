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
    
def main():
    #instantiate
    new_crop = Crop(1,4,3)
    #test
    print(new_crop.needs())
    print(new_crop.report())

if __name__ == '__main__':
    main()
