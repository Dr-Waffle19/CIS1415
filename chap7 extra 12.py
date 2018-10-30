getSentence = input("Enter the string : ")


lists = getSentence.split()

print("English :",getSentence)

print("Pig Latin : ",end="")
for i in lists:
    newString = i[1:len(i)] +\
                i[0]+"AY"
    print(newString.upper(),end=" ")
