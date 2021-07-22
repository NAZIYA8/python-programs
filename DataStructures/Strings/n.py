def longestLength(wordsList):
    finalList = []
      
    for word in wordsList:
        finalList.append((len(word), word))
      
    finalList.sort()
      
    print("The word with the longest length is:", finalList[-1][1],
          " and length is ", len(finalList[-1][1]))
  
  
# Driver Program
wordsList = ["one", "two", "third", "four"]
longestLength(wordsList)