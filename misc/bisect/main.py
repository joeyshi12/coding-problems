def bisect_left(nums: list[int], x: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return right

def bisect_right(nums: list[int], x: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

print("bisect_left")
nums = [1,3,5,8,9,10]
x = 7
print(nums, x)
print(bisect_left(nums, x))

print("bisect_right")
nums = [1,3,5,8,9,10]
x = 7
print(nums, x)
print(bisect_right(nums, x))
