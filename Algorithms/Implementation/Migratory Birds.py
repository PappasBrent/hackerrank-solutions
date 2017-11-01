n = int(input())

nums = tuple(map(int,(input().split())))

mode = nums[0]

count = -1

for i in range(1,6):
    if nums.count(i) >= count:
        if nums.count(i) == count:
            if  nums[i] < mode:
                mode = i
                count = nums.count(i)
        else:
            mode = i
            count = nums.count(i)


print(mode)