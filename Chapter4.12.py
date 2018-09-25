autoservice = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 0
}

print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print('')

first_serv = input('Select first service:\n')
second_serv = input('Select second service:\n')
print('')

print('Davy\'s auto shop invoice')
print('')

if first_serv == 'Oil change':
    print('Service 1: %s, $%d' % (first_serv, autoservice[first_serv]))
elif first_serv == 'Tire rotation':
    print('Service 1: %s, $%d' % (first_serv, autoservice[first_serv]))
elif first_serv == 'Car wash':
    print('Service 1: %s, $%d' % (first_serv, autoservice[first_serv]))
elif first_serv == 'Car wax':
    print('Service 1: %s, $%d' % (first_serv, autoservice[first_serv]))
elif first_serv == '-':
    print('Service 1: No service')
else:
    print('This service is not provided.')
    
if second_serv == 'Oil change':
    print('Service 2: %s, $%d' % (second_serv, autoservice[second_serv]))
elif second_serv == 'Tire rotation':
    print('Service 2: %s, $%d' % (second_serv, autoservice[second_serv]))
elif second_serv == 'Car wash':
    print('Service 2: %s, $%d' % (second_serv, autoservice[second_serv]))
elif second_serv == 'Car wax':
    print('Service 2: %s, $%d' % (second_serv, autoservice[second_serv]))
elif second_serv == '-':
    print('Service 2: No service')
else:
    print('This service is not provided.')
    
Total = (autoservice[first_serv] + autoservice[second_serv]) 
print('')
print('Total: $', Total)
