class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom=Counter(ransomNote)
        count_mag=Counter(magazine)
        return count_ransom==count_ransom & count_mag
        
        # for i in ransomNote:
        #     if i in magazine:
        #         magazine=magazine.replace(i,"",1)
        #     else: return False
        # return True