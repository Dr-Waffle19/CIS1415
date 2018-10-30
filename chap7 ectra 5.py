def main():

    alphaList = [["A","B","C"],\
                    ["D","E","F"],\
                    ["G","H","I"],\
                    ["J","K","L"],\
                    ["M","N","O"],\
                    ["P","Q","R","S"],\
                    ["T","U","V"],\
                    ["W","X","Y","Z"]]
    numList = ["2","3","4","5","6","7","8","9","1"]
    print("get the 10 character tp number",\
          "from the user in the form (XXX-XXXX-XXXX)")
    tpNumber = input("Enter the 10-character tp number(XXX-XXXX-XXXX) : ")
    tpSplit = tpNumber.split("-")
    listLength1,listLength2,listLength3 = tpList(tpSplit)
    while listLength1 != 3 or listLength2 != 3 or \
          listLength3 != 4 :
        print("you gave the wrong format of telephone number...")
        print("format should be XXX-XXX-XXXX")
        tpNumber = input("Enter the 10-character tp number(XXX-XXXX-XXXX) : ")
        tpSplit = tpNumber.split("-")
        listLength1,listLength2,listLength3 = tpList(tpSplit)
    print("user entered format : ",end="")
    print(tpSplit[0].upper(),"-",tpSplit[1].upper(),\
          "-",tpSplit[2].upper(),sep="")
    print("numeric format : ",end="")
    for element in tpSplit[0]:
        elementUpper = element.upper()
        result = convert_tp(elementUpper,numList,alphaList)
        print(result,end="")
    print("-",end="")
    for element in tpSplit[1]:
        elementUpper = element.upper()
        result = convert_tp(elementUpper,numList,alphaList)
        print(result,end="")
    print("-",end="")
    for element in tpSplit[2]:
        elementUpper = element.upper()
        result = convert_tp(elementUpper,numList,alphaList)
        print(result,end="")
    
    
def tpList(anyList):
    anyList1 = len(anyList[0])
    anyList2 = len(anyList[1])
    anyList3 = len(anyList[2])
    return anyList1,anyList2,anyList3

def convert_tp(element,numList,alphaList):
    if element in numList:
        return element
    else:
        for row in range(len(alphaList)):
            for coloumn in range(len(alphaList[row])):
                if element == alphaList[row][coloumn]:
                    return numList[row]


main()
