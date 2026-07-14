# Last updated: 7/14/2026, 1:57:18 PM
class Solution:
    def carFleet(self, target, position, speed):

        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        fleets = 0
        last_time = 0

        for pos, spd in cars:

            time = (target - pos) / spd

            if time > last_time:
                fleets += 1
                last_time = time

        return fleets