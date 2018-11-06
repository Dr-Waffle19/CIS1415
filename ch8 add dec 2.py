decryption_code = {'!':'A','@':'B','#':'C','$':'D','%':'E','^':'F','&':'G','*':'H','(':'I',
                      ')':'J','-':'K','_':'L','+':'M','=':'N','`':'O','~':'P','{':'Q','[':'R',
                      '}':'S',']':'T',':':'U',';':'V','"':'W','<':'X','>':'Y','0':'Z','1':'a',
                      '2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','a':'j',
                      'b':'k','c':'l','d':'m','e':'n','f':'o','g':'p','h':'q','i':'r','j':'s',
                      'k':'t','l':'u','m':'v','n':'w','o':'x','p':'y','q':'z'}

original_file = open('ENCRYPTED_Encrept_decrept_file.txt','r')
file_read = original_file.read()
original_file.close()
encrypt_file = open('DECRYPTED_Encrept_decrept_file.txt','w')

for er in file_read:
    if er in decryption_code:
        encrypt_file.write(decryption_code[er])
    else:
        encrypt_file.write(er)

encrypt_file.close()
encrypt_file = open('ENCRYPTED_Encrept_decrept_file.txt','r')
file_read = encrypt_file.read()
encrypt_file.close()    
codes_items = decryption_code.items()

for er in file_read:
    if not er in decryption_code.values() or er == '.' or er == ',' or er == '!':
        print(er)
    else:
        for k,v in codes_items:
            if er == v and er != '.':
                print(k,end='')
