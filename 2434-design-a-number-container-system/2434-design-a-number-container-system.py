class NumberContainers:
    #I can use one array .. but memory limit
    '''
    def __init__(self):
        # Initialize an empty array to store numbers at their respective indices
        self.array = []

    def change(self, index: int, number: int) -> None:
        # If the index is beyond the current array size, extend the array
        while len(self.array) <= index:
            self.array.append(None)
        
        # Update the number at the given index
        self.array[index] = number

    def find(self, number: int) -> int:
        # Iterate through the array to find the smallest index with the given number
        for i in range(len(self.array)):
            if self.array[i] == number:
                return i
        return -1
    '''
    def __init__(self):
        # Map to store number -> min heap of indices
        self.number_to_indices = defaultdict(list)
        # Map to store index -> number
        self.index_to_numbers = {}

    def change(self, index: int, number: int) -> None:
        # Update index to number mapping
        self.index_to_numbers[index] = number

        # Add index to the min heap for this number
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        # If number doesn't exist in our map
        if not self.number_to_indices[number]:
            return -1

        # Keep checking top element until we find valid index
        while self.number_to_indices[number]:
            index = self.number_to_indices[number][0]

            # If index still maps to our target number, return it
            if self.index_to_numbers.get(index) == number:
                return index

            # Otherwise remove this stale index
            heapq.heappop(self.number_to_indices[number])
        return -1
