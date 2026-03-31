class Solution:
    def time_taken(self, tup: tuple(int, int), target: int) -> float:
        return  (target - tup[0]) / tup[1]

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #make list(start_pos, speed)
        pos_speed = [(position[i], speed[i]) for i in range(len(position))]
        pos_speed = sorted(pos_speed, key= lambda x:x[0])

        #pass through stack and combine cars that meet
        stack = []
        for i in range(len(pos_speed) - 1, -1, -1):
            if i == len(pos_speed) - 1:
                stack.append(pos_speed[i])
            else:
                if self.time_taken(pos_speed[i], target) <= self.time_taken(stack[-1], target):
                    continue
                else:
                    stack.append(pos_speed[i])

        return len(stack)