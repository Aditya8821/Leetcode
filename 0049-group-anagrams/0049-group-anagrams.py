class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word in d:
                d[sorted_word].append(word)
            else:
                d[sorted_word]=[word]
        final_list=[]
        for values in d.values():       
            final_list.append(values)
        return final_list
    