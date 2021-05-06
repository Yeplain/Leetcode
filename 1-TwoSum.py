#暴力求解法
def twoSum(self, nums, sum):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == sum:
                return [i, j]

#哈希表
def twoSum(self, nums, sum):
    dic = {}
    for i, m in enumerate(nums):
        if sum - m in dic:
            return [dic[sum-m], i]
        else:
            dic[m] = i
