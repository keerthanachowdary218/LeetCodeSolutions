class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        hh, mm = time.split(':')
        count_possible_hours = 1
        if (hh == '??'):
            count_possible_hours = 24
        elif (hh[0] == '?' and int(hh[1]) >= 4):
            count_possible_hours = 2
        elif (hh[0] == '?' and int(hh[1]) <= 4):
            count_possible_hours = 3
        elif (int(hh[0]) <= 1 and hh[1] == '?'):
            count_possible_hours = 10
        elif (int(hh[0]) == 2 and hh[1] == '?'):
            count_possible_hours = 4
        
        count_possible_minutes = 1
        if (mm == '??'):
            count_possible_minutes = 60
        elif (mm[0] == '?'):
            count_possible_minutes = 6
        elif (mm[1] == '?'):
            count_possible_minutes = 10

        return count_possible_hours * count_possible_minutes
        