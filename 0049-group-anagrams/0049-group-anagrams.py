class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Handle edge cases for single or empty input
        if len(strs) == 1:
            return [[strs[0]]]
        elif len(strs) == 0:
            return []

        # Create a dictionary to store grouped anagrams
        anagrams = defaultdict(list)

        # Iterate through the list and group anagrams by their sorted string
        for string in strs:
            # Sort the string and use it as the key
            sorted_str = ''.join(sorted(string))
            # Add the original string to the corresponding list
            anagrams[sorted_str].append(string)
        
        # Return all the grouped anagrams as a list of lists
        return list(anagrams.values())