class Animal:
    '''A generic animal class'''

    def __init__(self, name, growth_rate, food_need, water_need):

        self._name = name
        self._weight = 1
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = 'Baby'
        self._type = 'Generic'

    def needs(self):
        return {'food need':self._food_need, 'water_need':self._water_need}

    def report(self):
        return {'name':self._name, 'type':self._type, 'status':self._status, 'weight':self._weight, 'days growing':self._days_growing}

    def update_status(self):
        if self._weight > 16:
            self._status = 'Old'
        elif self._weight > 11:
            self._status = 'Adult'
        elif self._weight > 6:
            self._status = 'Young Adult'
        elif self._weight > 1:
            self._status = 'Young'
        elif self._weight == 1:
            self._status = 'Baby'

    def grow(self
