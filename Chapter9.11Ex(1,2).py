#Initilization of the class ItemToPurchase with a constructor (__init__) and two methods.
class ItemToPurchase:

    #Basic constructor with the attributes item_name, item_price, item_quantity, and item_description.
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        
    #Definition of the method print_item_cost which uses the instances created by the constructor
    #to print out various details about each item.
    def print_item_cost(self):
        string = ('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price,
                                         (self.item_quantity * self.item_price)))
                  
        cost = self.item_quantity * self.item_price
        return string, cost

    #Definition of the method print_item_description which uses an instance created by the constructor
    #to print out the item's name and description.
    def print_item_description(self):
        string = ('%s: %s' % (self.item_name, self.item_description))
        print(string, end='\n')
        return string

#Initialization of the class ShoppingCart which has a constructor (__init__) and several methods
#that are used to modify certain aspects of the cart and the items in the cart.
class ShoppingCart:

    #Basic constructor with the attributes customer_name, current_date, and cart_items.
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    #Definition of the method add_item which adds an item to the "shopping cart" (cart_items list).
    def add_item(self, string):
        print('\nADD ITEM TO CART', end='\n')

        #Block of code takes user input and stored them under seperate values to later be used to call
        #the class ItemToPurchase.
        item_name = (str(input('Enter the item name:')))
        item_description = str(input('\nEnter the item description:'))
        item_price = int(input('\nEnter the item price:'))
        item_quantity = int(input('\nEnter the item quantity:\n'))

        #Appends the various specifics of the added item to the cart_items list through calling the
        #ItemToPurchase class.
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    #Definition of the method remove_item which removes an item from the cart_items list.
    def remove_item(self):
        print('\nREMOVE ITEM FROM CART', end='\n')
        #Takes user input of what item to remove. Later used in a for loop to search the
        #"cart" for the specific item.
        string = str(input('Enter name of item to remove:\n'))
        #Initialize a variable to increment for the searching of the item in for loop
        i = 0

        #for loop used to iterate through cart_items to search for, and delete the user
        #entered item. If not found, sets a flag to True and prints out an Error message.
        for item in self.cart_items:
            if(item.item_name == string):               
                del self.cart_items[i]
                i += 1
                empty = False
                break
            else:
                empty = True

        if(empty == True):
            print('Item not found in cart. Nothing removed.')

    #Definition of the method modify_item which enables the user to change certain specifics
    #of an item already in the cart.
    def modify_item(self):
        print('\nCHANGE ITEM QUANTITY', end='\n')
        #Takes user input for name of item that is desired to be modified.
        name = str(input('Enter the item name: '))

        #Uses a for loop to iterate through cart_items in search of user entered item.
        #If the item is not found, sets a flag to True and prints an Error message.
        for item in self.cart_items:
            if(item.item_name == name):
                #Takes new user entered quantity to be changed.
                quantity = int(input('Enter the new quantity: '))
                item.item_quantity = quantity
                empty = False
                break
            else:
                empty = True
                  
        if(empty == True):
            print('Item not found in cart. Nothing modified.')

    #Definition of the method get_num_items_in_cart which counts up the quantities of
    #all items present in the cart, and outputs.
    def get_num_items_in_cart(self):
        #Initialize variable to increment in loop (total count of items in cart).
        num_items = 0

        #for loop iterates through cart_items and increments the count of items
        #by each quantity of items in the cart.
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
            
        return num_items

    #Definition of the method get_cost_of_cart which totals up the prices of all of
    #the items in the cart and outputs.
    def get_cost_of_cart(self):
        #Initialize two variables to increment in the for loop.
        total_cost = 0
        cost = 0

        #for loop to iterate through cart_items that totals the prices of each items
        #and increments it to a total_cost variable.
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
            
        return total_cost

    '''Definition of the print_total method which prints out the cart and the specifics
    of each item, as well as the total price (references another method for shorter file).
    Prints out Error message if the cart is empty.'''
    def print_total():
        total_cost = get_cost_of_cart()
        
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            output_cart()

    #Definition of the print_descriptions method which iterates through the cart anf outputs
    #each item's name and description.
    def print_descriptions(self):
        print('\nOUTPUT ITEMS\' DESCRIPTIONS')
        print(('%s\'s Shopping Cart - %s' % (self.customer_name, self.current_date)),end='\n')
        print('\nItem Descriptions', end='\n')

        #for loop used to iterate through cart_items to print out item's names and descriptions
        for item in self.cart_items:
            print(('%s: %s' % (item.item_name, item.item_description)), end='\n')

    #Definition of the output_cart method which outputs the current cart and specifics of all
    #items, as well as the calculated total price.
    def output_cart(self):
        #Callin of the class ShoppingCart to be used in the output.
        new = ShoppingCart()
        print('\nOUTPUT SHOPPING CART', end='\n')
        print(('%s\'s Shopping Cart - %s' % (self.customer_name, self.current_date)),end='\n')
        print(('Number of Items: %d' % (new.get_num_items_in_cart())), end='\n\n')
        
        if (new.get_num_items_in_cart() == 0):
            print('SHOPPING CART IS EMPTY')
        
        tot_cost = 0

        #for loop used to iterate through the cart_items list and print out each item and its
        #specifics, as well as the total cost.
        for item in self.cart_items:
            print(('%s %d @ $%d = $%d' % (item.item_name, item.item_quantity,
                                             item.item_price, (item.item_quantity * item.item_price))), end='\n')
            tot_cost += (item.item_quantity * item.item_price)
            
        print(('\nTotal: $%d' % tot_cost),end='\n')
