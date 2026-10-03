class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        results = set()
        for word in words:
            code = []
            for letter in word:
                index = ord(letter)-ord("a")
                code.append(morse[index])
            morse_code = "".join(code)
            results.add(morse_code)
        return len(results)