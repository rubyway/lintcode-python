"""
最长单词

 描述
 笔记
 数据
 评测
给一个词典，找出其中所有最长的单词。

您在真实的面试中是否遇到过这个题？ Yes
样例
在词典

{
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
}
中, 最长的单词集合为 ["internationalization"]

在词典

{
  "like",
  "love",
  "hate",
  "yes"
}
中，最长的单词集合为 ["like", "love", "hate"]"""
#挑战 遍历两次的办法很容易想到，如果只遍历一次你有没有什么好办法？
class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        length = len(dictionary)
        temp = []
        templen = 0
        for i in dictionary:
            if len(i) > templen:
                temp = []
                temp.append(i)
                templen = len(i)
                #dictionary.remove(i)
            elif len(i) == templen: 
                temp.append(i)
                templen = len(i)
                #dictionary.remove(i)
        return temp
                
