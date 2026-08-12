class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in maps:
                maps[sorted_word] = []
            maps[sorted_word].append(word)
        return list(maps.values())