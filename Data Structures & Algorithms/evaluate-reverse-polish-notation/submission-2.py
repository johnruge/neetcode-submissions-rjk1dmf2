class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = tokens[:2]
        ops = {"+", "-", "/", "*"}
        for i in range(2, len(tokens)):
            if tokens[i] in ops:
                op = tokens[i]
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if op == "+":
                    stack.append(num1 + num2)
                elif op == "-":
                    stack.append(num1 - num2)
                elif op == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
            else:
                stack.append(tokens[i])
                
        return int(stack[0])