class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        A=s
        B=goal
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) < len(A):
            return True
        differences = []
        for x in range(len(B)):
            if A[x] != B[x]:
                differences.append([A[x], B[x]])

        if len(differences) == 2 and differences[0] == differences[-1][::-1]:
            return True
        return False
        