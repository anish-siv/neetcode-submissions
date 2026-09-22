class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        run_max = 0
        fleet_count = 0

        for pos, spd in pairs:
            time = (target - pos) / spd
            if time > run_max:
                run_max = time
                fleet_count += 1
        return fleet_count
