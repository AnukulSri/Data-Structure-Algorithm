''' Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
'''

class solution():
    def multiply_string(self,num1:int,num2:int) -> str:
        s = int(num1)*int(num2)
        return str(s)
    
if __name__ == '__main__':
    num1 = 3
    num2 = 2
    s = solution()
    print(s.multiply_string(num1,num2))