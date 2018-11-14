#Initializes the CellPhone class with a constructor (__init__) and six
#different methods.
class CellPhone:

    #Basic constructor that takes the attributes manufact, model, and
    #retail_price.
    def __init__(self, manufact='none', model='none', retail_price='none'):
        self.manufact = manufact
        self.model = model
        self.retail_price = retail_price

    #Method that takes an argument (manufact) and re-evalautes the dot notation
    #for that argument.
    def set_manufact(self, manufact):
        self.manufact = manufact
        return self.manufact

    #Method that takes an argument (model) and re-evalautes the dot notation
    #for that argument.
    def set_model(self, model):
        self.model = model
        return self.model

    #Method that takes an argument (retail_price) and re-evalautes the dot
    #notation for that argument.
    def set_retail_price(self, retail_price):
        self.retail_price = retail_price
        return self.retail_price

    #Returns the maunfacturer data for the cell phone.
    def get_manufact(self):
        return ('Manufacturer: %s' % self.manufact)

    #Returns the model number data for the cell phone.
    def get_model(self):
        return ('Model Number: %s' % self.model)

    #Returns the retail price data for the cell phone.
    def get_retail_price(self):
        return ('Retail Price: $%s' % self.retail_price)

if __name__ == '__main__':

    #Class initialization and tied to the variable cell
    cell = CellPhone()

    #This block of code asks for user entered data that is stored under
    #variables to later be called using dot notation in the class.
    new_manufact = str(input('Enter the manufacturer: ').strip())
    new_model = str(input('Enter the model number: ').strip())
    new_retail_price = str(input('Enter the retail price: ').strip())

    #Block of code calls certain methods in the class and uses the previous
    #variables as arguments.
    cell.set_manufact(new_manufact)
    cell.set_model(new_model)
    cell.set_retail_price(new_retail_price)

    print('Here is the data that you entered:')

    #Block of code calls certain methods that print out the user entered data
    print(cell.get_manufact())
    print(cell.get_model())
    print(cell.get_retail_price())
