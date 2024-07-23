class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait=[]
        com=0
        for customer in customers:
            if com<customer[0]:
                com=customer[0]
            com+=customer[1]
            wait.append(com-customer[0])
        print(wait)
        avg=0
        for i in wait:
            avg+=i
        avg=avg/len(wait)
        return avg