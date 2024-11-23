class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        start_index = max_length = 0

        for i in range(len(s)):
            if s[i] in index_map and start_index <= index_map[s[i]]:
                start_index = index_map[s[i]] + 1
            else:
                max_length = max(max_length, i - start_index + 1)

            index_map[s[i]] = i

        return max_length
        