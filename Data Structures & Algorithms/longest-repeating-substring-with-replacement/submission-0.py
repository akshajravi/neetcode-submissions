class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #important check is if windowsize - max freq in window <= k
        #this makes sense bc if windowsize - max freq was greater than k, we wouldnt be able to replace all other characters that arent off same type

        left = 0
        max_length = 0
        freq = dict()
        max_freq = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1
            max_freq = max(max_freq,freq[s[right]])

            window_size = right - left + 1
            

            while window_size - max_freq > k:
                freq[s[left]] -= 1
                left += 1
                window_size = right - left + 1
            
            max_length = max(max_length,window_size)

        return max_length

