class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Hashmap =  {} # val: index

        for i,n in enumerate(numbers):
            diff = target - n
            if diff in Hashmap:
                return [Hashmap[diff] + 1, i + 1]
            Hashmap[n] = i
        return
                