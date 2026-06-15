class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        hashmap={}
        

        for i, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                prev_index = stack.pop()
                hashmap[prev_index] = i
            stack.append(i)
        
        while stack:
            hashmap[stack.pop()] = 0
        
        
        return [0 if hashmap[i] == 0 else hashmap[i] - i for i in range(len(temperatures))]


#soln2
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        return res