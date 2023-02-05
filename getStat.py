import requests

def getStat(url):
    -- The function returns a words array and their frequencies from URL

    def getWords(txt):
        --Returns parsed Html splitted into words        
        result = []
        
        /*
            ToDo list: 
            1) parse using external library
            2) split into words
        */

        return result --array of words
    
    def getStat(words):
        result = []
        for i in words:
            found = false
            for j in result:
                if j[0] == i: 
                    found = true
                    -- increase the number of coincidences for the word found
                    j[1]++
                    break

            if found == false:
                -- add a new word to the list
                a = []*2
                a[0] = i
                a[1] = 1
                result.append(a)
        
        return result --array of Obj: [word], [frequency]


    -- Function's implementation

    r = requests.get(url) 
    html = r.text
    --print(html)
    words = getWords(html)
    wordStat = getStat(words)

    return wordStat

--Test

url = 'https://ru.wikipedia.org/wiki/The_Beatles'
print(getStat(url))