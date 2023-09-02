#Task 1. String in lower case: You want to Pre-process the customer feedback by converting all the text to lowercase. This step helps standardize the text. Lower casing the text allows you to focus on the content rather than the specific letter casing.

#Task 2. Frequency of all words in a given string: After converting the text to lowercase, you want to determine the frequency of each word in the customer feedback. This information will help you identify which words are used more frequently, indicating the key aspects or topics that customers are mentioning in their reviews. By analyzing the word frequencies, you can gain insights into the most common issues raised by customers.

#Task 3. Frequency of a specific word: In addition to analyzing the overall word frequencies, you want to specifically track the frequency of a particular word that is relevant to your analysis. For example, you might be interested in monitoring how often the word "reliable" appears in the customer reviews to gauge customer sentiment about the product's reliability. By focusing on the frequency of a specific word, you can gain a deeper understanding of customer opinions or preferences related to that particular aspect.

#Sample text for analysis
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# Let's create a class called TextAnalyzer to analyze text.

#Implement a code to Format the text in Lowercase
#Implement a code to count the Frequency of all unique words:
#Implement a code to count the Frequency of a specific word

class TextAnalzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
         
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
analyzed = TextAnalyzer(givenstring)

print("Formatted Text:", analyzed.fmtText)

freqMap = analyzed.freqAll()
print(freqMap)

word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")