class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: # While stack has items and current temperature is > temperature in stack
                j = stack.pop() # Pop the temperature's indice in the stack
                result[j] = i - j # Subtract and find the days in between the current temp day and the next highest temp day, and add to result list
            stack.append(i) # Push the next indice
        return result