from crop_class import *

class Potato(Crop):
    '''a potato crop'''

    #constructor
    def __init__(self):
        #call parent class
        #gowth 1, ligh 3, water 6
        super().__init__(1,3,6)
        self._type = 'Potato'

    #polymorthism
        def grow(self,light,water):
            if light >= self._light_need and water >= self._water_need:
                if self._status == 'Seedling' and water> self._water_need:
                    self._growth += self._growth_rate * 1.5
                elif self._status == 'Young' and water > self._water_need:
                    self._growth += self._gowth_rate * 1.25
                else:
                    self._growth += self._growth_rate
            # increment day
            self._days_growing += 1
            #udate status
            self._update_status()
                    

def main():
    #create new potato crop
    potato_crop = Potato()
    print(potato_crop.report())
    #manual gow
    manual_grow(potato_crop)
    print(potato_crop.report())

if __name__ == '__main__':
    main()
