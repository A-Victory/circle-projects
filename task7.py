# leetcode for Palindrome Number

def isPalindrome(x: int) -> bool:
        if x < 0 or x % 10 == 0:
            return False
        
        reversed_number = 0
        original_number = x

        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10
        
        return original_number == reversed_number