class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        time_stack = []

        for pos, spd in pairs:
            time = (target - pos) / spd
            if not time_stack or time > time_stack[-1]:
                time_stack.append(time)

        return len(time_stack)