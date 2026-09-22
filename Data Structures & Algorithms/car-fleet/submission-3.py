class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_zip = sorted(zip(position, speed), reverse=True)
        times = [(((target - pos) / spd)) for pos, spd in time_zip]
        fleet_stack = []

        for t in times:
            if not fleet_stack:
                fleet_stack.append(t) # This is the car in front, with none ahead
            elif t > fleet_stack[-1]:
                fleet_stack.append(t) 
        return len(fleet_stack)











# Position: [10, 8, 0, 5, 3]
# Speed:    [2, 4, 1, 1, 3]
# Zipped:   [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
# Times:    [1.0, 1.0, 7.0, 3.0, 12.0]
# Target: 12

# Stack: [1.0]




# time = (target - position) / speed
# added = [a + b for a, b in zip(list1, list2)]          # [12, 24, 35]