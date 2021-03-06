#'''(1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)'''
#Recieves an user inputed string to find length and edit.
inputStr = input('Enter a sentence or phrase:\n')

print('\nYou entered:', inputStr)

#'''(2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string.
#We encourage you to use a for loop in this function. (2 pts)'''

def get_num_of_characters(inputStr):
    '''Uses a for loop to count how many characters are in user's string'''
    for i in range(len(inputStr)):
        i += 1
    return i
    
#'''(3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)'''
    
#Calls get_num_of_characters and reassigns the value
num_chars = get_num_of_characters(inputStr)

#Prints out number of characters in the string using the reassigned var
print('\nNumber of characters:', num_chars)

#'''(4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace()
#outputs the string's characters except for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_whitespace()
#function in main(). (2 pts)'''

def output_without_whitespace(inputStr):
    '''Uses .replace() to remove spaces and tabs from the inputed string'''
    inputStr = inputStr.replace(' ', '')
    inputStr = inputStr.replace('\t', '')
    return inputStr

#Calls get_num_of_characters and reassigns the value
#num_chars = get_num_of_characters(inputStr)

#if statement used to check if in main(), then calls output_without_whitespace
#using the user inputed string. Reassigns the value and then prints it out.
if __name__ == '__main__':
    no_whitespace = output_without_whitespace(inputStr)
    print('String with no whitespace:', no_whitespace)
  
