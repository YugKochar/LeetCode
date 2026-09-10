class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        HashLen = 256
        hash = [-1] * HashLen
        for i in range(HashLen):
            hash[i] = -1
        l , r , maxLen = 0,0,0 
        while r < n:
            if hash[ord(s[r])] != -1:
                l = max(hash[ord(s[r])]+ 1, l)
            curr_len = r-l+1
            maxLen = max(curr_len , maxLen)
            hash[ord(s[r])] = r
            r+=1
        return maxLen