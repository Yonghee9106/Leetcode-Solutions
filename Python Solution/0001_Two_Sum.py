class Solution:
    def twoSum(self, nums, target):             # type nums: List[int], type target: int
        diff_dic = {}                           # key: num, value: index
        for index, num in enumerate(nums):      # enumerate() returns index and value(num)
            diff = target - num
            if diff in diff_dic:                # if there is diff in diff_dic
                return [diff_dic[diff], index]  # they are the two sum combination
            diff_dic[num] = index
        return print("No two sum solution!")


print(Solution().twoSum([2, 7, 11, 15], 9))
