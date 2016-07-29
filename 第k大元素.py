"""


在数组中找到第k大的元素
注意事项

你可以交换数组中的元素的位置
您在真实的面试中是否遇到过这个题？
样例

给出数组 [9,3,2,4,8]，第三大的元素是 4

给出数组 [1,2,3,4,5]，第一大的元素是 5，第二大的元素是 4，第三大的元素是 3，以此类推

"""
#http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
import random
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        length = len(A)
        if k > length:
            return None
        flag = random.choice(A)
        left, right = [], []
        for _ in A:
            if _> flag:
                left.append(_)
            elif _< flag:
                right.append(_)
        if k<= len(left):
            return self.kthLargestElement(k, left)
        elif k> (length- len(right)):
            return self.kthLargestElement(k- (length- len(right)), right)
        else:
            return flag
            
""" 
        A.sort()
        A = A[::-1]
        return A[k-1]
"""
        
