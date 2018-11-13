#Initializes the class ItemToPurchase with a constructor (__init__) and method
#(print_item_cost).
class ItemToPurchase:
    
    #Default class constructor with three atributes, item_name, item_price,
    #and item_quantity which all have default values.
    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    #Class method that uses the earlier atributes to print out item name, price
    #and quantity, as well as calculating and printing the total price.
    def print_item_cost(self):
        return ('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, (self.item_price * self.item_quantity)))
        

#if branch to check __main__ section of the file.
if __name__ == "__main__":
    
    #Block of code prints out formatted section that asks the user to enter
    #information about an item, and stores those entries under variables.
    print('Item 1')
    item1_name = str(input('Enter the item name:\n').strip())
    item1_price = float(input('Enter the item price:\n').strip())
    item1_quantity = int(input('Enter the item quantity:\n').strip())
    
    #Calling of the class using the user entered variables as atributes.
    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

    #Block of code prints out formatted section that asks the user to enter
    #information about an item, and stores those entries under variables.
    print('\nItem 2')
    item2_name = str(input('Enter the item name:\n').strip())
    item2_price = float(input('Enter the item price:\n').strip())
    item2_quantity = int(input('Enter the item quantity:\n').strip())
    
    #Calling of the class using the user entered variables as atributes.
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    #Block code prints out the total cost of the two entered items, as well as
    #the prices, names,and quantities of each item.
    print('\nTOTAL COST')
    print(item1.print_item_cost())
    print(item2.print_item_cost())
    print('\nTotal: $%d' % (float((item1_price * item1_quantity)) + float((item2_price * item2_quantity))))
