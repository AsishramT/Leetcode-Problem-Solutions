class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for op in operations:
            if op.isdigit():
                stack.append(int(op))
            elif op =="C":
                stack.pop()
            elif op =="D":
                num=stack[-1]
                num*=2
                stack.append(num)
            elif op == "+":
                s=stack[-1]
                s2=stack[-2]
                stack.append(s+s2)
            elif op[0]=="-":
                stack.append(-1*int(op[1:]))
        return sum(stack)


        


        