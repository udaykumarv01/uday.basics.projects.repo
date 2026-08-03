class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i 
    number =input("enter an array : ")
    tar=input("enter the wanted sum number :")
    sol=twoSum(number,tar)
    sol.twoSum()