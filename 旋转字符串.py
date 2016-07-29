"""


给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
您在真实的面试中是否遇到过这个题？
样例

对于字符串 "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"

挑战

在数组上原地旋转，使用O(1)的额外空间
"""

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        if offset == 0:
            return s
        length = len(s)
        if length == 0:
            return s
        offset %= length
        self.swap(s, 0, length- offset)
        self.swap(s, length- offset, length)
        self.swap(s, 0, length)
        
    def swap(self, s, a, b):
        for i in xrange(a, (a+b)>>1):
            s[i], s[a+ b- i- 1] = s[a+ b- i- 1], s[i]
"""          
    def rotateString(self, s, offset):
        n = len(s)
        if n == 0:
            return s
        offset %= n
        temp = s[:n-offset]
        for i in xrange(n):
            if i < offset:
                s[i] = s[n-offset+i]
            else:
                s[i] = temp[i-offset]"""
