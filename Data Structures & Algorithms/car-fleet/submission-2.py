class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        cars = []
        for i in range(n):
            car = [position[i], speed[i]]
            cars.append(car)

        cars.sort(key = lambda x : x[0], reverse = True)

        fleets = 0
        max_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets