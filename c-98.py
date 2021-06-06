def countWords():
    wordCount = 0
    file = input("Enter file name: ")
    fileReal = open(file,'r')
    for line in fileReal:
        word = line.split()
        wordCount = wordCount + len(word)
        print(wordCount)
    
countWords()