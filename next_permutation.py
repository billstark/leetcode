def nextPermutation(nums):
    changed = False
    for i in reversed(range(1, len(nums))):
        prev = i - 1
        if nums[prev] < nums[i]:
            for j in reversed(range(prev + 1, len(nums))):
                if nums[prev] < nums[j]:
                    temp = nums[j]
                    nums[j] = nums[prev]
                    nums[prev] = temp
                    t = nums[:prev + 1] + sorted(nums[prev + 1:])
                    for k in range(len(nums)):
                        nums[k] = t[k]
                    changed = True
                    return
    if not changed:
        nums.sort()
        reversed(nums)

start = [1,2,3]
for i in range(10):
    nextPermutation(start)
    print(start)
