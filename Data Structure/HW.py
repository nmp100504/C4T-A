from stack import Stack

class PolishNotation:
    def pn(self,string):    
        stack_1 = Stack()
        res = 0
        signs = ["+","-","*","/"]
        for i in string:
            if not str(i) in signs:
                stack_1.push(int(i))
            elif str(i) in signs:
                if i == "+":
                    res = stack_1.items[-1] + stack_1.items[-2]
                    stack_1.pop()
                    stack_1.pop()
                    stack_1.push(res)
                if i == "-":
                    res = stack_1.items[-1] - stack_1.items[-2]
                    stack_1.pop()
                    stack_1.pop()
                    stack_1.push(res)
                if i == "*":
                    res = stack_1.items[-1] * stack_1.items[-2]
                    stack_1.pop()
                    stack_1.pop()
                    stack_1.push(res)
                if i == "/":
                    res = stack_1.items[-1] / stack_1.items[-2]
                    stack_1.pop()
                    stack_1.pop()
                    stack_1.push(res)
        return stack_1.items
s = PolishNotation()
print(s.pn("123*+34*+"))
        


