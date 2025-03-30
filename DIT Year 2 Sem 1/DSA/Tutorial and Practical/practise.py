def triangle(n):
    for i in range(n):
        for j in range(i):
            print("* ", end='')
        print("")

    for i in range(n, 0, -1):
        for k in range(i):
            print("* ", end='')
        print("")



def numberPattern(n):
    for i in range(n+1):
        for j in range(i):
            print(i, end='')
        print("")


def search(self, nums: list[int], target: int) -> int:
    min = 0
    max = len(nums) - 1

    while min <= max:
        mid = (min + max) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            min = mid + 1
        elif nums[mid] > target:
            max = mid - 1
    return -1


def searchRange(self, nums: list[int], target: int) -> list[int]:
    min = 0
    max = len(nums) - 1
    output = [-1, -1]
    start = 0
    end = 0

    while min <= max:
        mid = (min + max) // 2
        if nums[mid] == target:
            start = mid
            end = mid
            counter = True
            while counter:
                if start == -1 or end > len(nums):
                    counter = False
                elif nums[start - 1] == target and start != -1:
                    start -= 1
                elif nums[end + 1] == target and end != len(nums):
                    end += 1
                else:
                    counter = False

            output = [start, end]
            return output

        elif nums[mid] < target:
            min = mid + 1
        elif nums[mid] > target:
            max = mid - 1
    return output


searchRange([1], 1)