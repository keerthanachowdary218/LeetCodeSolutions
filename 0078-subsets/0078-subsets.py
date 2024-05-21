import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        k=[[]]
        for i in range(1,len(nums)+1):
            #print((itertools.combinations(nums,i)))
            #there is a difference between append and extend , here we need to use extend insteas of append - check different between append and extend- append(single element) where as extend(iterable)
            k.extend(list(j) for j in itertools.combinations(nums,i))
        return (k)