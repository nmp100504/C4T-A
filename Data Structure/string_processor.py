# from stack import Stack


# class StringProcessor:   #camel case
#     def reverse(self,string):
#         stack = Stack()
#         res= ""
#         for s in string:
#             stack.push(s)
#         while not stack.is_empty():
#             res+=stack.pop()
#         return res


#     def binary_string(self,number):
#         binary_stack  = Stack()
#         result =""
#         while number // 2 != 0 :
#             binary_stack.push(str(number%2))
#             new_number = number // 2
#             number = new_number
#         while not binary_stack.is_empty():
#             result += binary_stack.pop()
#         return result 


#     def is_valid(self,open_brackets,close_brackets):    
#         if open_brackets == "{":
#             if close_brackets == "}":
#                 return True
#             return False
#         if open_brackets == "[":
#             if close_brackets == "]":
#                 return True
#             return False
#         if open_brackets == "(":
#             if close_brackets == ")":
#                 return True
#             return False    
            
#     def is_balance(self,brackets):
#         stack = Stack()
#         open_brackets = ["[","(","{"]
#         close_brackets = ["]",")","}"]
#         for i in brackets:
#             if i in open_brackets:
#                 stack.push(i)
#             elif i in close_brackets:
#                 if stack.is_empty():
#                     return False
#                 temp = stack.pop()
#                 if not self.is_valid(temp,i):
#                     return False
#         return stack.is_empty()


# s = StringProcessor()
# # print(s.reverse("filo"))
# # print(s.binary_string(124))
# print(s.is_balance("[{}]"))


2*5*7+3*4   257**34*+
(1+2)*(3+4)  12+34+*
1+2*3+4+5*6  123*+456*++

