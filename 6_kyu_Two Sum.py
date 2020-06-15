def two_sum(nums, target):
      return next((i, j)  for i in range(len(nums)) for j in range(len(nums[:i])) if nums[i] + nums[j] == target)
