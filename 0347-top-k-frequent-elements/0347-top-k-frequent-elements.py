class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store the numbers and times they show up
        frequency = defaultdict(int)

        # Iterate through the list and group numbers and their frequency
        for num in nums:
            # Add the num to the corresponding list
            frequency[num] += 1
                
        # Now, we need to find the k most frequent elements
        # Sort the dictionary by frequency and return the top k keys
        return sorted(frequency, key=frequency.get, reverse=True)[:k]