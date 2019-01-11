def absolute(n):
    if(n >= 0):
        return n
    return -n

def palindrome4(input):
    if(len(input) > 4 or len(input) < 4):
        return False
    string = input[::-1]
    if(string == input):
        return True
    return False


def ORF(DNA):
    beginning = DNA[:3]
    ending = DNA[-3:]
    if(beginning == "ATG"):
        if(ending == "TGA" or ending == "TAG" or ending == "TAA"):
            if(len(DNA)%3 == 0):
                return True
    return False

def ORFadviser(DNA):
    beginning = DNA[:3]
    ending = DNA[:-3:]
    if(ORF(DNA) == True):
        return "This is an ORF"
    elif(beginning != "ATG"):
        return "The first three bases are not ATG"
    elif(ending != "TGA" or ending != "TAG" or ending != "TAA"):
        return "The last three bases are not a stop codon"
    elif(len(DNA)%3 != 0):
        return "The string is not of the correct length"

def friendly(greeting):
    if(len(greeting) < 0):
        return "I am sorry, but I did not understand you"
    elif((len(greeting) > 2 and greeting[:2] == "Hi") or (len(greeting) > 5 and greeting[:5] == "Hello")):
        return "Hi, nice to meet you"
    elif(greeting[:1] == "?"):
        return "Good Question"
    else:
        return "I am sorry, but I did not understand you."
    
def count(letter,string):
    number = 0
    for i in string:
        if(i == letter):
            number = number + 1
    return number


        
        
