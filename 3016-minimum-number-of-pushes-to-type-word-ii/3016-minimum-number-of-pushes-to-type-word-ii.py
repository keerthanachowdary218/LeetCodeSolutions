class Solution:
    def minimumPushes(self, word: str) -> int:
        count = [0] * 26
        for x in word:
            idx = ord(x) - ord('a')
            count[idx] += 1
        count = sorted(count, reverse=True)
        ans = sum(count[:8]) * 1
        ans += sum(count[8:16]) * 2
        ans += sum(count[16:24]) * 3
        ans += sum(count[24:]) * 4
        return ans
        