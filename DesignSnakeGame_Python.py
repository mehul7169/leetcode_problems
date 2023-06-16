class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.wallWidth = width
        self.wallHeight = height
        self.score = 0
        self.snakePosition = [[0,0]]
        self.foodPosition = food
        self.dir = {
            "R" : [0, 1],
            "L" : [0, -1],
            "U" : [-1, 0],
            "D" : [1, 0]
        }
        

    def move(self, direction):
        """
        :type direction: str
        :rtype: int
        """
        currPos = self.snakePosition[-1]
        
        nextPos = [currPos[0] + self.dir[direction][0], currPos[1] + self.dir[direction][1]]
        
        self.snakePosition.pop(0)
        if nextPos in self.snakePosition or nextPos[0] < 0 or nextPos[0] >= self.wallHeight or nextPos[1] < 0 or nextPos[1] >= self.wallWidth:
            return -1

        self.snakePosition.append(nextPos)
        if len(self.foodPosition) != 0:
            if self.foodPosition[0] == nextPos:
                self.score += 1
                self.foodPosition.pop(0)
                self.snakePosition.insert(0, currPos)
            
        
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)