class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap={
            "b":0,
            "a":0,
            "l":0,
            "o":0,
            "n":0,
        }
        for char in text:
            if char in hashmap:
                hashmap[char]+=1

        hashmap["l"] = hashmap["l"]//2
        hashmap["o"] = hashmap["o"]//2
        
        return min(hashmap.values())

        
#shorter solution 
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap=Counter(text)
        return min(hashmap["b"], hashmap["a"], hashmap["l"]//2,hashmap["o"]//2, hashmap["n"])

        
        