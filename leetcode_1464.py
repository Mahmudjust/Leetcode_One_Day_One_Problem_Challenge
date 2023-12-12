#Algorithm 1:
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans = max(ans, (nums[i] - 1) * (nums[j] - 1))
        
        return ans


#Algorithm 2:

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[-1]
        y = nums[-2]
        return (x - 1) * (y - 1)

#Algorithm 3:

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)
        
        return (biggest - 1) * (second_biggest - 1)
