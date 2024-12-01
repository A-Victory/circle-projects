# leetcode for longest prefix

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]

    for s in strs:
        while len(prefix) > len(s) or s[:len(prefix)] != prefix:
            prefix = prefix[:len(prefix)-1]
            if prefix == "":
                return ""

    return prefix
        