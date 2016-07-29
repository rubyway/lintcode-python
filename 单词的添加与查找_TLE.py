#TLE

"""
设计一个包含下面两个操作的数据结构：addWord(word), search(word)

addWord(word)会在数据结构中添加一个单词。而search(word)则支持普通的单词查询或是只包含.和a-z的简易正则表达式的查询。

一个 . 可以代表一个任何的字母。
注意事项

你可以假设所有的单词都只包含小写字母 a-z。
样例

addWord("bad")
addWord("dad")
addWord("mad")
search("pad")  // return false
search("bad")  // return true
search(".ad")  // return true
search("b..")  // return true


"""
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
        length = len(self.aList)
            
        i = 0
        while i< length:
            temp = self.aList[i]
            if lent != len(temp):
                i += 1
                continue
            j = 0
            while j < lent:
                if j == (lent- 1) and (word[j] == temp[j] or word[j] == '.'):
                    return True
                if word[j] != temp[j] and word[j] != '.':
                    break
                else:
                    j += 1
            i += 1
        return False
        



# Your WordDictionary object will be instantiated and called as such:
#wordDictionary = WordDictionary()
#wordDictionary.addWord("abc")
#wordDictionary.addWord("bcd")
#wordDictionary.addWord("abcd")
#wordDictionary.addWord("adcd")
#wordDictionary.addWord("qord")
#wordDictionary.search("abcd")
