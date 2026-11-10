class UndergroundSystem:

    def __init__(self):
        # activeTrips stores id: (startStation, startTime)
        self.activeTrips = {}
        # completedTrips stores (start, end): (totalTime, numTrips)
        self.completedTrips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.activeTrips[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.activeTrips[id][0]
        startTime = self.activeTrips[id][1]
        
        # update completedTrips
        totalTime = t - startTime
        key = (startStation, stationName)
        if key in self.completedTrips:
            totalTimeSoFar, numTripsSoFar = self.completedTrips[key]
            self.completedTrips[key] = (totalTime + totalTimeSoFar, numTripsSoFar + 1)
        else:
            self.completedTrips[key] = (totalTime, 1)

        # remove from active trips
        del self.activeTrips[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, numTrips = self.completedTrips[(startStation, endStation)]

        return totalTime / numTrips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)