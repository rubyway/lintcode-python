class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.aList = []


    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        self.aList.append(word)


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        lent = len(word)
        templen = []
        for k in self.aList:
            templen.append(len(k))
        if lent not in templen:
            return False
        for i in self.aList:
            if lent == len(i):
                j = 0
                while j < lent:
                    if word[j] != i[j] and word[j] != '.':
                        return False
                    else:
                        j += 1
                return True


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("abc")
wordDictionary.addWord("bcd")
wordDictionary.addWord("abcd")
wordDictionary.addWord("adcd")
wordDictionary.addWord("qord")
wordDictionary.search("abcd")
