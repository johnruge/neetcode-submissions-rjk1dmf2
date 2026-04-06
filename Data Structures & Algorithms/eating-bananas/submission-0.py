class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed, min_speed = max(piles), math.ceil(sum(piles) / h) 
        result = max_speed

        while min_speed <= max_speed:
            speed = (max_speed + min_speed) // 2
            hours = 0 
            for p in piles:
                hours += math.ceil(p / speed)

            if h >= hours:
                result = min(result, speed)
                max_speed = speed - 1
            else:
                min_speed = speed + 1 

        return result
