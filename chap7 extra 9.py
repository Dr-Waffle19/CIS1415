def main():

    getString = input("Enter the string : ")
    print("counting number of vowel letters in given string....")
    totalVowels = vowelCount(getString)
    print("number vowel letters :",totalVowels)
    print()
    print("counting number of consonants letters in given string....")
    totalconsonants = consoCount(getString)
    print("number vowel letters :",totalconsonants)

def vowelCount(string):
    count = 0
    string1 = string.upper()
    for ch in string1:
        if ch == "A" or ch == "E" or ch == "I" or \
           ch == "O" or ch == "U":
            count += 1
    return count

def consoCount(string):
    count = 0
    for ch in string:
        if ch.isalpha():
            count += 1
    totalConsonants = count - vowelCount(string)
    return totalConsonants
main()

