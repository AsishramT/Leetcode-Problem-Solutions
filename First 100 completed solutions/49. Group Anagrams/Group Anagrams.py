class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper=defaultdict(list)
        for word in strs:
            sorted_word=''.join(sorted(word))
            mapper[sorted_word].append(word)
        

        return list(mapper.values())





        