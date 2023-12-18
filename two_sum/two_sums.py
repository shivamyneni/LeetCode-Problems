# Solution 1:
#1.Adding the value and index of list to the dictionary if we subtract target value and current value and check if the value is present in the dictionary and return both values
# Time Complexity: O(n)
# Space Complexity: O(n)



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict={}
        for i in range(0,len(nums)):
            if( index_dict.get(target-nums[i],-1)==-1):
                index_dict[nums[i]]=i
            else:
                return [index_dict[target-nums[i]],i]