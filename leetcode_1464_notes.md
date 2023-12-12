Approach 1: Brute Force
Intuition

To start, we will simply check every pair of indices (i, j) and calculate (nums[i] - 1) * (nums[j] - 1). We will take the maximum value as the answer.

Note that a pair of indices (i, j) will have the same result as (j, i). Thus, to be more efficient, we will start iterating j from i + 1. This way, we don't check any duplicate pairs.

Algorithm

Initialize the answer ans = 0.
Iterate i over the indices of nums:
Iterate j over the indices of nums, starting from i + 1:
Calculate (nums[i] - 1) * (nums[j] - 1) and update ans if it is larger.
Return ans.


Approach 2: Sort
Intuition

Intuitively, given all the candidates are non-negative, if you wanted to maximize the product of x * y, you would choose the largest values for x and y.

In this problem, we need to subtract one from our numbers before multiplying them. However, this doesn't change the logic of choosing the largest numbers, since every element will be reduced by the same amount and will still be non-negative. Thus, it is optimal for us to choose the two largest elements.

We can sort the array to easily find the two largest elements.

Algorithm

Sort nums in ascending order.
Set x as the last element in nums and y as the second last element in nums.
Return (x - 1) * (y - 1).

Approach 3: Track Second Biggest
Intuition

Without sorting, we can easily find the maximum element in nums by iterating over nums and continuously updating a variable with the largest value we see. However, we need the second largest value as well. Can we accomplish this without sorting?

We will use two variables: biggest to represent the biggest element we have seen so far, and secondBiggest to represent the second biggest element we have seen so far.

We then iterate over each num in nums. For each num, there are two possibilities:

num > biggest. We have found a new biggest element and should update biggest = num. However, before we do this, we update secondBiggest = biggest since the old biggest element we saw will become the new second biggest element.
num <= biggest. We should not update biggest. However, num may be larger than secondBiggest, in which case it would be the new second biggest element. We update secondBiggest with num if it is larger.
After iterating over all elements, we simply return (biggest - 1) * (secondBiggest - 1).

Algorithm

Initialize biggest = 0 and secondBiggest = 0.
Iterate over each num in nums:
If num > biggest:
Update secondBiggest = biggest.
Update biggest = num.
Else:
Update secondBiggest with num if it is larger.
Return (biggest - 1) * (secondBiggest - 1).

