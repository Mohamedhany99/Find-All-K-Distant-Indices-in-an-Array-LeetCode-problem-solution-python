class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        result =[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (abs(i-j)<=k and nums[j]==key) :
                    result.append(i)
        res=list(set(result))
        print(res)
        return res
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        