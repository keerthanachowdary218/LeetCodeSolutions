class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        cities = set()
        for path in paths:
            cities.add(path[0])
        for path in paths:
            if path[1] not in cities:
                return path[1]
        return ""
        