class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        i, j, k = m- 1, n- 1, m+ n- 1
        while i>= 0 and j>= 0:
            if A[i] <= B[j]:
                A[k] = B[j]
                k -= 1
                j -= 1
            else:
                A[k] = A[i]
                k -= 1
                i -=1
        while j>= 0:
            A[k] = B[j]
            k -= 1
            j -= 1
        
                
                
                
        