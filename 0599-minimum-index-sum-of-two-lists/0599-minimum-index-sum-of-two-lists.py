class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {restaurant: i for i, restaurant in enumerate(list1)}
        dic2 = {restaurant: dic1[restaurant] + i for i, restaurant in enumerate(list2) if restaurant in dic1}
        MIN = float('inf')
        res = []
        for key, val in dic2.items():
            if val < MIN:
                res = [key]
                MIN = val
            elif val == MIN:
                res.append(key)
                
        return res
        