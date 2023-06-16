class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.small = small
        self.medium = medium
        self.big = big
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        car = ''
        if carType == 1:
            car = self.big
            self.big -= 1
        elif carType == 2:
            car = self.medium
            self.medium -= 1
        else:
            car = self.small
            self.small -= 1
        if car <= 0:
            return False
        else:
            return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)