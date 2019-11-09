class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        max_sum = -1
        i=0
        j=len(A)-1
        A.sort()
        while i<j:
            if A[i]+A[j] < K:
                if A[i]+A[j] > max_sum:
                    max_sum=A[i]+A[j]
                i+=1
            else:
                j-=1
        return max_sum