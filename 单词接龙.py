"""
给出两个单词（start和end）和一个字典，找到从start到end的最短转换序列

比如：

每次只能改变一个字母。
变换过程中的中间单词必须在字典中出现。

 注意事项

如果没有转换序列则返回0。
所有单词具有相同的长度。
所有单词都只包含小写字母。

您在真实的面试中是否遇到过这个题？ Yes
样例
给出数据如下：

start = "hit"

end = "cog"

dict = ["hot","dot","dog","lot","log"]

一个最短的变换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog"，

返回它的长度 5"""
#以下是书影博客解法
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer

    def ladderLength(self, start, end, dict):
        if start == end:
            return 1
        from collections import defaultdict, deque
        queue = deque( [ [start, 1] ] )
        visited = set( [ start ] )
        neighbors = defaultdict(list)
        for word in dict:
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                neighbors[token] += word,
        while queue:
            word, length = queue.popleft()
            if self.wordDist(word, end) <= 1:
                return length + 1
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                for ladder in neighbors[token]:
                    if ladder not in visited:
                        visited.add(ladder)
                        queue += [ladder, length + 1],
        return 0
    def wordDist(self, wordA, wordB):
        return sum([wordA[x] != wordB[x] for x in range(len(wordA))])
#以下是自己的想法，在BFS过程中判断混乱，需要修改
"""
    def ladderLength(self, start, end, dict):
        length = len(dict)
        queue = []
        queue.append(start)
        count = 1
        while queue:
            #count += 1
            word = queue[0]
            queue = queue[1:]
            if self.diffone(word, end):
                return count+ 1
            temp = self.neighbours(dict, word)
            if temp != []:
                for i in temp:
                    dict.remove(i)
                    queue.append(i)
                count += 1
            

            
        
    def neighbours(self, alist, b):
        #length = len(alist)
        temp = []
        for i in alist:
            if self.diffone(i, b):
                temp.append(i)
        return temp
    def diffone(self, a, b):
        length = len(a)
        temp = 0
        for i in xrange(length):
            if a[i] != b[i]:
                temp += 1
            else:
                temp = temp
        if temp == 1:
            return True
        else:
            return False"""
