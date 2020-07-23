# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:07:04 2019

@author: leiya
"""



'''
0723
这道题最重要的条件在于没有重复的数字，如果存在重复的数字那么就需要考虑重复数字的处理问题，这一点参考34
'''
#0702 即使目标值不存在需要插入，目标值也绝对不可能插入到比他小的value对应的index处,这会产生一个问题，那就是如果num最后一个数也小于target，那么需要返回的
#index 在 nums中是找不到的，这个特殊情况需要单独处理
#0620 updated:重新更新二分法模板，注意left = mid时需要向上取整即mid = (left+right+1) // 2,为了避免死循环出现
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        #注意结尾的边界值问题
        #需要判断特例，因为这种情况left,right都遍历不到
        if nums[right] < target:
            return right + 1
        #注意此处没有等于号
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        #需要判断特例，因为这种情况left,right都遍历不到
        if nums[right] < target:
            return right+1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left
#----------------------------------------------------------------------------
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
                else:
                    pass
            return len(nums)
        
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            if target > nums[i]:
                count += 1
            
        return count
    

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        if target in nums:
            #more faster
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target > nums[i]:
                    count += 1
            return count
        