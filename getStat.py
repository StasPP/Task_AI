import requests
from bs4 import BeautifulSoup
import os.path

def getStat(url):
    #The function returns a words array and their frequencies from URL

    def specialFilter(url, soup):
        # For pages of Wikipedia
        if 'wikipedia.org' in url.lower():
            # take only the content!!!

            a = [p.get_text() for p in soup.find_all("div", {"id":"bodyContent"})] 
            b = [p.get_text() for p in soup.find_all("span", {"class":"mw-page-title-main"})]

            return b+a
        
        # here can be added more special conditions!!!
        return soup.body.strings

    def replaceSymbols(str):
        toDel = "'([;,.!?])"

        result = ''
        for s in str:
            for d in toDel:
                if s == d or s =='"':
                    break
            else: result += s

        return result

    def getWords(soup):  #returns parsed Html splitted into words        
        
        result = []
        
        # file_path = 'Task_AI\\stop_test.txt'
        file_path = os.getcwd()+'//Task_AI//stop_test.txt'
        # if os.path.exists(file_path):
        my_file = open(file_path, "r")

        stopList = my_file.read()
        stopList = stopList.split("\n")

        # Here also could be filtered some parts of the page before adding and splitting!

        for string in specialFilter(url, soup):
            string = string.replace('\n',' ')
            string = string.replace('\t',' ')
            string = string.replace('\xa0-',' ')
            
            string = replaceSymbols(string)

            string = string.split(' ')
            string = [item for item in string if (len(item)>=2) and (item is not None) ] # filter the array - delete strings with lenght < 2
            
            # Add each word in case it is not presented in the stopList
            for s in string:

                for stopWord in stopList:
                    if s.lower() == stopWord.lower():
                        break
                else:
                    result.append(s)

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

        return result #array of Obj: [word], [frequency]
    
    def FilterFrequencies(result):      
        # Cut off the words under the median frequency
        if len(result) > 1:
            numbers = []
            for r in result:   
                canAdd = True
                for n in numbers:
                    if n == r[1]:
                        canAdd = False
                        break
                    else:
                        canAdd = True
                    
                if canAdd:
                    numbers.append(r[1])   
      

            numbers.sort()

            if len(numbers) > 3:
                result = [item for item in result if item[1] > numbers[len(numbers)//2]] 

        return result
    

    def AddWeights(words, soup):

        # Icrease the weights for the words presented in headers

        # Arrays of words in headers h1 to h5
        h1 = [p.get_text() for p in soup.find_all("h1", {}) ] 
        h23 = [p.get_text() for p in soup.find_all("h2", {}) ] + [p.get_text() for p in soup.find_all("h3", {}) ] 
        h45 = [p.get_text() for p in soup.find_all("h4", {}) ] + [p.get_text() for p in soup.find_all("h5", {}) ] 

        for h_word in h1:
            h_word = h_word.split(" ")
            for w in h_word:
                for word in words:
                    if word[0] == w:
                        word[1] *= 2
                        break
        for h_word in h23:
            h_word = h_word.split(" ")
            for w in h_word:
                for word in words:
                    if word[0] == w:
                        word[1] *= 1.5
                        break
        for h_word in h45:
            h_word = h_word.split(" ")
            for w in h_word:
                for word in words:
                    if word[0] == w:
                        word[1] *= 1.25
                        break
        
        # Reduce the weights of the words contained in the reference if it's WikiPedia
        if 'wikipedia.org' in url.lower():
            reflist = [p.get_text() for p in soup.find_all("div", {"class":"reflist"}) ] 
            for h_word in reflist:
                h_word = h_word.split(" ")
                for w in h_word:
                    for word in words:
                        if word[0] == replaceSymbols(w):
                            word[1] -= 0.75
                            break
        return words

    def Sort(arr):
        return(sorted(arr, key = lambda x: x[1]))   
 
    #Function's implementation

    r = requests.get(url) 
    html = r.text
    # create BeautifulSoup object (we could use different parsers)
    soup = BeautifulSoup(html,"html.parser")

    words = getWords(soup)
    wordStat = AddWeights( FilterFrequencies( getStat(words) ), soup )
    
    return  Sort(wordStat)

#Test

url = 'https://en.wikipedia.org/wiki/The_Beatles'
# getStat(url)
print(getStat(url))
