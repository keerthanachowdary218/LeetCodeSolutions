class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        def validIPv4(queryIP):
            IP=queryIP.split('.')
            print(IP)
            res=0
            if len(IP)==4:
                for i in IP:
                    if i.isdigit() and 0<=int(i) and int(i)<=255 and len(i)==len(str(int(i))):
                        res+=1
                if res==4:
                    return True
            return False
        def validIPv6(queryIP):
            IP = queryIP.split(':')
            if len(IP) != 8:
                return False
            hex_digits = '0123456789abcdefABCDEF'
            for i in IP:
                if 1 <= len(i) <= 4 and all(c in hex_digits for c in i):
                    continue
                else:
                    return False
            return True
        if validIPv4(queryIP):
            return "IPv4"
        if validIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
        