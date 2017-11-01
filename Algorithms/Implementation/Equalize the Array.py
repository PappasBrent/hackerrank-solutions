n = int(input())

nums = tuple(map(int, input().split()))

modeCount = -1
mode = nums[0]

for num in nums:
    if nums.count(num) > modeCount:
        mode = num
        modeCount = nums.count(num)

toRemove = 0

for num in nums:
    if num!=mode:
        toRemove+=1

print(toRemove)