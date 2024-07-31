class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words)==1:
            return 1
        MORSE = {
		'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',    'f': '..-.', 'g': '--.',
		'h': '....', 'i': '..',   'j': '.---', 'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',
		'o': '---',  'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '...',  't': '-',    'u': '..-',
		'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--', 'z': '--..',
	}
        res=[]
        for word in words:
            mapp=''
            for letter in word:
                mapp+=MORSE[letter]
            res.append(mapp)
        return len(set(res))
            
        