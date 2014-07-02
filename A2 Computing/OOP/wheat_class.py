from crop_class import *

class Wheat(Crop):
    '''a wheat croo'''

    def __init__(self):
        super().__init__(2,5,6)
        self._type='Wheat'

        def grow(slef,light,water):
            if light >= self._light_need and water >= self._water_need:
                if self._status == 'Seedling' and light > self._light_need:
                    self._growth += self._growth_rate * 1.5
                elif self._status == 'Young' and light > self._light_need:
                    self._growth += self._gowth_rate * 1.25
                else:
                    self._growth += self._growth_rate
            self._days_growing += 1
            self._update_status()

def main():
    wheat_crop = Wheat()
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == '__main__':
    main()
