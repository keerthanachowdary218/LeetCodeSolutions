class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters=''
        for i in licensePlate:
            if i.isalpha():
                letters+=i.lower()
        print(letters)
        license_count = {}
        for letter in letters:
            if letter in license_count:
                license_count[letter] += 1
            else:
                license_count[letter] = 1
        def can_complete(word, license_count):
            word_count = {}
            for char in word:
                if char in word_count:
                    word_count[char] += 1
                else:
                    word_count[char] = 1
            
            # Check if the word contains all letters with at least the required frequency
            for char in license_count:
                if word_count.get(char, 0) < license_count[char]:
                    return False
            return True

        # Find the shortest completing word
        shortest_word = None
        for word in words:
            if can_complete(word, license_count):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word

        return shortest_word
        

        