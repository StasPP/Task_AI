import requests
from bs4 import BeautifulSoup

def getStat(url):
    #The function returns a words array and their frequencies from URL

    def getWords(txt):  #returns parsed Html splitted into words        
        
        result = []

        # create BeautifulSoup object (we could use different parsers)
        soup = BeautifulSoup(txt,"html.parser")
        
        # Here also could be filtered some parts of the page before adding and splitting!

        for string in soup.body.strings:
            string = string.split(' ')

            for string2 in string:
                string2 = string2.split('/n')
                string2 = [item for item in string2 if len(item)>=2] # filter the array - delete strings with lenght < 2
                result.append(string2)

        # The algorithm is too slow but it works

        return result 
    
    def getStat(words):
        result = []
        for i in words:
            found = False
            for j in result:
                if j[0] == i: 
                    found = True
                    #increase the number of coincidences for the word found
                    j[1] += 1
                    break

            if found == False:
                #add a new word to the list
                a = []
                a.append(i)
                a.append(1)
                result.append(a)

                result.sort()

        return result #array of Obj: [word], [frequency]

    def Sort(arr):
 
        # reverse = None (Sorts in Ascending order)
        # key is set to sort using second element of
        # sublist lambda has been used
        return(sorted(arr, key = lambda x: x[1]))   
 
    #Function's implementation

    r = requests.get(url) 
    html = r.text
    #print(html)
    words = getWords(html)
    wordStat = getStat(words)

    return  Sort(wordStat)

#Test

url = 'https://ru.wikipedia.org/wiki/The_Beatles'
print(getStat(url))