
def encrypt():
    '''This function starts by initilizing a dictionary with a list of code, which will
    be referenced later on when encrypting. It then asks for a user entered string to
    encrypt. This string is .split() ito a list for easy iteration. Finally, a set of
    for loops, one nested, searched through the user's sentence list and then indexes
    the values found to the code dictionary. These codes are then .append()ed to a
    list that is joined and then printed out.'''
    codes = {
        'A':'!', 'B':'@', 'C':'#', 'D':'$', 'E':'%', 'F':'^', 'G':'&', 'H':'*',
        'I':'(', 'J':')', 'K':'`', 'L':'-', 'M':'=', 'N':',', 'O':'.', 'P':'/',
        'Q':'\'', 'R':'[', 'S':']', 'T':'|', 'U':';', 'V':'S', 'W':'~', 'X':'?',
        'Y':'{', 'Z':'}', 'a':'8', 'b':'5', 'c':'9', 'd':'+', 'e':':', 'f':'<',
        'g':'>', 'h':'\"', 'i':'4', 'j':'6', 'k':'0', 'l':'2', 'm':'1', 'n':'7',
        'o':'3', 'p':'Q', 'q':'P', 'r':'_', 's':'y', 't':'a', 'u':'L', 'v':'E',
        'w':'D', 'x':'i', 'y':'c', 'z':'J'
    }

    usr_input = input('Enter a sentence to encrypt:\n')
    sentence_list = list(usr_input)
    encrypt_list = []

    for index, val in enumerate(sentence_list):
        for key, value in codes.items():
            if val in codes:
                encrypt_list.append(codes[val])
                break
            else:
                encrypt_list.append(val)
                break

    encrypt_sentence = ''.join(encrypt_list)
    print('\n%s encrypted is: %s' % (usr_input, encrypt_sentence))
    
    return encrypt_sentence


def decode(encrypted_str):
    '''This function stars off by initializing an opposite dictionary from the earlier
    function, which is used for decoding. This is done by taking the earlier encrypted
    string and .split()ing it into a list for iteration. A set of for loops, one nested,
    index the encoded value from the encrypted string and searches for the replacement
    in the decode dictionary. Once found, the decoded character is .append()ed to
    a list that is later .join()ed and printed out'''
    decode = {
        '!':'A', '@':'B', '#':'C', '$':'D', '%':'E', '^':'F', '&':'G', '*':'G',
        '(':'I', ')':'J', '`':'K', '-':'L', '=':'M', ',':'N', '.':'O', '/':'P',
        '\'':'Q', '[':'R', ']':'S', '|':'T', ';':'U', 'S':'V', '`':'W', '?':'X',
        '{':'Y', '}':'Z', '8':'a', '5':'b', '9':'c', '+':'d', ':':'e', '<':'f',
        '>':'g', '\"':'h', '4':'i', '6':'j', '0':'k', '2':'l', '1':'m', '7':'n',
        '3':'o', 'Q':'p', 'P':'q', '_':'r', 'y':'s', 'a':'t', 'L':'u', 'E':'v',
        'D':'w', 'i':'x', 'c':'y', 'J':'z'
    }

    encrypted_str_list = list(encrypted_str)
    decoded_list = []
    
    for index, val in enumerate(encrypted_str_list):
        for key, value in decode.items():
            if val in decode:
                decoded_list.append(decode[val])
                break
            else:
                decoded_list.append(val)
                break

    decoded_sentence = ''.join(decoded_list)
    print('\n%s decoded is: %s' % (encrypted_str, decoded_sentence))
    
    return decoded_sentence

#Calls the two functions, with one as the other's argument
decode(encrypt())

