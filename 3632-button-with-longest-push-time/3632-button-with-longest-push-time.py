class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        Longest_time = events[0][1]
        ButtonIndex = events[0][0]
        for i in range(1, len(events)):
            Current_Button_Time = events[i][1] - events[i - 1][1]
            Current_Index = events[i][0]
            if Current_Button_Time > Longest_time:
                Longest_time = Current_Button_Time
                ButtonIndex = Current_Index
            elif Current_Button_Time == Longest_time and Current_Index < ButtonIndex:
                Longest_time = Current_Button_Time
                ButtonIndex = Current_Index

        return ButtonIndex