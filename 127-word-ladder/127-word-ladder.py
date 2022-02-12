class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # For a faster access turing it into a set
        words = set(wordList)
        
        # Edge case
        if endWord not in words: return 0
        
        # We will be doing a Breadth First search, so we begin with placing beginWord in the queue
        queue = collections.deque([beginWord])
        count = 1
        
        # To keep a track of what words we have visited already
        seen = set()
        
        while queue:
            # Picking up every word we put from the BFS neighbours
            
            for _ in range(len(queue)):
                
                # Taking one element at a time
                word = queue.popleft()
                
                # We will not come to this word again
                seen.add(word)
                
                # Bingo, we won
                if word == endWord:
                    return count
                
                # Find the current words neighbours
                for i in range(0, len(word)):
                    
                    # Try to create the possible new words
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        
                        # Never visited this word, the word is in words
                        if new_word in words and new_word not in seen:
                            queue.append(new_word)
                            seen.add(new_word)
            count+=1 
        return 0