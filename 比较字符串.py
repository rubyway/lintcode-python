"""
比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母

 注意事项

在 A 中出现的 B 字符串里的字符不需要连续或者有序。

给出 A = "ABCD" B = "ACD"，返回 true

给出 A = "ABCD" B = "AABC"， 返回 false
"""
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        lengtha, lengthb = len(A), len(B)
        adict, bdict = {}, {}
        for i in A:
            if i not in adict:
                adict[i] = 1
            else:
                adict[i] += 1
        for j in B:
            if j not in bdict:
                bdict[j] = 1
            else:
                bdict[j] += 1
        temp = bdict.keys()
        for k in temp:
            if k not in adict.keys() or adict[k] < bdict[k]:
                return False
        return True
                
