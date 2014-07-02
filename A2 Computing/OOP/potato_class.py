from crop_class import *

class Potato(Crop):
    '''a potato crop'''

    #constructor
    def __init__(self):
        #call parent class
        #gowth 1, ligh 3, water 6
        super().__init__(1,3,6)
        self._type = 'Potato'

def main():
    #create new potato crop
    potato_crop = Potato()
    print(potato_crop.report())
    #manual gow
    manual_grow(potato_crop)
    print(potato_crop.report())

if __name__ == '__main__':
    main()
