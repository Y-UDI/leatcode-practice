# Two Sum python

Input = [4,5,21,5]
Taget = 9

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i,x in enumerate(nums):
        r = target - x
        if r in seen:
            return [seen[r], i]
        seen[x] = i