iclass Animal:
    def __init__(self, leg_count):
        print('animal object was created')
        self._leg_count = leg_count

    def runs(self):
        print('running started')

    def num_of_legs(self):
        print(f'it has {self._leg_count}')

    def return_legs(self):
        return self._leg_count




dog = Animal('four legs')
print(dog.num_of_legs(), dog.return_legs(),sep='\n')
print(dog._leg_count)
