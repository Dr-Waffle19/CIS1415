#This chunk prints out the name of the auto shop as well as the names and prices
#of the services they offer
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

#This chunk asks for the customer's choices of services and
#stores those choices in two variables
first_service = input('\nSelect first service:\n')
second_service = input('Select second service:\n')

print('\nDavy\'s auto shop invoice')
print('')

'''Creates a dictionary with the services as the key and the price as the value.
I did this to make the repeatability and understandability of the
code possibly better (in the if-else branches)'''
services_costs = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 0
}

#Creates an if-else branch to print off the first choice and its price using
#the previously created dictionary.
if first_service == 'Oil change':
    print('Service 1: %s, $%d' % (first_service, services_costs[first_service]))
elif first_service == 'Tire rotation':
    print('Service 1: %s, $%d' % (first_service, services_costs[first_service]))
elif first_service == 'Car wash':
    print('Service 1: %s, $%d' % (first_service, services_costs[first_service]))
elif first_service == 'Car wax':
    print('Service 1: %s, $%d' % (first_service, services_costs[first_service]))
elif first_service == '-':
    print('Service 1: No service')
else:
    print('Error: Entered service is not provided at Davy\'s auto shop')

#Same as last chunk but for the second choice.
if second_service == 'Oil change':
    print('Service 2: %s, $%d' % (second_service, services_costs[second_service]))
elif second_service == 'Tire rotation':
    print('Service 2: %s, $%d' % (second_service, services_costs[second_service]))
elif second_service == 'Car wash':
    print('Service 2: %s, $%d' % (second_service, services_costs[second_service]))
elif second_service == 'Car wax':
    print('Service 2: %s, $%d' % (second_service, services_costs[second_service]))
elif second_service == '-':
    print('Service 2: No service')
else:
    print('Error: Entered service is not provided at Davy\'s auto shop')

#Creates a variable that adds the prices of the two choices and then outputs
#that value. Utilizes the dictionary.
total_cost = services_costs[first_service] + services_costs[second_service]
    
print('\nTotal: $%d' % total_cost)
