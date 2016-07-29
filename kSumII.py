class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer 
    """
    def kSumII(self, A, k, target):
        length = len(A)
        if length == 0 or length < k:
            return None
        result = []
        n = k
        def helper(A, n, target, temp):
            length = len(A)
            if sum(temp) > target or length< n:
                return
            if len(temp) == k and sum(temp) == target:
                result.append(temp)
            for i in xrange(length):
                helper(A[i+ 1:], n- 1, target, temp+[A[i]])
        helper(A, n, target, [])
        return result
