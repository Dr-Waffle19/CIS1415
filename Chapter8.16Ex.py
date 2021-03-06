#Initializes variables for number of weights that will be entered in
#the for loop, as well as creating an empty list to append to later.
num_people = 4
weight_lbs = []

#for loop used to take user inputs of weights (in pounds), strip() them
#and convert them to floats, and finally append them to the empty list.
for i in range(num_people):
    user_input = float(input('Enter weight %d:\n' % (i + 1)).strip())
    weight_lbs.append(user_input)

print('Weights:', weight_lbs)

#Calculates and prints out the average weight to a .2 preciseness.
avg_weight = sum(weight_lbs) / num_people
print('\nAverage weight: %.2f' % avg_weight)

#Finds and prints out the highest weight out of the user entered weights
max_weight = max(weight_lbs)
print('Max weight: %.2f' % max_weight)

#Asks the user to enter an index to view both the weight of that index in
#pounds and kilograms. Both are found or calculated and stored under a variable
user_index = int(input('\nEnter a list index (1 - 4):\n').strip())
user_index_lbs = weight_lbs[(user_index - 1)]
user_index_kg = user_index_lbs / 2.2

#Prints out the previously found weights.
print('Weight in pounds: %.2f' % user_index_lbs)
print('Weight in kilograms: %.2f' % user_index_kg)

#Sorts the list from lowest weight to highest. Use sorted() to make a copy list
#to avoid changing the original list, in-case more functions are added on later
sorted_list = sorted(weight_lbs)
print('\nSorted list:', sorted_list)
