import sys

def threeSumClosest(nums, target):
  nums.sort()
  closest = sys.maxsize
  result = 0
  for idx, a in enumerate(nums[:-2]):
    low = idx + 1
    high = len(nums) - 1
    while low < high:
      b = nums[low]
      c = nums[high]

      total = a + b + c
      diff = target - total
      if diff == 0:
        return target

      if abs(diff) < closest:
        result = total
        closest = abs(diff)
      
      if diff < 0:
        high -= 1
      else:
        low += 1

  return result

print(threeSumClosest([-1, 2, 1, -4], 1))
