"""
Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

 

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
 

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in increasing order.
"""
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        if len(mat) == 0:
            return min(mat[0])
        hmap = {}
        for row in mat:
            for item in row:
                if hmap.get(item):
                    hmap[item] += 1
                else:
                    hmap[item] = 1
        for k in sorted(hmap.keys()):
            if hmap[k] == len(mat):
                return k
        return -1