## Two sum problem from leetcode.
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


def twoSums(nums, target):
    this_index = 0
    next_index = 1

    while True:
        if nums[this_index] + nums[next_index] == target:
            return [this_index, next_index]
        elif next_index == len(nums) - 1:
            this_index = this_index + 1
            next_index = this_index + 1
        else:
            next_index = next_index + 1


nums = [3, 3]
target = 6
result = twoSums(nums, target)
print(result)
