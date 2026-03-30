class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))

        for _, i in stack:
            res[i] = 0

        return res