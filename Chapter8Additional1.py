
def enter_rainfall():
    '''This function uses a for loop to obtain user entered data on the amount
    of rainfall recorded in each month. Each iteration of the for loop, the
    user entered data is appended to a list that is returned at the end of the
    function to be utilized by another function later in the file.'''
    monthly_rainfall = []
    for i in range(12):
        usr_input = float(input('Enter month %d\'s total rainfall:\n' % (i+1)).strip())
        monthly_rainfall.append(usr_input)

    return monthly_rainfall

def rainfall_calc(rain_list):
    '''This function utilized the earlier user created list with data on
    monthly rainfall. It calculates both the average and total rainfall
    using the built-in function sum(). The function later uses two for loops
    to check for and print out the maximum and minimum amounts of rainfall, as
    well as the month in which they occured. These loops utilize the enumerate()
    function.'''
    total_rainfall = sum(rain_list)
    average_rainfall = total_rainfall / 12

    print('\nTotal rainfall: %.2f' % total_rainfall)
    print('Average monthly rainfall: %.2f' % average_rainfall)

    for index, val in enumerate(rain_list):
        if max(rain_list) == val:
            print('Maximum rainfall: Month %d, %.2f' % ((index + 1), val))

    for index, val in enumerate(rain_list):
        if min(rain_list) == val:
            print('Minimum rainfall: Month %d, %.2f' % ((index + 1), val))

    return

#Calling of both functions, with one as the argument of the other.
rainfall_calc(enter_rainfall())
