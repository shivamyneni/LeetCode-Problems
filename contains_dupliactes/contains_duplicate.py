# Solution 1:
# 1.Converting the list to set and comparing the length of both
class Solution:
    def containsDuplicate(self, nums: List[int]) :
        if(len(nums)!=len(set(nums))):
            return True
        else:
            return False
        

# Solution 2:
# 1.Using Hashset to store the elements and check if the element is already present in the set
class Solution:
    def containsDuplicate(self, nums: List[int]) :
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            else :
                hashset.add(i)
        return False