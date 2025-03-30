class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        mapp=defaultdict(int)
        for num,i in enumerate(s):
            mapp[i]=num
        print(mapp)
        part=[]
        curr=0
        parti=0
        for num,i in enumerate(s):
            curr=max(curr,mapp[i])
            if num==curr:
                part.append(curr-parti+1)
                parti=num+1
        return part
