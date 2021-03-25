#Comma Code
#This program creates a function that accepts a "dirty" list of strings
#and returns a clean string. It also checks for an empty list and returns
#a notice if an empty list is receieved.

def formalize(dirtyList):
    length = len(dirtyList)
    cleanString = ''
    if length == 0:
        cleanString = 'Well, you did not pass me anything at all!'
    else:
        for i in range(length - 1):
            cleanString = cleanString + dirtyList[i] + ', '
        cleanString = cleanString + 'and ' + dirtyList[length-1] + '.'
        
    return cleanString

testList1 = []
testList2 = ['pig', 'dog', 'cow', 'chicken']

result1 = formalize(testList1)
result2 = formalize(testList2)

print(result1 + '\n')
print(result2)