class Airplane:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.is_flying = False
        self.descriptive_name = print(self.make + ' ' + self.model + ' ' + self.year)
    
    def take_off(self):
        self.is_flying = True
        print('The plane takes off')

    def fly (self,km):
        self.odometer += km

    def land(self):
        self.is_flying = False
        print('The plane does not fly')

change = Airplane('Boening', '555' , '2015')
change.descriptive_name
print(change.odometer)
print(change.is_flying)
change.take_off()
print(change.is_flying)
change.fly(100)
print(change.odometer)
change.land()
print(change.is_flying)
##как найти расстояние полета и изменять показания

