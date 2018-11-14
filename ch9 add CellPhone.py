class CellPhone:
    def __init__(self, manufact, model, retail_price):
        self.manufact = manufact
        self.model = model
        self.retail_price = float(retail_price)

    def set_manufact(manufact):
        self.manufact = manufact

    def set_model(model):
        self.model = model

    def set_retail_price(retail_price):
        self.retail_price = retail_price

    def get_manufact(self):
        return ('{}'.format(self.manufact))

    def get_model(self):
        return ('{}'.format(self.model))

    def get_retail_price(self):
        return self.retail_price

manufact = input('Enter the manufacturer: ')
model = input('Enter the model number: ')
retail_price = float(input('Enter the retail price: '))
phone1 = CellPhone(manufact, model, retail_price)

print('Here is the data you entered:')
print('Manufacturer: {}'.format(phone1.get_manufact()))
print('Model number: {}'.format(phone1.get_model()))
print('Model number: ${:.2f}'.format(phone1.get_retail_price()))
