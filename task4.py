# Given an array of intergers [nums] and an interger target, 
# retun indices of the two numbers such that they add up to target

def two_sum(nums, target):
    # First create a dictionary that stores number and indices of intergers
    hash_dict = {}
    
    # Next, looping through the nums array
    for i, num in enumerate(nums):
        
        # Now calculate the complement of the current interger
        complement = target - num
        
        # Checking if the complement is already present in the dictionary
        if complement in hash_dict:
            # If it is present, we then return the indices of the compliment and the current interger
            return [hash_dict[complement], i]
        
        # Otherwise if not found, add the current integer to the dictionary with its index
        hash_dict[num] = i