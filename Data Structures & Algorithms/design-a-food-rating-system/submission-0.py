class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToRating = {}
        self.foodToCuisine = {}
        self.cuisineToHeap = {}

        for i in range(len(foods)):
            self.foodToRating[foods[i]] = ratings[i]
            self.foodToCuisine[foods[i]] = cuisines[i]

            if cuisines[i] in self.cuisineToHeap:
                heapq.heappush(self.cuisineToHeap[cuisines[i]], (-ratings[i], foods[i]))
            else:
                self.cuisineToHeap[cuisines[i]] = []
                heapq.heappush(self.cuisineToHeap[cuisines[i]], (-ratings[i], foods[i]))

        
    def changeRating(self, food: str, newRating: int) -> None:
        self.foodToRating[food] = newRating
        cuisine = self.foodToCuisine[food]
        heapq.heappush(self.cuisineToHeap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        cuisineHeap = self.cuisineToHeap[cuisine]

        while -cuisineHeap[0][0] != self.foodToRating[cuisineHeap[0][1]]:
            heapq.heappop(cuisineHeap)

        return cuisineHeap[0][1]

