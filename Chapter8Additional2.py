#Initializes a three-dimesional list with bases for an exponential growth program.
exp_growth_base = [[2], [3], [4], [5]]
#Prints out the base list for reference to the user for indexing.
print(exp_growth_base)

#Takes an user inpur of what base they want to grow and stores it under a variable.
usr_input = int(input('Enter index to exponentially grow (-1 to quit):\n').strip())

#While loop used so the user can repeatedly use the program for other bases.
while usr_input != -1:
    #Asks the user to what degree they want to grow the base and stores it.
    usr_choice = int(input('\nHow many times of growth:\n').strip())

    #Prints out the original base for visual formatting.
    base = exp_growth_base[usr_input]
    print(base)

    #Uses a for loop to grow and output the exponential growth, as well as
    #.append() the outpur to the list for later useage.
    for i in range(usr_choice):
        exp_grow = exp_growth_base[usr_input][i] * 2
        exp_growth_base[usr_input].append(exp_grow)
        print(exp_grow)

    #Utilizes the appended list to sum up the exponential growth and outputs the result.
    print('\nThe sum of this exponential growth is: %d' % (sum(exp_growth_base[usr_input])))

    #Asks the user for a new index to continue or break the while loop.
    usr_input = int(input('\nEnter index to exponentially grow (-1 to quit):\n').strip())

