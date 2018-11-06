
encryption_code = {'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
                      'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
                      'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
                      'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
                      'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
                      't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}

original_file = open('Encrept_decrept_file.txt','r')
file_read = original_file.read()
original_file.close()
encrypt_file = open('ENCRYPTED_Encrept_decrept_file.txt','w')

for er in file_read:
    if er in encryption_code:
        encrypt_file.write(encryption_code[er])
    else:
        encrypt_file.write(er)

encrypt_file.close()
encrypt_file = open('Encrept_decrept_file.txt','r')
file_read = encrypt_file.read()
encrypt_file.close()
codes_items = encryption_code.items()

for er in file_read:
    if not er in encryption_code.values() or er == '.' or er == ',' or er == '!':
        print(er)
    else:
        for k,v in codes_items:
            if er == v and er != '.':
                print(k,end='')
